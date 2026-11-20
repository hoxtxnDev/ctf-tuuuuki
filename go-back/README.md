# Desafío CTF: `go-back` — Go Back

## 1. Introducción
Entorno de terminal con un binario SUID (`go-back`) que compara el argumento recibido con `/home/ctf/flag.txt` y devuelve el resultado de `strcmp` como código de salida del proceso.
- **Categoría:** Misceláneo / Ingeniería Inversa

## 2. Objetivo
Analizar fugas de información por canal lateral basadas en códigos de retorno de procesos (*exit status oracle*) y por qué las comparaciones de secretos deben devolver únicamente un estado binario de tiempo constante.

## 3. Requisitos
- Acceso por terminal TCP (`netcat`) y Ruby o Bash.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd go-back/challenge && docker build -t ctf-go-back . && docker run --rm -it -P ctf-go-back
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Ejecutar `./go-back` carácter por carácter verificando el código de salida `$?` (`0` si coincide, `1` o `255` según el signo de la diferencia ASCII en `strcmp`) para reconstruir la flag secuencialmente.

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
