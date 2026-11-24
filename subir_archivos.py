import requests, re, glob

CTFD_URL = "http://192.168.100.121"
USUARIO = "lalalisa"
CONTRASENA = "lalalisa"
CHALL_ID = 2
CARPETA = "subprime"

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"})
r = s.get(f"{CTFD_URL}/login")
nonce = (re.search(r'name="nonce"[^>]*value="([^"]+)"', r.text) or
          re.search(r'value="([^"]+)"[^>]*name="nonce"', r.text)).group(1)
s.post(f"{CTFD_URL}/login", data={"name": USUARIO, "password": CONTRASENA, "nonce": nonce})

r = s.get(f"{CTFD_URL}/admin/challenges")
csrf = re.search(r"csrfNonce['\"]?\s*:\s*['\"](.+?)['\"]", r.text).group(1)
HEADERS = {"CSRF-Token": csrf, "Referer": f"{CTFD_URL}/admin/challenges"}

for archivo in glob.glob(f"{CARPETA}/distfiles/*"):
    with open(archivo, "rb") as f:
        r = s.post(f"{CTFD_URL}/api/v1/files?nonce={csrf}", headers=HEADERS,
            data={"challenge_id": CHALL_ID, "type": "challenge"}, files={"file": f})
        print("archivo:", archivo, r.status_code, r.text[:200])
