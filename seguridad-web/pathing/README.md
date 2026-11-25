# Desafío CTF: `pathing` — Pathing

## 1. Introducción
Servidor web minimalista que resuelve rutas de archivos estáticos sin normalizar secuencias de salto de directorio (`../`).
- **Categoría:** Seguridad Web (101)

## 2. Objetivo
Comprender las vulnerabilidades de Path Traversal (Directory Traversal) a nivel de servidor HTTP y la importancia de canonicalizar rutas dentro del directorio raíz permitido.

## 3. Requisitos
- Cliente HTTP que no normalice rutas antes de enviarlas (`curl --path-as-is` o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd pathing/challenge && docker build -t ctf-pathing . && docker run --rm -it -P ctf-pathing
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Solicitar directamente `/../../../../../../flag.txt` desactivando la normalización local de URL en el cliente HTTP (`curl --path-as-is`).

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
