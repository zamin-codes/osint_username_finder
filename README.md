# OSINT Username Finder

This project is a fast and simple **OSINT (Open Source Intelligence)** tool for checking usernames across multiple popular platforms. It is designed to help security researchers, investigators, and individuals quickly identify whether a specific username exists on various social media and community platforms.

## ✨ Features
- Asks the user for a username.
- Checks if the username exists across multiple platforms:
  - Facebook
  - Instagram
  - TikTok
  - Snapchat
  - Telegram
  - GitHub
  - YouTube
  - Chess.com
  - And more can be added easily.
- Provides direct profile links if found.
- Option to save results in a file with a custom filename.
- Uses asynchronous requests (super fast).
- Fully commented for easy understanding.

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zamin-codes/osint-username-finder.git
   cd osint-username-finder
   ```

2. Install dependencies:
   ```bash
   pip install aiohttp
   ```

3. Run the tool:
   ```bash
   python3 osint_username_finder.py
   ```

## 🛠 Usage
- Enter a username when prompted.
- The tool will search across all supported platforms.
- Choose whether to save the results in a file.

Example:
```bash
Enter the username to search: attacker123
Do you want to save results to a file? (y/n): y
Enter filename: attacker123_results.txt
```

## ⚠️ Disclaimer
This tool is built **only for educational and research purposes**. It should not be used for illegal or unethical activities. The author is not responsible for misuse of this project.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

