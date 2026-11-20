# Desafío CTF: `soothsayer` — Soothsayer

## 1. Introducción
Aplicación Android conectada a Firebase Firestore y un servidor Python donde el jugador debe acertar 30 predicciones binarias consecutivas generadas mediante Mersenne Twister.
- **Categoría:** Seguridad Móvil (Android) / Criptografía

## 2. Objetivo
Analizar vulnerabilidades de control de acceso y exposición de estado cuando la semilla del generador pseudoaleatorio (PRNG) y el puntaje se almacenan en documentos de Firestore accesibles o manipulables desde el cliente mediante Frida.

## 3. Requisitos
- Python 3 (`numpy`, `requests`, `firebase-admin`) o emulador Android con `adb` y `frida`.

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd soothsayer/challenge && docker compose up --build
   ```
2. Archivos distribuidos al participante: `distfiles/soothsayer.apk`.

## 5. Metodología de resolución
Instrumentar la aplicación Android con Frida (`solver.js`) o consultar la semilla almacenada en el documento del usuario en Firestore para precalcular las 30 elecciones de `numpy.random` y solicitar `/get-flag`.

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
- **Autor original:** `itsc0rg1`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
