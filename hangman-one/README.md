# Desafío CTF: `hangman-one` — Hangman One

## 1. Introducción
Juego web del ahorcado en Flask donde todos los usuarios comparten la misma palabra objetivo estática, pero cada cuenta dispone únicamente de 4 vidas.
- **Categoría:** Seguridad Web

## 2. Objetivo
Identificar fallas de lógica de negocio cuando un secreto compartido carece de límite global de intentos entre distintas cuentas de usuario.

## 3. Requisitos
- Python 3 (`requests`, `beautifulsoup4`).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd hangman-one/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Registrar múltiples cuentas de usuario sucesivas para probar distintos subconjuntos del alfabeto alfanumérico sin que el límite de 4 errores por usuario impida descubrir las letras que componen la palabra.

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
