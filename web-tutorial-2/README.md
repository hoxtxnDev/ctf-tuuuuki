# Desafío CTF: `web-tutorial-2` — Web Tutorial 2 (CSP Bypass)

## 1. Introducción
Segunda parte del tutorial de XSS donde la política Content-Security-Policy bloquea scripts en línea pero autoriza la carga de scripts desde cualquier subdominio `*.us-central1.run.app`.
- **Categoría:** Seguridad Web / Cloud

## 2. Objetivo
Analizar el riesgo de autorizar comodines de plataformas de nube compartidas (`*.run.app`, `*.appspot.com`) dentro de la directiva `script-src` de Content-Security-Policy.

## 3. Requisitos
- Python 3 (`requests`) o cuenta en Google Cloud Run / Cloud Functions.

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd web-tutorial-2/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Inyectar una etiqueta `<script src='...'>` apuntando a un servicio en `*.us-central1.run.app` que sirva el código JavaScript encargado de leer `/xss-two-flag` y exfiltrar su contenido.

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
