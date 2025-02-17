import requests
import argparse

def push_clipboard(server_url, text):
    try:
        response = requests.post(f"{server_url}/post", json={"text": text}, timeout=5)
        if response.status_code == 200:
            print("Clipboard updated on server!")
        else:
            print("Failed to update clipboard:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_clipboard(server_url):
    try:
        response = requests.get(f"{server_url}/get", timeout=5)
        if response.status_code == 200:
            clipboard_text = response.json().get("text", "")
            print(f"Clipboard content: {clipboard_text}")
        else:
            print("Failed to fetch clipboard:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple clipboard sync client.")
    parser.add_argument("ip", help="Server IP address (e.g., 192.168.1.100)")
    parser.add_argument("action", choices=["push", "get"], help="Action to perform")
    parser.add_argument("-t", "--text", help="Text to push (only required for 'push')")

    args = parser.parse_args()
    server_url = f"http://{args.ip}:5000"

    if args.action == "push":
        if not args.text:
            print("Error: You must provide text to push.")
        else:
            push_clipboard(server_url, args.text)
    elif args.action == "get":
        get_clipboard(server_url)
