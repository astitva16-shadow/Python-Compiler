# 🐍 Python IDE - Full-Stack Compiler

A modern, fully-functional Python IDE with **dual execution modes**: run code server-side with full Python support OR client-side in the browser using WebAssembly (Pyodide).

![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## ✨ Features

### 🎨 Modern UI/UX
- **Professional Design** - Clean, dark-themed interface with smooth animations
- **Responsive Layout** - Works seamlessly on desktop, tablet, and mobile devices
- **Split Panel View** - Code editor and output panel side-by-side
- **Line Numbers** - Synchronized line numbers with scroll support
- **Syntax Highlighting** - Monospace font with clear code visibility

### ⚡ Code Editor Features
- **10 Built-in Templates** - Quick start with common Python patterns
- **File Upload/Download** - Import and export `.py` files
- **Keyboard Shortcuts** - `Ctrl+Enter` to run, `Tab` for indentation
- **Auto-indentation** - Tab key inserts 4 spaces
- **Code Persistence** - Your code stays in the browser

### 🚀 Dual Execution Modes
- **Server Mode** - Real Python backend with Flask (all packages, better performance)
- **Browser Mode** - WebAssembly/Pyodide (offline, no server needed)
- **Auto Mode** - Automatically selects best available option

### 🔧 Backend Server Features
- **Real Python Execution** - Full Python 3.13 environment
- **All Packages** - Install any package via pip (NumPy, Pandas, Requests, etc.)
- **Subprocess Isolation** - Secure code execution
- **Timeout Protection** - Configurable execution limits
- **REST API** - Clean API endpoints for code execution
- **Auto-Browser Launch** - Opens default browser automatically

### 📦 Package Management
- **Server Mode** - Install ANY Python package via pip
- **Browser Mode** - Pure Python packages via micropip
- **One-click Install** - Simple package installation interface

### 🎯 Execution & Output
- **Real-time Execution** - Run Python code instantly
- **Execution Timer** - Track how long your code takes to run
- **Color-coded Output** - Success (green), errors (red), info (blue)
- **Output Management** - Clear, copy, and download output
- **Error Handling** - Clear error messages with stack traces

## 🎯 Built-in Code Templates

1. **Hello World** - Simple introduction
2. **Fibonacci Sequence** - Recursive number generation
3. **Prime Numbers** - Prime number finder
4. **Factorial Calculator** - Recursive factorial
5. **Palindrome Checker** - String manipulation
6. **Sorting Algorithms** - Bubble sort implementation
7. **List Operations** - Common list methods
8. **Classes and Objects** - OOP example
9. **File Operations** - Virtual filesystem demo
10. **Matplotlib Plot** - Data visualization

## 🚀 Getting Started

### Quick Start (Easiest - Windows)

1. **Double-click `start.bat`**
   - Automatically installs dependencies
   - Starts the Flask backend server
   - Opens your default browser
   - Ready to code!

### Quick Start (Linux/macOS)

```bash
chmod +x start.sh
./start.sh
```

### Manual Setup

#### Option 1: With Backend Server (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server (auto-opens browser)
python app.py
```

Then your browser will open automatically at `http://localhost:5000`

#### Option 2: Browser-Only Mode (No Server)

Simply open `index.html` in any modern browser (Chrome, Firefox, Edge, Safari).
- No installation needed
- Works offline
- Limited to pure Python packages

#### Option 3: Local Server for Static Files

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

Then navigate to `http://localhost:8000`

## 🔧 Execution Modes

### Auto Mode (Default)
- Automatically uses backend if available
- Falls back to browser mode if server is offline
- Best of both worlds

### Server Mode
- ✅ Full Python 3.13 environment
- ✅ All pip packages available
- ✅ Better performance
- ✅ Real file system access
- ✅ Network requests
- ⚠️ Requires backend server running

### Browser Mode
- ✅ Works offline
- ✅ No server required
- ✅ Safe sandboxed execution
- ⚠️ Limited to pure Python packages
- ⚠️ Slower for heavy computations

## 📖 Usage Guide

### Running Code
1. **Write Code** - Type or paste Python code in the editor
2. **Run** - Click "Run Code" button or press `Ctrl+Enter`
3. **View Output** - Results appear in the output panel

### Loading Templates
1. Click the **"Load Template..."** dropdown
2. Select any template from the list
3. Template code loads into the editor

### Installing Packages
```python
# Example: Install NumPy
1. Type "numpy" in the package input field
2. Click "Install" button
3. Wait for installation to complete
4. Use the package in your code:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())
```

### File Management
- **Upload**: Click "Upload" to load a `.py` file from your computer
- **Download**: Click "Download" to save your code as a `.py` file
- **Clear**: Click "Clear" to start fresh (with confirmation)

### Keyboard Shortcuts
| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Run code |
| `Tab` | Insert 4 spaces |
| `Enter` (in package input) | Install package |

## 🛠️ Technical Details

### Technologies Used
- **Backend**: Python 3.13, Flask 3.0, Flask-CORS
- **Frontend**: HTML5/CSS3, Vanilla JavaScript
- **Browser Runtime**: Pyodide (WebAssembly)
- **Fonts**: Google Fonts (Inter & JetBrains Mono)

### Architecture
```
┌─────────────────────────────────────┐
│         Frontend (HTML/JS)          │
│  ┌─────────────────────────────┐   │
│  │   Editor   │    Output      │   │
│  └─────────────────────────────┘   │
└──────────┬──────────────┬───────────┘
           │              │
    ┌──────▼──────┐  ┌───▼──────────┐
    │   Flask     │  │   Pyodide    │
    │   Backend   │  │  (Browser)   │
    │  (Server)   │  │ (WebAssembly)│
    └─────────────┘  └──────────────┘
     Server Mode      Browser Mode
```

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Firefox 90+
- ✅ Edge 90+
- ✅ Safari 14+

### Performance
- **Backend Server** - Near-native Python speed, better for heavy computations
- **Browser Mode** - ~5-10 seconds initial load (Pyodide download)
- **Package Installation** - Server: seconds, Browser: varies by package size

## 📦 Supported Packages

### Server Mode (All Packages)
Install ANY Python package via pip:
- **NumPy** - Numerical computing
- **Pandas** - Data analysis  
- **Matplotlib** - Data visualization
- **SciPy** - Scientific computing
- **Requests** - HTTP library
- **BeautifulSoup** - Web scraping
- **Pillow** - Image processing
- **Flask, Django** - Web frameworks
- **TensorFlow, PyTorch** - Machine learning
- And thousands more!

### Browser Mode (Pure Python Only)
Pyodide-compatible packages:
- **NumPy** - Numerical computing
- **Pandas** - Data analysis
- **Matplotlib** - Data visualization
- **SciPy** - Scientific computing
- **SymPy** - Symbolic mathematics
- **Pillow** - Image processing

[Full Pyodide package list](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)

## ⚠️ Limitations

### Backend Server Mode
- **Security Warning**: Not production-ready (no sandboxing)
- Development use only
- No multi-user support
- No rate limiting
- See `BACKEND_SETUP.md` for production considerations

### Browser Mode
- **No C Extensions** - Only pure Python packages work
- **No Threading** - Limited to single-threaded execution
- **Memory Limits** - Browser memory constraints apply
- **Long Operations** - May block UI (use with caution)
- **File System** - Virtual filesystem (not persistent)

## 🎨 Customization

### Color Scheme
Edit the CSS variables in `index.html`:

```css
:root {
  --bg-primary: #0a0e1a;
  --bg-secondary: #0f1419;
  --accent-primary: #3b82f6;
  /* ... more variables */
}
```

### Templates
Add your own templates in the `templates` object:

```javascript
const templates = {
  mytemplate: {
    name: 'My Template',
    description: 'Custom template',
    code: `# Your code here`
  }
};
```

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Pyodide](https://pyodide.org/) - Python runtime for the browser
- [Google Fonts](https://fonts.google.com/) - Typography
- [GitHub](https://github.com/) - Code hosting

## 📞 Support

If you encounter any issues or have questions:

- 🐛 [Report a Bug](https://github.com/astitva16-shadow/Python-Compiler/issues)
- 💡 [Request a Feature](https://github.com/astitva16-shadow/Python-Compiler/issues)
- 📧 Contact: astitva16-shadow@users.noreply.github.com
- 📚 Documentation: See `QUICKSTART.md` and `BACKEND_SETUP.md`

## 🔗 Links

- **Repository**: [github.com/astitva16-shadow/Python-Compiler](https://github.com/astitva16-shadow/Python-Compiler)
- **Flask Docs**: [flask.palletsprojects.com](https://flask.palletsprojects.com/)
- **Pyodide Docs**: [pyodide.org](https://pyodide.org/)
- **Python Docs**: [docs.python.org](https://docs.python.org/)

## 📁 Project Structure

```
Python-Compiler/
├── index.html              # Main IDE interface
├── app.py                  # Flask backend server
├── requirements.txt        # Python dependencies
├── start.bat              # Windows startup script
├── start.sh               # Linux/macOS startup script
├── README.md              # This file
├── QUICKSTART.md          # Quick start guide
├── BACKEND_SETUP.md       # Backend configuration guide
└── IMPLEMENTATION_SUMMARY.md  # Complete implementation details
```

---

<div align="center">
  
**Made with ❤️ by [astitva16-shadow](https://github.com/astitva16-shadow)**

⭐ Star this repo if you find it helpful!

### 🚀 [Try it Now!](https://github.com/astitva16-shadow/Python-Compiler)

</div>