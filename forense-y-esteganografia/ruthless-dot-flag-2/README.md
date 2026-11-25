# Desafío CTF: `ruthless-dot-flag-2` — Ruthless.flag (Parte 2)

## 1. Introducción
Segunda capa oculta dentro del mismo archivo `flags.r16` del desafío `ruthless-dot-flag`.
- **Categoría:** Forense Digital / Esteganografía

## 2. Objetivo
Identificar canales de datos ignorados por el renderizador (el bit de transparencia alfa en píxeles de 16 bits ARGB1555 cuando la cabecera desactiva el canal alfa) para extraer archivos incrustados bit a bit.

## 3. Requisitos
- Python 3 (`struct`).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Extraer el bit más significativo (`(rgba & 0x8000) >> 15`) de cada uno de los $800 \times 600$ píxeles de `flags.r16` utilizando `r16_extract_hidden_data.py` y empaquetar los bits en bytes para obtener la imagen con la segunda flag.

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
