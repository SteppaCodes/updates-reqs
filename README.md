# update-reqs 🚀  

**A smart CLI tool to clean and update your `requirements.txt` by fetching the latest package versions from PyPI.**  

## ✨ Features  
✅ **Remove version numbers** from `requirements.txt` (clean mode).  
✅ **Fetch and update to the latest package versions** from PyPI.  
✅ **Preserve comments and structure** in the requirements file.  
🚧 **Fast batch requests** to PyPI for improved performance (**In Progress**).  
🚧 **Dry-run mode** to preview changes before applying (**Coming Soon**).  
🚧 **Backup option** before modifying `requirements.txt` (**Coming Soon**).  

## 📦 Installation  

```sh
pip install update-reqs
```

## 🚀 Usage  

### 1. **Clean the `requirements.txt` (remove versions)**  
```sh
update-reqs clean --file requirements.txt
```

### 2. **Update to the latest package versions**  
```sh
update-reqs update --file requirements.txt
```

### 3. **Specify a different requirements file**  
```sh
update-reqs update --file path/to/your/requirements.txt
```

### 4. **View help**  
```sh
update-reqs --help
```

## 📌 Feature Checklist  
| Feature | Status |
|---------|--------|
| Remove version numbers | ✅ Done |
| Fetch latest versions | 🚧 In Progress |
| Preserve comments and formatting | 🔜 Coming Soon |
| Parallelized requests for speed | 🔜 Coming Soon |
| Dry-run mode (preview updates) | 🔜 Coming Soon |
| Backup before modifying file | 🔜 Coming Soon |

## 🚀 How It Works  
1. **Reads `requirements.txt`** and extracts package names.  
2. **Fetches the latest version** of each package from PyPI.  
3. **Updates the file** while keeping comments and spacing intact.  
4. **Writes back** the updated `requirements.txt`.  

## 🤝 Contributing  
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

### 🔥 What's Changed?
- **Feature Checklist**: Clearly marks **what's done** and **what's coming soon**.  
- **Realistic Expectations**: No false claims—just **transparency** on what’s built and what's next.  
- **"Coming Soon" Features**: Encourages contributions! 
