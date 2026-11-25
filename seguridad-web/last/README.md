# Desafío CTF: `last` — NextPM

## 1. Introducción
Gestor de contraseñas desarrollado en Next.js que protege sus rutas de API (`/api/users`, `/api/keybag/[user]`) mediante un middleware de autenticación y cifra los cofres de claves con Argon2id y NaCl SecretBox.
- **Categoría:** Seguridad Web / Criptografía

## 2. Objetivo
Comprender la vulnerabilidad de evasión de middleware en Next.js (CVE-2025-29927) mediante la cabecera `X-Middleware-Subrequest` y auditar el almacenamiento de hashes bcrypt débiles que protegen bóvedas cifradas.

## 3. Requisitos
- Python 3 (`requests`, `bcrypt`, `pynacl`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd last/challenge && docker build -t ctf-last . && docker run --rm -it -P ctf-last
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Enviar la cabecera `X-Middleware-Subrequest: middleware:middleware:middleware:middleware:middleware` a `/api/users` para omitir la verificación de sesión, obtener el hash bcrypt del usuario `bingo`, recuperar su contraseña (`banditthedog`), descargar `/api/keybag/bingo` y descifrar la bóveda con libsodium/PyNaCl.

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
- **Autor original:** `matir`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
