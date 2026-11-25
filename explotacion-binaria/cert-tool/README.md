# Desafío CTF: `cert-tool` — Cert-Tool

## 1. Introducción
Herramienta de inspección de certificados TLS en Base64 que invoca a OpenSSL internamente tras decodificar la entrada en un búfer contiguo al comando.
- **Categoría:** Pwn / Binarios

## 2. Objetivo
Identificar vulnerabilidades de subdesbordamiento de índice (*buffer underflow*) causadas por el manejo incorrecto de caracteres de relleno (`=`) en decodificadores Base64 personalizados.

## 3. Requisitos
- Python 3 y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd cert-tool/challenge && docker build -t ctf-cert-tool . && docker run --rm -it -P ctf-cert-tool
   ```
2. Archivos distribuidos al participante: `distfiles/cert-tool`.

## 5. Metodología de resolución
Revisar la función de decodificación Base64 para observar que cada carácter `=` resta 2 bits al desplazamiento actual, permitiendo retroceder 128 bytes (512 signos `=`) y sobrescribir el búfer del comando ejecutado por el servidor.

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
