# Desafío CTF: `block-cipher` — Block Cipher

## 1. Introducción
Servicio web de codificación visual que transforma bloques de tres letras en imágenes compuestas por sub-bloques geométricos y rotaciones según una clave numérica.
- **Categoría:** Criptografía

## 2. Objetivo
Analizar esquemas de codificación en base mixta y criptoanálisis por texto plano elegido (CPA) mediante inspección de patrones visuales.

## 3. Requisitos
- Python 3, navegador web o cliente HTTP.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd block-cipher/challenge && docker build -t ctf-block-cipher . && docker run --rm -it -P ctf-block-cipher
   ```
2. Archivos distribuidos al participante: `distfiles/flag.png`.

## 5. Metodología de resolución
Enviar entradas de prueba al codificador para identificar la secuencia de símbolos (bases 5, 5 y 7) y las rotaciones (bases 4, 4, 2 y 4), deducir la permutación de la clave y decodificar los bloques de `distfiles/flag.png`.

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
