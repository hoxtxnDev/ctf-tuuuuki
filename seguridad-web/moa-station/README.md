# Desafío CTF: `moa-station` — MoA Station

## 1. Introducción
Servicio de revisión automatizada de visas que visita la URL enviada utilizando un navegador Chromium con una extensión personalizada instalada.
- **Categoría:** Seguridad Web / Extensiones de Navegador

## 2. Objetivo
Analizar la superficie de ataque de las extensiones de navegador (`content_scripts` y `background.js`), la inyección de eventos DOM simulados y el abuso de endpoints JSONP permitidos por la CSP de la extensión.

## 3. Requisitos
- Servidor HTTP público o local accesible por el bot y cliente HTTP (`curl`).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd moa-station/challenge && docker compose up --build
   ```
2. Archivos distribuidos al participante: `distfiles/extension.zip`.

## 5. Metodología de resolución
Examinar el código de la extensión en `distfiles/`, identificar la secuencia de teclas que activa el modo de depuración en el script de contenido, despachar eventos `KeyboardEvent` sintéticos desde una página HTML controlada e inyectar un callback JSONP permitido por la política de seguridad para leer `localStorage.getItem('secret')`.

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
- **Autor original:** `mandatory`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
