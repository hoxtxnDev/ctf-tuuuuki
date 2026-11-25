# Desafío CTF: `boxy` — Boxy

## 1. Introducción
Desafío presencial compuesto por dos cajas de seguridad idénticas (Boxy A y Boxy B) con cerradura de combinación.
- **Categoría:** Seguridad Física (On-Site)

## 2. Objetivo
Aplicar técnicas de observación y decodificación mecánica no destructiva sobre cerraduras de combinación en entorno de laboratorio.

## 3. Requisitos
- Acceso presencial a las cajas de práctica del laboratorio educativo.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Inspeccionar las holguras mecánicas de los discos de combinación para identificar la secuencia de apertura y recuperar la tarjeta interna.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `50` puntos (configurado en `metadata.yml`).
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
