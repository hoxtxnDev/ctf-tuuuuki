# Desafío CTF: `goto-zero` — Goto Zero

## 1. Introducción
Binario SUID con vulnerabilidad de desbordamiento de búfer en la pila, compilado sin PIE pero con aleatorización del espacio de direcciones (ASLR) activa en el sistema.
- **Categoría:** Pwn / Binarios

## 2. Objetivo
Construir cadenas de programación orientada a retorno (ROP) en dos etapas: filtración de direcciones de `libc` mediante la tabla GOT/PLT con retorno a `main()`, seguida de lectura del archivo de la flag.

## 3. Requisitos
- Ruby, `objdump`/`gdb` y cliente TCP (`netcat`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd goto-zero/challenge && docker build -t ctf-goto-zero . && docker run --rm -it -P ctf-goto-zero
   ```
2. Archivos distribuidos al participante: `distfiles/goto-zero`.

## 5. Metodología de resolución
Enviar una primera carga útil ROP que invoque `puts(puts@GOT)` y retorne a `main()`, calcular la dirección base de `libc` a partir de la dirección filtrada y enviar una segunda cadena ROP que ejecute `open`/`read`/`puts` sobre `/home/ctf/flag.txt`.

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
