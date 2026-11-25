# Desafío CTF: `cipher-block-corruption` — Cipher Block Corruption

## 1. Introducción
Imagen PNG cifrada mediante AES-128 en modo CBC utilizando una clave conocida pero un vector de inicialización (IV) aleatorio no registrado.
- **Categoría:** Criptografía

## 2. Objetivo
Comprender la propiedad de propagación limitada de errores en el descifrado AES-CBC y cómo restaurar el primer bloque a partir de cabeceras de formato conocidas.

## 3. Requisitos
- Python 3 con `pycryptodome`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/enc_cbc.py`, `distfiles/flag.png.enc`.

## 5. Metodología de resolución
Descifrar el archivo `distfiles/flag.png.enc` en modo AES-CBC con un IV nulo y reemplazar los primeros 16 bytes corruptos por los 16 bytes estándar de la cabecera PNG (`\x89PNG...IHDR`).

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
