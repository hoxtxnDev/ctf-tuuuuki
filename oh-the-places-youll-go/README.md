# Desafío CTF: `oh-the-places-youll-go` — Oh The Places You'll Go (Parte 1)

## 1. Introducción
Conjunto de 11 capturas de Google Street View frente a monumentos históricos mundiales junto con un mapa guía (`places.tar.gz`).
- **Categoría:** OSINT Geográfico

## 2. Objetivo
Aplicar técnicas de geolocalización visual (orientación de brújula, perspectiva arquitectónica y búsqueda en Street View) para ubicar puntos exactos e identificar caracteres en elementos del entorno.

## 3. Requisitos
- Navegador web con acceso a Google Maps / Street View y descompresor `tar`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/places.tar.gz`.

## 5. Metodología de resolución
Localizar cada una de las 11 vistas en Google Street View, extraer el número o palabra señalada por el recuadro en cada ubicación y ensamblar el mensaje según el orden del mapa.

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
- **Autor original:** `symmetric & TheSorites`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
