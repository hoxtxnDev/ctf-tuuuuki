# Guía de Solución — `your-browser-hates-you` (Your Browser Hates You)

## Categoría
Seguridad Web / TLS (101)

## Procedimiento de Resolución
El servidor HTTPS devuelve la flag directamente en el documento HTML (`challenge/app/index.html`) cuando se establece la conexión TLS ignorando la advertencia del certificado (`curl -k` o `HTTParty.get(PATH, verify: false)` en `solution/solve.rb`).

## Flag Esperada
```text
DUOC{omision_certificado_autofirmado_37614}
```
