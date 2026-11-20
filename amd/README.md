# Desafío CTF: `amd` — Advanced Machinecode Defense

## 1. Introducción
Utilidad de actualización de firmware que valida la clave pública RSA mediante AES-CMAC con una clave simétrica conocida antes de verificar la firma del código.
- **Categoría:** Criptografía / Pwn

## 2. Objetivo
Analizar por qué un código de autenticación de mensajes simétrico (AES-CMAC) cuya clave está embebida no proporciona resistencia a preimagen y permite forjar un módulo RSA válido.

## 3. Requisitos
- Python 3 (`pycryptodome`, `sympy`), `nasm` y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd amd/challenge && docker build -t ctf-amd . && docker run --rm -it -P ctf-amd
   ```
2. Archivos distribuidos al participante: `distfiles/amd`, `distfiles/official_blob.hex`.

## 5. Metodología de resolución
Invertir los últimos bloques de AES-CMAC en `aes_cmac.py` para construir un módulo de 2048 bits que produzca el CMAC esperado y sea fácilmente factorizable, permitiendo firmar una actualización con `build_forged_blob.py`.

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
