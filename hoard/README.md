# Desafío CTF: `hoard` — Dragon Hoard

## 1. Introducción
Calculadora web de tesoros cuyo backend en PHP (`backend.php`) recibe un objeto JSON e invoca un binario del sistema pasando los campos numéricos dentro de una cadena de shell.
- **Categoría:** Seguridad Web / Pwn

## 2. Objetivo
Analizar vulnerabilidades de inyección de comandos en APIs JSON cuando se confía en la validación de tipos del frontend sin sanitizar los argumentos en el backend.

## 3. Requisitos
- Cliente HTTP (`curl` o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd hoard/challenge && docker build -t ctf-hoard . && docker run --rm -it -P ctf-hoard
   ```
2. Archivos distribuidos al participante: `distfiles/backend.php`.

## 5. Metodología de resolución
Inspeccionar `distfiles/backend.php`, observar cómo se interpola el campo `artifacts` entre comillas simples en la llamada a `exec()` e inyectar el cierre de comilla simple seguido de la lectura de `/flag.txt`.

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
