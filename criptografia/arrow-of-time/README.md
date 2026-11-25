# Desafío CTF: `arrow-of-time` — Arrow of Time

## 1. Introducción
Reloj criptográfico cuyo estado interno de 64 bits avanza cada segundo aplicando MD5 truncado a 8 bytes, acompañado de un video con marcas de tiempo futuras.
- **Categoría:** Criptografía

## 2. Objetivo
Aplicar algoritmos de detección de ciclos (algoritmo de Brent) sobre funciones iteradas de espacio finito para retroceder estados dentro de un ciclo periódico.

## 3. Requisitos
- Compilador C (`gcc`), biblioteca OpenSSL (`libcrypto`), Python 3 y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd arrow-of-time/challenge && docker build -t ctf-arrow-of-time . && docker run --rm -it -P ctf-arrow-of-time
   ```
2. Archivos distribuidos al participante: `distfiles/aclock.mp4`.

## 5. Metodología de resolución
Determinar la longitud del ciclo $\lambda$ del hash MD5 truncado a 64 bits utilizando el algoritmo de Brent (`md5_brent.c`) y avanzar $(\lambda - (t_{\text{futuro}} - t_{\text{actual}})) \bmod \lambda$ pasos desde el estado conocido.

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
