# Backend Setup Guide

## 🚀 Quick Start

### 1. Install Python
Make sure you have Python 3.8 or higher installed:
```bash
python --version
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Backend Server
```bash
python app.py
```

The server will start on `http://localhost:5000`

### 4. Open the Frontend
Open `http://localhost:5000` in your browser, or open `index.html` directly.

---

## 📋 Detailed Setup

### Windows (PowerShell)

```powershell
# Navigate to project directory
cd E:\Astitva\Frontend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

### Linux / macOS

```bash
# Navigate to project directory
cd /path/to/Frontend

# Create virtual environment (optional but recommended)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

---

## 🔧 Configuration

### Server Settings

Edit `app.py` to customize:

```python
# Maximum execution time (seconds)
MAX_EXECUTION_TIME = 10

# Maximum memory (bytes)
MAX_MEMORY = 128 * 1024 * 1024  # 128 MB

# Maximum output length (characters)
MAX_OUTPUT_LENGTH = 10000
```

### Port Configuration

Change the port in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

Also update `BACKEND_URL` in `index.html`:

```javascript
const BACKEND_URL = 'http://localhost:5000/api';  // Change 5000 to your port
```

---

## 🌐 Execution Modes

The IDE supports three execution modes:

### 1. **Auto Mode** (Recommended)
- Automatically selects server if available, otherwise browser
- Best balance of performance and convenience

### 2. **Server Mode**
- Executes code on backend server
- ✅ Better performance for CPU-intensive tasks
- ✅ No browser memory limits
- ✅ Real Python packages (NumPy, Pandas, etc.)
- ⚠️ Requires backend server running

### 3. **Browser Mode**
- Executes code in browser using Pyodide (WebAssembly)
- ✅ Works offline
- ✅ No server required
- ⚠️ Limited to pure Python packages
- ⚠️ Slower for heavy computations

---

## 🔒 Security Considerations

### ⚠️ WARNING: Development Only

This backend is **NOT secure for production use**. It executes arbitrary Python code without sandboxing.

### For Production:

1. **Use Docker containers** for isolation
2. **Implement user authentication**
3. **Rate limiting** to prevent abuse
4. **Resource quotas** per user
5. **Code validation** and sanitization
6. **Network isolation**
7. **Audit logging**

### Recommended Production Solutions:

- **Docker + cgroups** for resource limits
- **Kubernetes** for scalability
- **Judge0** or **Sphere Engine** for secure code execution
- **AWS Lambda** or **Google Cloud Functions** for serverless

---

## 📦 API Endpoints

### `GET /`
Serves the main HTML file

### `POST /api/execute`
Execute Python code

**Request:**
```json
{
  "code": "print('Hello')",
  "method": "direct|subprocess"
}
```

**Response:**
```json
{
  "success": true,
  "stdout": "Hello\n",
  "stderr": "",
  "execution_time": 0.123
}
```

### `POST /api/install`
Install Python package

**Request:**
```json
{
  "package": "numpy"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Successfully installed numpy",
  "output": "..."
}
```

### `GET /api/packages`
List installed packages

**Response:**
```json
{
  "success": true,
  "packages": [
    {"name": "numpy", "version": "1.21.0"},
    ...
  ]
}
```

### `GET /api/health`
Health check

**Response:**
```json
{
  "status": "healthy",
  "python_version": "3.11.0",
  "max_execution_time": 10,
  "max_memory": 134217728
}
```

---

## 🐛 Troubleshooting

### Server won't start

**Error:** `Address already in use`

**Solution:** Port 5000 is already in use. Either:
1. Kill the process using port 5000
2. Change the port in `app.py`

```bash
# Windows - Find process on port 5000
netstat -ano | findstr :5000

# Windows - Kill process
taskkill /PID <PID> /F

# Linux/Mac - Find and kill
lsof -ti:5000 | xargs kill -9
```

### CORS Errors

**Error:** `Access to fetch blocked by CORS policy`

**Solution:** Make sure Flask-CORS is installed:
```bash
pip install flask-cors
```

### Module Import Errors

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:** Install requirements:
```bash
pip install -r requirements.txt
```

### Connection Refused

**Error:** `Failed to fetch` or `Connection refused`

**Solution:**
1. Make sure backend server is running
2. Check the URL in browser matches `BACKEND_URL` in `index.html`
3. Try accessing `http://localhost:5000/api/health` directly

---

## 🚀 Deployment

### Local Network Access

To allow other devices on your network to access:

```python
# In app.py
app.run(debug=False, host='0.0.0.0', port=5000)
```

Then access from other devices using:
```
http://<your-ip-address>:5000
```

### Production Deployment

For production, use a proper WSGI server:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Or with uWSGI:

```bash
# Install uwsgi
pip install uwsgi

# Run with uwsgi
uwsgi --http 0.0.0.0:5000 --wsgi-file app.py --callable app --processes 4
```

---

## 📊 Performance Tips

1. **Use subprocess execution** for better isolation
2. **Set appropriate timeouts** to prevent hanging
3. **Limit memory usage** to prevent crashes
4. **Use caching** for frequently installed packages
5. **Implement rate limiting** to prevent abuse

---

## 🔗 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [Python Subprocess](https://docs.python.org/3/library/subprocess.html)
- [Resource Limits](https://docs.python.org/3/library/resource.html)

---

**Need help?** Open an issue on GitHub or contact the maintainer.
