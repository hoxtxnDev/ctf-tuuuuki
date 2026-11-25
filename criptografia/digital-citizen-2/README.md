# Desafío CTF: `digital-citizen-2` — Digital Citizen 2

## 1. Introducción
Segunda parte del desafío `digital-citizen` (utiliza el mismo servicio en el puerto 6537), enfocada en la clave del Ciudadano 1 cuyos primos contienen 48 bits aleatorios adicionales.
- **Categoría:** Criptografía

## 2. Objetivo
Comprender y aplicar el método de raíces pequeñas de Coppersmith (`small_roots`) en SageMath para factorizar módulos RSA cuando se conocen las partes altas del factor primo.

## 3. Requisitos
- SageMath, Python 3 y `netcat`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Utilizar la lista de primos candidatos generados por patrón como aproximación de los bits superiores y ejecutar el método de Coppersmith (`trial_coppersmith.sage`) para recuperar los 64 bits inferiores desconocidos de la clave del Ciudadano 1.

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
