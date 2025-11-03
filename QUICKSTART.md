# 🚀 Quick Start Guide

## Starting the Backend Server

### Step 1: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 2: Start the Server
```powershell
python app.py
```

You should see:
```
============================================================
🐍 Python Compiler Backend Server
============================================================
Python Version: 3.x.x
Max Execution Time: 10s
Max Memory: 128MB
============================================================

🚀 Server starting on http://localhost:5000
📝 Open http://localhost:5000 in your browser
```

### Step 3: Open in Browser
- Open `http://localhost:5000` in your browser
- The IDE will automatically detect the backend server
- You'll see: "✓ Backend server connected"

---

## 💡 Usage

### Execution Modes

Select from the dropdown in the IDE:

1. **Auto Mode** (Default)
   - Automatically uses server if available
   - Falls back to browser mode if server is offline
   
2. **Server Mode**
   - Forces server-side execution
   - Best for heavy computations
   - Requires backend running
   
3. **Browser Mode**
   - Forces browser execution (Pyodide)
   - Works offline
   - No server needed

### Running Code

1. Write Python code in the editor
2. Select execution mode (or keep Auto)
3. Click "Run Code" or press `Ctrl+Enter`
4. View output in the right panel

### Installing Packages

**Server Mode:**
- Type package name (e.g., "numpy")
- Click "Install"
- Package installs on the server

**Browser Mode:**
- Uses micropip for pure Python packages
- Limited to Pyodide-compatible packages

---

## 🎯 Examples

### Example 1: Hello World
```python
print("Hello from Python IDE!")
print("Execution mode: Server" if __name__ == "__main__" else "Browser")
```

### Example 2: Using NumPy (Server Mode)
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Mean: {arr.mean()}")
print(f"Sum: {arr.sum()}")
```

### Example 3: File I/O (Server Mode)
```python
# Write to file
with open("test.txt", "w") as f:
    f.write("Hello from server!\n")

# Read from file
with open("test.txt", "r") as f:
    content = f.read()
    print(f"File content: {content}")
```

### Example 4: Web Requests (Server Mode)
```python
import requests

response = requests.get("https://api.github.com")
print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")
```

---

## 🔍 Features

### Backend (Server Mode)
✅ Full Python 3.x support
✅ All packages available via pip
✅ File system access
✅ Network requests
✅ Better performance
✅ No memory limits (browser)
✅ Subprocess isolation

### Frontend (Browser Mode)
✅ Runs offline
✅ No server required
✅ Pure Python packages
✅ Safe sandboxed execution
✅ No installation needed

---

## ⚡ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Run code |
| `Tab` | Insert 4 spaces |
| `Enter` (in package field) | Install package |

---

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal to stop the backend server.

---

## 📊 Testing the Backend

### Method 1: Browser
Open `http://localhost:5000/api/health`

Should return:
```json
{
  "status": "healthy",
  "python_version": "3.x.x",
  "max_execution_time": 10,
  "max_memory": 134217728
}
```

### Method 2: PowerShell
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/health" -Method Get
```

### Method 3: curl
```bash
curl http://localhost:5000/api/health
```

---

## 🐛 Common Issues

### Issue: "Backend server not available"
**Solution:** Start the backend server with `python app.py`

### Issue: "Port 5000 already in use"
**Solution:** 
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process
taskkill /PID <PID> /F
```

### Issue: "Module not found"
**Solution:**
```powershell
pip install -r requirements.txt
```

---

## 🎉 You're Ready!

Your Python IDE now works as a proper compiler with:
- ✅ Backend server for real Python execution
- ✅ Browser fallback for offline use
- ✅ Package management
- ✅ Multiple execution modes
- ✅ Professional UI

**Enjoy coding!** 🐍
