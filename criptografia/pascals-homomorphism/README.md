# Desafío CTF: `pascals-homomorphism` — Pascal's Homomorphism 1

## 1. Introducción
Servicio interactivo que implementa el criptosistema homomórfico de Paillier con una clave inicial débil de 192 bits para cifrar la primera flag.
- **Categoría:** Criptografía

## 2. Objetivo
Comprender la estructura matemática del criptosistema de Paillier ($g = n + 1$, módulo $n^2$) y cómo recuperar el texto plano cuando el módulo $n = p \cdot q$ puede factorizarse.

## 3. Requisitos
- GP/PARI (o Python / SageMath) y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd pascals-homomorphism/challenge && docker build -t ctf-pascals-homomorphism . && docker run --rm -it -P ctf-pascals-homomorphism
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Conectarse al servicio, obtener el módulo débil $n$ de 192 bits y el texto cifrado de la primera flag (`getflag`), factorizar $n = p \cdot q$ para calcular $\lambda = (p-1)(q-1)$ y $u = \lambda^{-1} \bmod n$, y aplicar la función de descifrado de Paillier.

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
