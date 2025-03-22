# update-reqs 

**A smart CLI tool to automatically update `requirements.txt` by fetching the latest versions of outdated libraries from PyPI.**  

Still a work in progress
## ✨ Features  
- **Remove version numbers** from `requirements.txt` (clean mode).  
- **Fetch and update to the latest versions** from PyPI.  
- **Preserve comments and structure** in the requirements file.  
- **Fast batch requests** to PyPI for improved performance.  

## 📦 Installation  

```sh
pip install update-reqs
```

## 🚀 Usage  

### 1️⃣ **Clean the `requirements.txt` (remove versions)**  
```sh
update-reqs clean --file requirements.txt
```

### 2️⃣ **Update to the latest package versions**  
```sh
update-reqs update --file requirements.txt
```

### 3️⃣ **Specify a different requirements file**  
```sh
update-reqs update --file path/to/your/requirements.txt
```

### 4️⃣ **View help**  
```sh
update-reqs --help
```

## ⚙️ How It Works  
1. **Reads `requirements.txt`** and extracts package names.  
2. **Fetches the latest version** of each package from PyPI.  
3. **Updates the file** while keeping comments and spacing intact.  
4. **Writes back** the updated `requirements.txt`.  

## 🚀 Roadmap  
- [ ] Parallelized requests for **faster updates**.  
- [ ] Support for **version pinning (>=, <=, ~, etc.)**.  
- [ ] Dry-run mode to **preview changes before applying**.  
- [ ] Backup option before modifying `requirements.txt`.  

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

---
🔹 Made with ❤️ by ## The API Artist for Python developers! Happy coding!
```
