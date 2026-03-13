
```markdown
# 🕵️‍♂️ Not Follow Back Dashboard

A lightweight, privacy-focused Python tool that analyzes your social media connections to find out who isn't following you back. 

Unlike many third-party apps, this tool operates **100% locally**. It does not require your username, password, or any API keys, ensuring your account remains secure and your data stays private.

## ✨ Features
* **Zero Credential Risk:** Analyzes raw HTML data exported directly from your account.
* **Robust Parsing:** Built with `BeautifulSoup4` for accurate and fast HTML extraction.
* **Modular Design:** Clean separation between the follower-checking logic and the dashboard presentation.

## 🛠️ Prerequisites
Make sure you have Python 3.x installed on your machine.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Yxusef777/Notfollowback_dashboard.git](https://github.com/Yxusef777/Notfollowback_dashboard.git)
   cd Notfollowback_dashboard

```

2. **Install the required dependencies:**
```bash
pip install -r requirements.txt

```



## 📊 How to Use

1. Request and download your account data (specifically the followers and following lists in HTML format) from your social media settings.
2. Place the downloaded files (`followers_1.html` and `following.html`) directly into the root folder of this project.
3. Run the analyzer:
```bash
python check_followers.py

```


4. Launch the dashboard to view your results:
```bash
python dashboard.py

```
