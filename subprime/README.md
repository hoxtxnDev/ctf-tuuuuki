# Desafío CTF: `subprime` — Subprime

## 1. Introducción
Archivo de texto con una clave pública RSA de módulo pequeño ($n = 98563159, e = 1009$) y un arreglo de enteros que representan los caracteres de la flag cifrados individualmente.
- **Categoría:** Criptografía (101)

## 2. Objetivo
Comprender los fundamentos matemáticos de RSA y por qué la seguridad del esquema depende de que el módulo $n = p \cdot q$ no pueda factorizarse en tiempo razonable.

## 3. Requisitos
- Python 3.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/cipher.txt`, `distfiles/pubkeypair.txt`.

## 5. Metodología de resolución
Factorizar $n = 98563159 = 9883 \times 9973$, calcular $\phi(n) = 98543304$ y la clave privada $d = e^{-1} \bmod \phi(n) = 31545577$, y descifrar cada entero $c_i$ del archivo `distfiles/cipher.txt` como $m_i = c_i^d \bmod n$.

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
