# Desafío CTF: `pascals-homomorphism-2` — Pascal's Homomorphism 2

## 1. Introducción
Segunda parte del desafío sobre el criptosistema de Paillier (mismo servicio en el puerto 1999), utilizando una clave fuerte de 1024 bits y un oráculo de descifrado limitado a entradas menores de 2000 bits.
- **Categoría:** Criptografía

## 2. Objetivo
Explotar la propiedad homomórfica aditiva del criptosistema de Paillier ($\text{Dec}(c_1 \cdot c_2 \bmod n^2) = (m_1 + m_2) \bmod n$) para eludir restricciones de longitud en un oráculo de descifrado.

## 3. Requisitos
- GP/PARI (o Python / SageMath) y `netcat`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Generar una clave fuerte (`genkey strong`), obtener la segunda flag cifrada $c$ (~2048 bits), extraer factores primos pequeños de $c$ hasta que el cofactor restante sea menor de 2000 bits, descifrar cada factor en el oráculo (`decrypt`) y sumar los textos planos resultantes módulo $n$.

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
