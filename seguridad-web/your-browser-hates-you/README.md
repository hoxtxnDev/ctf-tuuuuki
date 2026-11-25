# Desafío CTF: `your-browser-hates-you` — Your Browser Hates You

## 1. Introducción
Servidor HTTPS en el puerto 443 configurado intencionalmente con un certificado TLS autofirmado/inválido que los navegadores modernos bloquean de forma estricta.
- **Categoría:** Seguridad Web / TLS (101)

## 2. Objetivo
Comprender cómo funcionan las validaciones de cadena de confianza de certificados X.509/TLS y cómo inspeccionar servicios HTTPS de laboratorio mediante herramientas de línea de comandos (`curl -k`).

## 3. Requisitos
- `curl`, `openssl s_client` o Ruby (`httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd your-browser-hates-you/challenge && docker build -t ctf-your-browser-hates-you . && docker run --rm -it -P ctf-your-browser-hates-you
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Realizar una petición HTTPS omitiendo la verificación de autoridad certificadora (`curl -k https://<host>:443/`) para inspeccionar el código HTML devuelto por el servidor.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `1000` puntos (configurado en `metadata.yml`).
- El desafío otorga el puntaje al validar la cadena de respuesta exacta en la plataforma del CTF.

## 7. Formato de flags
La flag de este desafío sigue el estándar institucional del laboratorio:
```text
DUOC{palabra_clave_XXXXX}
```

## 8. Consideraciones de seguridad
- Este ejercicio debe ejecutarse exclusivamente dentro del entorno de laboratorio aislado o sobre los archivos provistos en `distfiles/`.
- No utilices las técnicas estudiadas fuera de entornos educativos expresamente autorizados.

## 9. Créditos y referencias
- **Autor original:** `ron`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
