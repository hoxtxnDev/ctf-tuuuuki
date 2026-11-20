# Desafío CTF: `hangman-three` — Hangman Three

## 1. Introducción
Tercera versión del juego del ahorcado que almacena el contador de vidas perdidas (`life_lost`) dentro de un JSON Web Token (JWT) firmado con HS256.
- **Categoría:** Seguridad Web / Criptografía

## 2. Objetivo
Auditar la fortaleza de secretos de firma HMAC en tokens JWT y comprender cómo una clave débil de diccionario permite falsificar reclamaciones (*claims*) de estado.

## 3. Requisitos
- Python 3 (`requests`, `beautifulsoup4`, `pyjwt`) y `hashcat` (o diccionario `jwt.secrets.list`).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd hangman-three/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Extraer la cookie `access_token_cookie`, recuperar la clave secreta HMAC (`tobemodified`) mediante ataque de diccionario y firmar tokens JWT propios fijando `"life_lost": "0"` en cada intento.

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
- **Autor original:** `itsc0rg1`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
