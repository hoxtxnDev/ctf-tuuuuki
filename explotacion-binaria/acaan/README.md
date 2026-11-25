# Desafío CTF: `acaan` — ACAAN (Any Code At Any Offset)

## 1. Introducción
Servicio de red en C que permite abrir cualquier archivo accesible por el proceso y sobrescribir bytes en un desplazamiento arbitrario.
- **Categoría:** Pwn / Binarios

## 2. Objetivo
Comprender cómo funciona el sistema de archivos virtual `/proc/self/mem` en Linux y cómo una escritura arbitraria sobre descriptores de archivo permite modificar páginas de código ejecutable en memoria.

## 3. Requisitos
- Cliente TCP (`netcat`), Ruby (`socket`), `objdump` y `nasm` (o Docker para ejecutar el contenedor).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd acaan/challenge && docker build -t ctf-acaan . && docker run --rm -it -P ctf-acaan
   ```
2. Archivos distribuidos al participante: `distfiles/Dockerfile`, `distfiles/Makefile`, `distfiles/acaan`, `distfiles/acaan.c`.

## 5. Metodología de resolución
Analizar el binario desensamblado para localizar la llamada a `close@plt`, calcular el desplazamiento de la instrucción siguiente e indicar `/proc/self/mem` como archivo destino para escribir código de lectura de `/flag.txt`.

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
- **Autor original:** `ron`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
