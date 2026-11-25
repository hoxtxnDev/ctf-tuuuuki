# Desafío CTF: `go-git-it` — Go Git It

## 1. Introducción
Sitio web estático cuyo servidor Nginx expone por error el directorio de control de versiones `/git/` con listado automático de archivos (`autoindex on`).
- **Categoría:** Seguridad Web

## 2. Objetivo
Comprender el riesgo de exponer directorios `.git` en servidores web de producción y cómo auditar el historial de commits para identificar secretos eliminados en revisiones previas.

## 3. Requisitos
- Cliente HTTP (`wget` o `curl`) y `git`.

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd go-git-it/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Inspeccionar el código fuente HTML para hallar la nota sobre `/git/`, descargar el repositorio expuesto, listar los commits con `git log --name-status` y recuperar el archivo eliminado `flag.html` con `git show`.

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
- **Autor original:** `anshc`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
