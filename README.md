# 🔍 Username Checker

A simple Node.js tool to check the availability of GitHub usernames in bulk.

> ⚠️ This project is currently a **proof of concept** and may not be fully optimized or production-ready.

---

## 📌 Features

* ✅ Bulk username checking
* 📂 Load usernames from a file
* 🌐 Proxy support (optional)
* ⚡ Fast and lightweight
* 🛠 Easy to customize

---

## 📁 Project Structure
```
Username-Checker/
│── checker.js        # Main script
│── config.json       # Configuration settings
│── usernames.txt     # List of usernames to check
│── proxies.txt       # Proxy list (optional)
│── package.json      # Dependencies
│── install.bat       # Install dependencies (Windows)
│── checker.bat       # Run script (Windows)
```

---

## 🚀 Installation

### 1. Clone the repository

```
git clone https://github.com/vr8010/Username-Checker.git
cd Username-Checker
```

### 2. Install dependencies

```
npm install
```

Or use:

```
install.bat
```

---

## ▶️ Usage

1. Add usernames to:

```
usernames.txt
```

2. (Optional) Add proxies to:

```
proxies.txt
```

3. Run the checker:

```
node checker.js
```

Or:

```
checker.bat
```

---

## ⚙️ Configuration

Edit `config.json` to customize behavior:

* Timeout settings
* Request delays
* Proxy usage
* Other options (depending on implementation)

---

## 📊 Output

The script will:

* Check each username
* Display availability status in the console

---

## ⚠️ Disclaimer

* This tool is for **educational purposes only**
* Excessive requests may lead to **rate limiting or temporary blocks**
* Use proxies responsibly

---

## 🛠 Future Improvements

* Add CLI interface
* Improve speed and efficiency
* Better error handling
* Save available usernames automatically
* Add logging system

---

## 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
