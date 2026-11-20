# Desafío CTF: `nearest-neighbor` — Nearest Neighbor

## 1. Introducción
Imagen de fondo de pantalla de alta resolución (`4096x3072`, `flag.webp`) que oculta una segunda imagen intercalada cada 16 píxeles en ambos ejes.
- **Categoría:** Forense Digital / Esteganografía

## 2. Objetivo
Comprender las diferencias entre algoritmos de interpolación de imágenes (bilineal, bicúbico vs. vecino más cercano) y cómo el submuestreo periódico permite ocultar información visual.

## 3. Requisitos
- ImageMagick (`magick` / `convert`) o Python con Pillow.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/flag.webp`.

## 5. Metodología de resolución
Inspeccionar la imagen con zoom para observar la rejilla de píxeles cada 16 posiciones y redimensionar `distfiles/flag.webp` a `256x192` especificando interpolación `nearest-neighbor`.

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
- **Autor original:** `symmetric`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
