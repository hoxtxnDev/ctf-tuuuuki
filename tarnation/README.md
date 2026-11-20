# Desafío CTF: `tarnation` — Tarnation

## 1. Introducción
Respaldo comprimido (`tarnation.tar.xz`) formado por múltiples archivos `.tar` concatenados que contienen tres versiones distintas de un archivo llamado `.`.
- **Categoría:** Forense Digital (101)

## 2. Objetivo
Comprender el comportamiento de los archivos tar concatenados y cómo listar y extraer ocurrencias específicas de archivos cuyo nombre colisiona con el directorio actual (`.`).

## 3. Requisitos
- Utilidad `tar` con soporte `xz` (o `binwalk`).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/tarnation.tar.xz`.

## 5. Metodología de resolución
Listar todas las entradas con `tar -Jtiv -f tarnation.tar.xz` y extraer la segunda ocurrencia del archivo `.` hacia la salida estándar con `tar -Jiv -x '.' -f tarnation.tar.xz -O --occurrence=2 > flag.jpg`.

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
