# Desafío CTF: `oh-the-places-youll-go-2` — Oh The Places You'll Go (Parte 2)

## 1. Introducción
Segunda etapa del desafío de geolocalización OSINT compuesta por 12 fotografías de carreteras y costas sin monumentos famosos.
- **Categoría:** OSINT Geográfico

## 2. Objetivo
Utilizar metadatos visuales avanzados de geolocalización (formato de matrículas, bolardos, señalética vial, posición solar y vehículos de captura) para determinar coordenadas geográficas exactas.

## 3. Requisitos
- Navegador web con acceso a Google Maps / Street View, guías de geolocalización (Plonk It / GeoHints).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Identificar el país y punto exacto de las 12 imágenes, tomar los dos primeros dígitos decimales de la latitud y longitud de cada punto (4 dígitos por imagen, 48 dígitos en total) y construir la flag en el formato `DUOC{coordenadas_<48_digitos>}`.

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
