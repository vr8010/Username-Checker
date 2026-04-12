# Username Checker

A Python CLI tool to check username availability across multiple popular platforms. Perfect for OSINT (Open Source Intelligence) and cybersecurity learning.

## 🎯 Description

Username Checker is a beginner-friendly command-line tool that helps you quickly verify if a username is available or taken on various social media and development platforms. It uses multithreading for fast, parallel checking across multiple sites.

## ✨ Features

- **Multi-platform checking**: Supports GitHub, Instagram, Twitter, Reddit, and more
- **Fast execution**: Uses multithreading via ThreadPoolExecutor
- **OSINT-focused**: Useful for open source intelligence gathering
- **CLI-based**: Simple command-line interface
- **Customizable**: Easy to add more platforms via JSON configuration
- **Error handling**: Handles timeouts and connection errors gracefully

## 📋 Supported Platforms

- GitHub
- Instagram
- Twitter (X)
- Reddit
- Pinterest
- Tumblr
- Medium
- Twitch
- YouTube

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/username-checker.git
cd username-checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the tool:
```bash
python username_checker.py
```

Enter the username when prompted and wait for results.

## 📊 Example Output

```
============================================================
                    USERNAME CHECKER
============================================================

Enter username to check: johndoe

Checking availability for 'johndoe'...
Please wait...

============================================================
RESULTS:
============================================================
GitHub         : Taken        -> https://github.com/johndoe
Twitter        : Taken        -> https://twitter.com/johndoe
Instagram      : Available
Reddit         : Available
Pinterest      : Available
Medium         : Taken        -> https://medium.com/@johndoe
Tumblr         : Available
Twitch         : Available
YouTube        : Available
============================================================

Completed in 2.34 seconds

⚠️  Disclaimer: This tool is for educational purposes only.
Use responsibly and ethically.
```

## 🔧 Customization

You can add or modify platforms by editing the `sites.json` file:

```json
{
  "PlatformName": "https://platform.com/{}",
  "AnotherSite": "https://example.com/user/{}"
}
```

The `{}` placeholder will be replaced with the username.

## ⚠️ Important Notes

- Some websites may block automated requests or use anti-bot protection
- The tool includes User-Agent headers to reduce blocking
- Results may vary depending on platform rate limiting
- 404 status = Available, 200 status = Taken
- Timeouts and errors are handled gracefully

## 🛡️ Disclaimer

This tool is intended for **educational and ethical use only**. Always respect:
- Platform Terms of Service
- Privacy laws and regulations
- Ethical hacking guidelines
- Rate limiting and responsible usage

Do not use this tool for:
- Harassment or stalking
- Unauthorized access attempts
- Violating platform policies
- Any illegal activities

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

Created for cybersecurity education and OSINT learning.

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests. Suggestions for additional platforms are welcome!

## 📚 Learning Resources

This project demonstrates:
- HTTP requests in Python
- Multithreading with concurrent.futures
- JSON file handling
- Error handling and timeouts
- CLI application development
- OSINT techniques

Perfect for beginners learning Python, web scraping, or cybersecurity basics!
