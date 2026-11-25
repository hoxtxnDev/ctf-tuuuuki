# Desafío CTF: `matryoshkafs` — MatryoshkaFS

## 1. Introducción
Archivo comprimido (`fs.xz`) que contiene 16 imágenes de sistemas de archivos históricos y modernos anidados uno dentro de otro como una muñeca rusa.
- **Categoría:** Forense Digital

## 2. Objetivo
Identificar, montar y extraer datos de múltiples sistemas de archivos y tablas de particiones heterogéneas (ReiserFS, Amiga AFFS, CramFS, HFS, GPT/Minix, SquashFS, HPFS, ISO9660, UDF, SGI/F2FS, Sun/NILFS2, exFAT, NTFS, JFS, Btrfs y XFS con sectores de 8 KB).

## 3. Requisitos
- Entorno Linux con utilidades de montaje loop (`losetup`, `mount`, `xfs_db`, `mmls`, `xzcat`).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/fs.xz`.

## 5. Metodología de resolución
Inspeccionar cada capa con `file` y `mmls`, descomprimir o montar en bucle cada sistema de archivos sucesivo (y extraer con `xfs_db`/`dd` en la capa XFS de sectores de 8192 bytes) hasta recuperar `flag.heic` en la última capa.

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
