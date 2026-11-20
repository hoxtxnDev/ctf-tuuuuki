# Desafío CTF: `sighting` — Dragon Sighting

## 1. Introducción
Aplicación web en PHP que carga imágenes dinámicamente a través del endpoint `picture.php?file=...` sin validar que el archivo pertenezca al directorio permitido.
- **Categoría:** Seguridad Web (101)

## 2. Objetivo
Identificar y corregir vulnerabilidades de Inclusión Local de Archivos (LFI) / Path Traversal en parámetros de consulta PHP.

## 3. Requisitos
- Navegador web, `curl` o Ruby (`httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd sighting/challenge && docker build -t ctf-sighting . && docker run --rm -it -P ctf-sighting
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Modificar el parámetro `file` en `picture.php?file=../../../../../../flag.txt` para atravesar directorios hasta la raíz del sistema de archivos y leer `/flag.txt`.

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
