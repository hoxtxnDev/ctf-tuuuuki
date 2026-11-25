import requests
import re

CTFD_URL = "http://192.168.100.121"
USERNAME = "lalalisa"
PASSWORD = "lalalisa"

CARPETA = "criptografia/subprime"
NOMBRE = "Subprime"
CATEGORIA = "Crypto"
DESCRIPCION = "Factoriza la clave RSA para recuperar la flag."
FLAG = "DUOC{exponente_privado_factorizado_51739}"
ARCHIVOS = [f"{CARPETA}/distfiles/cipher.txt", f"{CARPETA}/distfiles/pubkeypair.txt"]
VALOR = 100

s = requests.Session()
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Linux; Android 16; Pixel 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Mobile Safari/537.36",
    "Origin": CTFD_URL,
    "X-Requested-With": "XMLHttpRequest",
})

r = s.get(f"{CTFD_URL}/login")
m = re.search(r'<input[^>]*name="nonce"[^>]*value="([^"]+)"', r.text)
nonce = m.group(1)
s.post(f"{CTFD_URL}/login", data={"name": USERNAME, "password": PASSWORD, "nonce": nonce})

r2 = s.get(f"{CTFD_URL}/admin/challenges")
csrf = re.search(r"'csrfNonce':\s*\"([^\"]+)\"", r2.text).group(1)

headers = {"CSRF-Token": csrf}

payload = {
    "name": NOMBRE,
    "category": CATEGORIA,
    "description": DESCRIPCION,
    "value": VALOR,
    "state": "hidden",
    "type": "standard",
}
r = s.post(f"{CTFD_URL}/api/v1/challenges", json=payload, headers=headers)
print("crear challenge:", r.status_code, r.text)
chall_id = r.json()["data"]["id"]

flag_payload = {"challenge_id": chall_id, "content": FLAG, "type": "static"}
r = s.post(f"{CTFD_URL}/api/v1/flags", json=flag_payload, headers=headers)
print("crear flag:", r.status_code, r.text)

headers_files = {"Referer": f"{CTFD_URL}/admin/challenges/{chall_id}"}
for ruta in ARCHIVOS:
    with open(ruta, "rb") as f:
        files = {"file": f}
        data = {"challenge": str(chall_id), "type": "challenge", "nonce": csrf}
        r = s.post(f"{CTFD_URL}/api/v1/files", files=files, data=data, headers=headers_files)
        print(ruta, r.status_code, r.text)

print(f"\nListo. Challenge creado con id={chall_id}")
