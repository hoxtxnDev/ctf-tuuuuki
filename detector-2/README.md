# Desafío CTF: `detector-2` — Dragon Detector 2

## 1. Introducción
Segunda versión de la herramienta web de diagnóstico que incorpora una lista negra parcial de caracteres en el servidor PHP.
- **Categoría:** Seguridad Web / Pwn

## 2. Objetivo
Analizar las limitaciones de las listas negras de caracteres (*blacklisting*) frente a mecanismos de sustitución de subshell y por qué debe usarse `escapeshellarg()` o APIs nativas.

## 3. Requisitos
- Cliente HTTP (`curl`, navegador o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd detector-2/challenge && docker build -t ctf-detector-2 . && docker run --rm -it -P ctf-detector-2
   ```
2. Archivos distribuidos al participante: `distfiles/detect-dragon.php`, `distfiles/index.php`.

## 5. Metodología de resolución
Revisar `distfiles/detect-dragon.php` para identificar qué metacaracteres fueron bloqueados (como `;`, `&`, `|`) y cuáles permanecen permitidos (como la sustitución `$(...)`) para leer `/app/dragon-detector-ai`.

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
