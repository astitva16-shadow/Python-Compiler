# 🐍 Python IDE - Browser Edition

A modern, fully-functional Python IDE that runs entirely in your browser using WebAssembly (Pyodide). No server required!

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
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

### 🚀 Execution & Output
- **Real-time Execution** - Run Python code instantly
- **Execution Timer** - Track how long your code takes to run
- **Color-coded Output** - Success (green), errors (red), info (blue)
- **Output Management** - Clear, copy, and download output
- **Error Handling** - Clear error messages with stack traces

### 📦 Package Management
- **Install Packages** - Use micropip to install pure Python packages
- **Popular Libraries** - NumPy, Matplotlib, Pandas, and more
- **One-click Install** - Simple package installation interface

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

### Option 1: Open Directly in Browser
Simply open `index.html` in any modern browser (Chrome, Firefox, Edge, Safari).

### Option 2: Local Server (Recommended)
For best performance, serve the file over HTTP:

```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js
npx http-server

# Using PHP
php -S localhost:8000
```

Then navigate to `http://localhost:8000`

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
- **Pyodide** - Python runtime in WebAssembly
- **HTML5/CSS3** - Modern web standards
- **Vanilla JavaScript** - No framework dependencies
- **Google Fonts** - Inter & JetBrains Mono

### Browser Compatibility
- ✅ Chrome 90+
- ✅ Firefox 90+
- ✅ Edge 90+
- ✅ Safari 14+

### Performance
- **Initial Load** - ~5-10 seconds (Pyodide download)
- **Code Execution** - Near-native Python speed
- **Package Installation** - Varies by package size

## 📦 Supported Packages

Pyodide supports many pure Python packages. Popular ones include:

- **NumPy** - Numerical computing
- **Pandas** - Data analysis
- **Matplotlib** - Data visualization
- **SciPy** - Scientific computing
- **SymPy** - Symbolic mathematics
- **Pillow** - Image processing
- **Beautiful Soup** - Web scraping
- **Requests** - HTTP library

[Full list of packages](https://pyodide.org/en/stable/usage/packages-in-pyodide.html)

## ⚠️ Limitations

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

- 🐛 [Report a Bug](https://github.com/astitva16-shadow/E-Commerce/issues)
- 💡 [Request a Feature](https://github.com/astitva16-shadow/E-Commerce/issues)
- 📧 Contact: astitva16-shadow@users.noreply.github.com

## 🔗 Links

- **Repository**: [github.com/astitva16-shadow/E-Commerce](https://github.com/astitva16-shadow/E-Commerce)
- **Pyodide Docs**: [pyodide.org](https://pyodide.org/)
- **Python Docs**: [docs.python.org](https://docs.python.org/)

---

<div align="center">
  
**Made with ❤️ by [astitva16-shadow](https://github.com/astitva16-shadow)**

⭐ Star this repo if you find it helpful!

</div>