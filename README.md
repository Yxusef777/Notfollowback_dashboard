# Instagram Safe Unfollow Dashboard (V2) 🛡️



A robust, command-line Python utility that compares your Instagram 'Followers' and 'Following' HTML data exports to identify accounts that do not follow you back. 



Built with strong OpSec principles in mind, this tool processes everything locally on your machine. It generates an interactive, styled HTML dashboard so you can safely and manually unfollow users at a human pace, completely bypassing Instagram's strict anti-bot detection systems and avoiding API action blocks.## 🚀 What's New in V2?- **Advanced HTML Parsing:** Upgraded to use `BeautifulSoup4` for highly accurate data extraction, ensuring the script remains stable even if Instagram slightly alters their export structures.- **Command-Line Interface (CLI):** Implemented `argparse` for flexible execution. You can now pass custom file names directly from your terminal.- **Zero Account Risk:** Does not use the Instagram API or browser automation (like Selenium). 100% safe from shadowbans.- **Fully Local (Privacy First):** Your personal data never leaves your machine.## 🛠️ Prerequisites- Python 3.x- `beautifulsoup4` library## 📥 Installation1. **Clone the repository:**

   ```bash

   git clone [https://github.com/Yxusef777/Notfollowback_dashboard.git](https://github.com/Yxusef777/Notfollowback_dashboard.git)

   cd Notfollowback_dashboard

Install the required dependencies:

Bash



pip install beautifulsoup4

📂 How to Get Your Instagram Data

Open Instagram -> Settings & Privacy -> Your Information and Permissions -> Download Your Information.

Request a download and select "HTML" as the format.

Once downloaded, extract the ZIP file and locate your followers and following HTML files.

💻 Usage

Place your HTML files in the same directory as the script.

Default Mode:

If your files are named exactly followers_1.html and following.html, simply run:

Bash



python dashboard.py

Advanced Mode (CLI Arguments):

You can specify custom input files and a custom output dashboard name using flags:

Bash



python dashboard.py -f my_custom_followers.html -w my_custom_following.html -o target_dashboard.html

Flags:

-f, --followers : Path to your followers HTML file (Default: followers_1.html)

-w, --following : Path to your following HTML file (Default: following.html)

-o, --output    : Name of the generated dashboard file (Default: unfollow_dashboard.html)

⚠️ Operational Safety Warning

To maintain account safety and avoid triggering Instagram's spam filters, do not unfollow hundreds of accounts in one sitting. Open the generated dashboard daily and unfollow roughly 20 to 30 accounts per day.
