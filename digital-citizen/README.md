# Desafío CTF: `digital-citizen` — Digital Citizen 1

## 1. Introducción
Servicio de registro de claves públicas RSA que emula un defecto real de generación de números primos con patrones repetitivos de bits en tarjetas inteligentes.
- **Categoría:** Criptografía

## 2. Objetivo
Aplicar técnicas de factorización por máximo común divisor por lotes (*Batch GCD*) y análisis de patrones binarios para auditar generadores de números aleatorios defectuosos.

## 3. Requisitos
- Python 3 (`sympy`) y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd digital-citizen/challenge && docker build -t ctf-digital-citizen . && docker run --rm -it -P ctf-digital-citizen
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Recolectar módulos RSA generados con la opción de hardware RNG, calcular el MCD entre pares con `gcd_mods.py`, deducir la estructura periódica de bits y factorizar la clave del Ciudadano 0 con `generate_all_pattern_primes.py` y `trial_division.py`.

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
