import pyfiglet
import aiohttp
import asyncio
import socket
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# List of platforms with username URL patterns
PLATFORMS = {
    "Facebook": "https://www.facebook.com/{username}",
    "Instagram": "https://www.instagram.com/{username}",
    "Twitter": "https://x.com/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Telegram": "https://t.me/{username}",
    "GitHub": "https://github.com/{username}",
    "GitLab": "https://gitlab.com/{username}",
    "YouTube": "https://www.youtube.com/{username}",
    "Reddit": "https://www.reddit.com/user/{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Medium": "https://medium.com/@{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "SoundCloud": "https://soundcloud.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "Flickr": "https://www.flickr.com/people/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "Behance": "https://www.behance.net/{username}",
    "Chess": "https://www.chess.com/member/{username}"
}

# Rotating user-agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15A5341f Safari/604.1"
]

# Generate username variations
def generate_variations(username):
    return [
        username,
        username + "123",
        "real" + username,
        username + "_official",
        username + "01",
        "the" + username,
        username + "_"
    ]

# Check internet connection
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

# Check a single username on a single platform
async def check_username(session, platform, variation):
    url = PLATFORMS[platform].format(username=variation)
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            if response.status == 200:
                print(Fore.GREEN + f"[FOUND] {platform}: {url}")
                return f"FOUND: {platform}: {url}"
            else:
                print(Fore.RED + f"[NOT FOUND] {platform}: {variation}")
    except Exception as e:
        print(Fore.MAGENTA + f"[ERROR] {platform} ({variation}): {e}")
    return None

# Main async function with concurrency
async def search_usernames(username, save_file=None):
    results = []
    variations = generate_variations(username)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for variation in variations:
            for platform in PLATFORMS.keys():
                tasks.append(check_username(session, platform, variation))

        responses = await asyncio.gather(*tasks)
        results = [r for r in responses if r]

    # Save results if requested
    if save_file:
        with open(save_file, "w", encoding="utf-8") as f:
            for line in results:
                f.write(line + "\n")
        print(Fore.CYAN + f"\n[+] Results saved to {save_file}")

# Entry point
def main():
    if not check_internet():
        print(Fore.RED + "[!] No internet connection. Please check your network and try again.")
        return
    print(pyfiglet.figlet_format("Zamin Ali"))
    username = input("Enter the username to search: ").strip()
    save_choice = input("Do you want to save the results to a file? (y/n): ").strip().lower()
    save_file = None
    if save_choice == 'y':
        save_file = input("Enter the filename to save results: ").strip()

    asyncio.run(search_usernames(username, save_file))

if __name__ == "__main__":
    main()
