# Desafío CTF: `drago-daction` — Drago-Daction

## 1. Introducción
Utilidad en C con permisos elevados que redacta la palabra 'dragon' en archivos de texto, pero presenta un desbordamiento de búfer sobre punteros de estructura.
- **Categoría:** Pwn / Binarios

## 2. Objetivo
Analizar desbordamientos de búfer basados en funciones de cadena (`strlen`/`strcpy`) que permiten redirigir el archivo de salida hacia `/proc/self/mem`.

## 3. Requisitos
- Ruby, `nasm`, `objdump` y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd drago-daction/challenge && docker build -t ctf-drago-daction . && docker run --rm -it -P ctf-drago-daction
   ```
2. Archivos distribuidos al participante: `distfiles/drago-daction`, `distfiles/drago-daction-fixed`, `distfiles/dragon-report.txt`.

## 5. Metodología de resolución
Construir una cadena de reemplazo de 128 bytes que sobrescriba el puntero de nombre de archivo de salida por `/proc/self/mem` y el desplazamiento hacia `__stack_chk_fail@plt` para ejecutar la lectura de `/flag.txt`.

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
