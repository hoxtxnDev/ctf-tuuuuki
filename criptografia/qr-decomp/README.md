# Desafío CTF: `qr-decomp` — QR Decomposition

## 1. Introducción
Cinco fragmentos de códigos QR que contienen las matrices ortogonal $Q$ y triangular superior $R$ resultantes de la descomposición QR de una matriz $M_{4\times 4}$ con los caracteres de la flag.
- **Categoría:** Criptografía / Matemáticas (On-Site 101)

## 2. Objetivo
Relacionar el concepto de códigos QR con la descomposición matricial $M = Q \cdot R$ del álgebra lineal para reconstruir información codificada en matrices numéricas.

## 3. Requisitos
- Lector de códigos QR y entorno de cálculo matricial (GP/PARI, Python NumPy o Octave).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Ensamblar y escanear los fragmentos de los códigos QR 1, 2a/2b y 3a/3b para obtener las matrices $Q$ y $R$, multiplicar $Q \times R$, redondear al entero más cercano y convertir los 16 valores ASCII a texto.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `100` puntos (configurado en `metadata.yml`).
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
