# update-reqs 🚀  

**A smart CLI tool to clean and update your `requirements.txt` by fetching the latest package versions from PyPI.**  

## ✨ Features  
✅ **Remove version numbers** from `requirements.txt` (clean mode).  
🚧 **Fetch and update to the latest package versions** from PyPI.  
🔜 **Preserve comments and structure** in the requirements file.  
🔜 **Fast batch requests** to PyPI for improved performance (**In Progress**).  
🔜 **Dry-run mode** to preview changes before applying (**Coming Soon**).  
🔜 **Backup option** before modifying `requirements.txt` (**Coming Soon**).  

## 📦 Installation  

```sh
pip install update-reqs
```

## 🚀 Usage  

### **Basic Commands**  

| Command | Description |
|---------|-------------|
| `update-reqs clean --file requirements.txt` | Removes all version numbers from the file. |
| `update-reqs update --file requirements.txt` | Updates all packages to the latest versions. |
| `update-reqs update --file path/to/requirements.txt` | Updates a specific requirements file. |
| `update-reqs --help` | Displays help and usage information. |

## 📌 Feature Checklist  
| Feature | Status |
|---------|--------|
| Remove version numbers | ✅ Done |
| Fetch latest versions | 🚧 In Progress |
| Preserve comments and formatting | 🔜 Coming Soon |
| Parallelized requests for speed | 🔜 Coming Soon |
| Dry-run mode (preview updates) | 🔜 Coming Soon |
| Backup before modifying file | 🔜 Coming Soon |

## 🔥 How It Works  
1. **Reads `requirements.txt`** and extracts package names.  
2. **Fetches the latest version** of each package from PyPI.  
3. **Updates the file** while keeping comments and spacing intact.  
4. **Writes back** the updated `requirements.txt`.  

## 🤝 Contributing  
Want to help improve `update-reqs`? Follow these steps:  

1. **Fork the repo**.  
2. **Clone your fork**:  
   ```sh
   git clone https://github.com/your-username/update-reqs.git
   cd update-reqs
   ```  
3. **Install dependencies**:  
   ```sh
   pip install -r requirements.txt
   ```  
4. **Create a new branch**:  
   ```sh
   git checkout -b feature-name
   ```  
5. **Submit a Pull Request!** 🚀  

## 📜 License  
This project is licensed under the MIT License.  

🔹 Made with ❤️ for Python developers! Happy coding!  
```
