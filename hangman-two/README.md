# Desafío CTF: `hangman-two` — Hangman Two

## 1. Introducción
Segunda versión del juego del ahorcado donde cada usuario recibe una palabra aleatoria de 25 caracteres, vinculada en la base de datos mediante una cookie llamada `state`.
- **Categoría:** Seguridad Web

## 2. Objetivo
Analizar vulnerabilidades de desvinculación entre estado de sesión y autorización (IDOR en cookies de estado) cuando el contador de intentos fallidos se almacena en el usuario pero el recurso objetivo se referencia por una cookie manipulable.

## 3. Requisitos
- Python 3 (`requests`, `beautifulsoup4`).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd hangman-two/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Capturar la cookie `state` generada para el primer usuario y reutilizarla en nuevas cuentas registradas (probando 3 letras por cuenta) para descubrir los caracteres de la misma palabra aleatoria sin perder las 4 vidas.

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
