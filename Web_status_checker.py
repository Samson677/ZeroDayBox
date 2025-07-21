import requests
import sys
import os

input_file = sys.argv[1]

def web_status_checker():
    count = 0
    with open(input_file, "r") as in_file:
        for line in in_file:
            url = line.strip()
            count += 1
            print(f"[Scanning: {line} :> {count}")
            try:
                resp = requests.get(url, timeout=5)
                with open("WebStatus.txt", "a") as f:
                    if resp.status_code == 404:
                        f.write(f"Page not found for: {url}\n")
                        os.system("clear")
                    elif resp.status_code == 500:
                        f.write(f"Server error for: {url}\n")
                        os.system("clear")
                    elif resp.status_code == 200:
                        f.write(f"This site is online: {url}\n")
                        os.system("clear")
                    else:
                        f.write(f"{url} returned status: {resp.status_code}\n")
                        os.system("clear")
            except requests.RequestException as e:
                with open("Error.txt", "a") as f:
                    f.write(f"Failed to reach {url}: {e}\n")
                    os.system("clear")


web_status_checker()
print("[Done:] ✅ Check 'WebStatus.txt'")

