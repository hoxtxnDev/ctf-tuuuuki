# Desafío CTF: `ruthless-dot-flag` — Ruthless.flag (Parte 1)

## 1. Introducción
Archivo gráfico en formato propietario `.r16` (`flags.r16`) procedente del videojuego clásico de 1998 *Tom Clancy's ruthless.com*.
- **Categoría:** Forense Digital (101)

## 2. Objetivo
Practicar ingeniería inversa de formatos binarios de imagen sin compresión (cabecera de dimensiones y píxeles RGB555 de 16 bits little-endian).

## 3. Requisitos
- Python 3, GIMP (modo Raw Image Data) o `hexdump`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/flags.r16`.

## 5. Metodología de resolución
Analizar la cabecera de 18 bytes (`0x0320` = 800 de ancho, `0x0258` = 600 de alto) y decodificar cada par de bytes little-endian como 5 bits por canal RGB (`r16_to_ppm.py`) para visualizar la imagen.

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
