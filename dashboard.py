import argparse
import webbrowser
import os
from bs4 import BeautifulSoup

def extract_usernames(filepath):
    usernames = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # BeautifulSoup parses the HTML structure perfectly
            soup = BeautifulSoup(file, 'html.parser')
            
            # Find all anchor tags (links)
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if 'instagram.com' in href:
                    # Extract the username from the end of the URL safely
                    username = href.strip('/').split('/')[-1]
                    usernames.add(username)
                    
    except FileNotFoundError:
        print(f"[!] Error: Could not find '{filepath}'. Please check the file path.")
    except Exception as e:
        print(f"[!] An error occurred while parsing {filepath}: {e}")
        
    return usernames

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Generate a safe Instagram unfollow dashboard from HTML exports.")
    parser.add_argument('-f', '--followers', default='followers_1.html', help="Path to your followers HTML file")
    parser.add_argument('-w', '--following', default='following.html', help="Path to your following HTML file")
    parser.add_argument('-o', '--output', default='unfollow_dashboard.html', help="Name of the output HTML file")
    
    args = parser.parse_args()

    print("[*] Initializing Safe Unfollow Dashboard Generator...")
    print(f"[*] Reading followers from: {args.followers}")
    print(f"[*] Reading following from: {args.following}")

    followers = extract_usernames(args.followers)
    following = extract_usernames(args.following)

    if not followers or not following:
        print("[!] Missing data. Exiting...")
        return

    # Find people you follow who don't follow back
    not_following_back = sorted(list(following - followers))

    # Generate the HTML dashboard
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Unfollow Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }}
            .container {{ max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; }}
            .stats {{ color: #555; font-size: 14px; margin-bottom: 20px; }}
            .user-link {{ display: block; padding: 10px; margin: 5px 0; background: #eee; text-decoration: none; color: #d93025; font-weight: bold; border-radius: 4px; transition: 0.2s; }}
            .user-link:hover {{ background: #ddd; transform: translateX(5px); }}
            .warning {{ color: #856404; background-color: #fff3cd; padding: 10px; border-radius: 4px; border: 1px solid #ffeeba; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Accounts Not Following You Back</h1>
            <div class="stats">
                You follow: <strong>{len(following)}</strong> | Following you: <strong>{len(followers)}</strong> | Traitors: <strong>{len(not_following_back)}</strong>
            </div>
            <div class="warning">
                <strong>Safety Tip:</strong> Only click and unfollow about 20-30 accounts per day to avoid triggering Instagram's spam filters.
            </div>
    """

    for user in not_following_back:
        html_content += f'<a class="user-link" href="https://www.instagram.com/{user}" target="_blank">@{user}</a>\n'

    html_content += """
        </div>
    </body>
    </html>
    """

    with open(args.output, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"[+] Success! Dashboard created with {len(not_following_back)} accounts.")
    print(f"[*] Opening {args.output} in your browser...")
    
    webbrowser.open('file://' + os.path.realpath(args.output))

if __name__ == "__main__":
    main()