# Desafío CTF: `magic` — Magic

## 1. Introducción
Archivo de imagen (`magic.png`) que los visores gráficos rechazan abrir debido a una alteración en sus primeros bytes.
- **Categoría:** Forense Digital

## 2. Objetivo
Comprender la estructura de firmas de archivo (*magic bytes*) y cómo identificar y reparar cabeceras PNG corruptas mediante análisis hexadecimal.

## 3. Requisitos
- Editor hexadecimal (`xxd`, `hexedit` o Python).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/magic.png`.

## 5. Metodología de resolución
Inspeccionar los primeros 8 bytes de `distfiles/magic.png`, observar que los primeros 4 bytes fueron reemplazados por `616e 7368` y restaurarlos al valor estándar PNG `8950 4e47`.

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
- **Autor original:** `anshc`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
