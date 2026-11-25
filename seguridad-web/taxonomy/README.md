# Desafío CTF: `taxonomy` — Dragon Taxonomy

## 1. Introducción
Directorio web de especies de dragones respaldado por SQLite que oculta los registros marcados con `is_classified = 0` pero concatena el término de búsqueda directamente dentro de paréntesis en la consulta SQL.
- **Categoría:** Seguridad Web (101)

## 2. Objetivo
Aprender a identificar la estructura de consultas SQL con condiciones agrupadas por paréntesis y cómo evitar la inyección SQL utilizando parámetros vinculados (*bound parameters*).

## 3. Requisitos
- Navegador web, `curl` o Ruby (`httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd taxonomy/challenge && docker build -t ctf-taxonomy . && docker run --rm -it -P ctf-taxonomy
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Cerrar la comilla simple y el paréntesis de la condición de búsqueda en el parámetro `?search=Nano' OR 1=1) --` para anular el filtro `AND is_classified = 0` y listar el registro `Dragon-000`.

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
