import re

def extract_usernames(filepath):
    usernames = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        # Find all hrefs matching standard and _u/ Instagram profiles
        matches = re.findall(r'href="https://www\.instagram\.com/(?:_u/)?([^/"]+)"', content)
        for match in matches:
            usernames.add(match)
    return usernames

# Ensure the filenames match the ones you downloaded
followers = extract_usernames('followers_1.html')
following = extract_usernames('following.html')

# Find users in 'following' that are not in 'followers'
not_following_back = following - followers

print(f"Accounts you follow: {len(following)}")
print(f"Accounts following you: {len(followers)}")
print(f"Accounts not following back: {len(not_following_back)}\n")

print("--- List of accounts not following you back ---")
for user in sorted(not_following_back):
    print(user)