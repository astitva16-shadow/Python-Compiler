"""
Python Compiler Backend API
Flask server for executing Python code with security and isolation
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import io
import traceback
import subprocess
import tempfile
import os
import threading
import time
from contextlib import redirect_stdout, redirect_stderr
import json

# Platform-specific imports
try:
    import signal
    import resource
    UNIX_PLATFORM = True
except ImportError:
    UNIX_PLATFORM = False

app = Flask(__name__, static_folder='.')
CORS(app)

# Configuration
MAX_EXECUTION_TIME = 10  # seconds
MAX_MEMORY = 128 * 1024 * 1024  # 128 MB
MAX_OUTPUT_LENGTH = 10000  # characters

class ExecutionTimeout(Exception):
    """Raised when code execution times out"""
    pass

def timeout_handler(signum, frame):
    """Handle execution timeout"""
    raise ExecutionTimeout("Code execution timed out")

def limit_memory():
    """Limit memory usage of the process (Unix only)"""
    if UNIX_PLATFORM:
        try:
            resource.setrlimit(resource.RLIMIT_AS, (MAX_MEMORY, MAX_MEMORY))
        except:
            pass

@app.route('/')
def index():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/api/execute', methods=['POST'])
def execute_code():
    """
    Execute Python code in a controlled environment
    
    Request JSON:
    {
        "code": "print('Hello, World!')",
        "method": "direct|subprocess"
    }
    
    Response JSON:
    {
        "success": true|false,
        "stdout": "output string",
        "stderr": "error string",
        "execution_time": 0.123,
        "error": "error message if any"
    }
    """
    try:
        data = request.get_json()
        code = data.get('code', '')
        method = data.get('method', 'direct')
        
        if not code or not code.strip():
            return jsonify({
                'success': False,
                'error': 'No code provided'
            }), 400
        
        # Check code length
        if len(code) > 50000:
            return jsonify({
                'success': False,
                'error': 'Code too long (max 50000 characters)'
            }), 400
        
        # Execute based on method
        if method == 'subprocess':
            result = execute_subprocess(code)
        else:
            result = execute_direct(code)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

def execute_direct(code):
    """
    Execute code directly in the current process with timeout (Unix only)
    More dangerous but faster. On Windows, uses threading timeout instead.
    """
    start_time = time.time()
    
    # Create string buffers for output
    stdout_buffer = io.StringIO()
    stderr_buffer = io.StringIO()
    
    if UNIX_PLATFORM:
        # Set up timeout handler (Unix only)
        old_handler = signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(MAX_EXECUTION_TIME)
    
    try:
        # Redirect stdout and stderr
        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            # Create restricted namespace
            namespace = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__doc__': None,
            }
            
            # Execute the code
            exec(code, namespace)
        
        execution_time = time.time() - start_time
        stdout = stdout_buffer.getvalue()
        stderr = stderr_buffer.getvalue()
        
        # Truncate output if too long
        if len(stdout) > MAX_OUTPUT_LENGTH:
            stdout = stdout[:MAX_OUTPUT_LENGTH] + '\n... (output truncated)'
        if len(stderr) > MAX_OUTPUT_LENGTH:
            stderr = stderr[:MAX_OUTPUT_LENGTH] + '\n... (output truncated)'
        
        return {
            'success': True,
            'stdout': stdout,
            'stderr': stderr,
            'execution_time': round(execution_time, 3)
        }
    
    except ExecutionTimeout:
        return {
            'success': False,
            'stdout': stdout_buffer.getvalue(),
            'stderr': stdout_buffer.getvalue(),
            'error': f'Execution timed out after {MAX_EXECUTION_TIME} seconds'
        }
    
    except Exception as e:
        return {
            'success': False,
            'stdout': stdout_buffer.getvalue(),
            'stderr': stderr_buffer.getvalue() + traceback.format_exc(),
            'error': str(e)
        }
    
    finally:
        if UNIX_PLATFORM:
            # Cancel alarm and restore handler (Unix only)
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)

def execute_subprocess(code):
    """
    Execute code in a separate subprocess (safer, more isolated)
    """
    start_time = time.time()
    
    try:
        # Create temporary file with the code
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            temp_file = f.name
            f.write(code)
        
        # Execute in subprocess with timeout
        process = subprocess.Popen(
            [sys.executable, temp_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            preexec_fn=limit_memory if os.name != 'nt' else None
        )
        
        try:
            stdout, stderr = process.communicate(timeout=MAX_EXECUTION_TIME)
            execution_time = time.time() - start_time
            
            # Truncate output if too long
            if len(stdout) > MAX_OUTPUT_LENGTH:
                stdout = stdout[:MAX_OUTPUT_LENGTH] + '\n... (output truncated)'
            if len(stderr) > MAX_OUTPUT_LENGTH:
                stderr = stderr[:MAX_OUTPUT_LENGTH] + '\n... (output truncated)'
            
            return {
                'success': process.returncode == 0,
                'stdout': stdout,
                'stderr': stderr,
                'execution_time': round(execution_time, 3),
                'return_code': process.returncode
            }
        
        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = process.communicate()
            return {
                'success': False,
                'stdout': stdout,
                'stderr': stderr,
                'error': f'Execution timed out after {MAX_EXECUTION_TIME} seconds'
            }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'Subprocess execution failed: {str(e)}'
        }
    
    finally:
        # Clean up temporary file
        try:
            if 'temp_file' in locals():
                os.unlink(temp_file)
        except:
            pass

@app.route('/api/install', methods=['POST'])
def install_package():
    """
    Install a Python package using pip
    
    Request JSON:
    {
        "package": "numpy"
    }
    
    Response JSON:
    {
        "success": true|false,
        "message": "Installation message",
        "output": "pip output"
    }
    """
    try:
        data = request.get_json()
        package = data.get('package', '').strip()
        
        if not package:
            return jsonify({
                'success': False,
                'error': 'No package name provided'
            }), 400
        
        # Validate package name (basic security)
        if not package.replace('-', '').replace('_', '').replace('.', '').isalnum():
            return jsonify({
                'success': False,
                'error': 'Invalid package name'
            }), 400
        
        # Install package
        process = subprocess.Popen(
            [sys.executable, '-m', 'pip', 'install', package],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(timeout=60)  # 60 second timeout
        
        if process.returncode == 0:
            return jsonify({
                'success': True,
                'message': f'Successfully installed {package}',
                'output': stdout
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Failed to install {package}',
                'output': stderr
            })
    
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Installation timed out'
        }), 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/packages', methods=['GET'])
def list_packages():
    """
    List installed Python packages
    
    Response JSON:
    {
        "packages": [
            {"name": "numpy", "version": "1.21.0"},
            ...
        ]
    }
    """
    try:
        process = subprocess.Popen(
            [sys.executable, '-m', 'pip', 'list', '--format=json'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = process.communicate(timeout=10)
        
        if process.returncode == 0:
            packages = json.loads(stdout)
            return jsonify({
                'success': True,
                'packages': packages
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to list packages'
            }), 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'python_version': sys.version,
        'max_execution_time': MAX_EXECUTION_TIME,
        'max_memory': MAX_MEMORY
    })

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🐍 Python Compiler Backend Server")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Max Execution Time: {MAX_EXECUTION_TIME}s")
    print(f"Max Memory: {MAX_MEMORY / (1024*1024)}MB")
    print("=" * 60)
    print("\n🚀 Server starting on http://localhost:5000")
    print("📝 Open http://localhost:5000 in your browser\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
