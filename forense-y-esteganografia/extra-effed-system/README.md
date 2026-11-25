# Desafío CTF: `extra-effed-system` — Extra Effed System

## 1. Introducción
Imagen de disco comprimida (`exefs.bin.xz`) que contiene un sistema de archivos XFS con metadatos de inodos corruptos.
- **Categoría:** Forense Digital

## 2. Objetivo
Utilizar herramientas de diagnóstico forense de sistemas de archivos (`xfs_db`, `xfs_repair` y `dd`) para localizar extents de datos y reconstruir archivos fragmentados.

## 3. Requisitos
- Herramientas `xz`, `xfsprogs` (`xfs_db` / `xfs_repair`) y `dd`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/exefs.bin.xz`.

## 5. Metodología de resolución
Descomprimir `exefs.bin.xz`, consultar los bloques de datos asignados al inodo de `/flag.jpg` mediante `xfs_db -c 'path /flag.jpg' -c 'print'` y extraer los dos extents con `dd` (`bs=4k`).

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
