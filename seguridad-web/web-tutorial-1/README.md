# Desafío CTF: `web-tutorial-1` — Web Tutorial 1 (XSS)

## 1. Introducción
Aplicación web educativa con un bot administrador que revisa las cargas útiles enviadas y una política CSP permisiva que acepta scripts en línea.
- **Categoría:** Seguridad Web (101)

## 2. Objetivo
Comprender el funcionamiento de Cross-Site Scripting (XSS) cuando la cabecera Content-Security-Policy incluye `'unsafe-inline'` y cómo proteger endpoints sensibles y cookies de sesión.

## 3. Requisitos
- Navegador web, endpoint receptor HTTP (webhook/requestbin) o Python 3 (`requests`).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd web-tutorial-1/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Enviar una etiqueta `<script>` que realice una petición `XMLHttpRequest` interna a `/xss-one-flag` desde el contexto del navegador del administrador y reenvíe la respuesta a un receptor externo.

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
