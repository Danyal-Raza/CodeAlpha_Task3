import requests

def check_auth_bypass(url):
    r = requests.get(url + '/dashboard', allow_redirects=False)
    if r.status_code == 200:
        print("[+] Authentication Bypass Detected!")
    else:
        print("[-] Authentication appears to be enforced.")

# Replace with the target URL (e.g., from DVWA or your test site)
URL = "http://127.8.0.1/dvwa"

check_auth_bypass(URL)
