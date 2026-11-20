# Desafío CTF: `meow` — Meow

## 1. Introducción
Desafío introductorio de conexión a una consola remota Linux donde la flag se encuentra almacenada en el directorio personal del usuario.
- **Categoría:** Terminal / Introductorio (101)

## 2. Objetivo
Familiarizarse con la conexión a servicios de terminal interactiva en un CTF y el uso de comandos básicos de lectura de archivos en Unix/Linux (`ls`, `cat`).

## 3. Requisitos
- Cliente TCP (`netcat` / `nc`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd meow/challenge && docker build -t ctf-meow . && docker run --rm -it -P ctf-meow
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Conectarse al puerto TCP 4445 del desafío, listar los archivos del directorio `/home/ctf` con `ls` y mostrar el contenido de `/home/ctf/flag.txt` mediante el comando `cat` (en alusión al nombre del reto, *meow*).

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
- **Autor original:** `Daniel Pendolino`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
