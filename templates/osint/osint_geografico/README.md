# Plantilla 1: Desafío de OSINT Geográfico — *Coordenadas en la Bahía*

> **Nota de plantilla:** Este directorio es una plantilla reutilizable para diseñar desafíos de geolocalización (GEOINT/IMINT) con datos ficticios o recursos públicos autorizados.

## 1. Nombre del desafío
**Coordenadas en la Bahía** (`plantilla-osint-geografico`)

## 2. Descripción narrativa
Durante un ejercicio de simulación logística, un auditor de infraestructura portuaria envió una captura ambiental junto con una bitácora descriptiva antes de quedar sin cobertura. Los metadatos GPS del archivo fueron parcialmente truncados por el sistema de mensajería, pero se conservan el rumbo magnético, el huso horario y referencias arquitectónicas inequívocas del entorno.

## 3. Nivel de dificultad
**Intermedio** (200 – 400 puntos / 1000 puntos en esquema dinámico)

## 4. Objetivos de aprendizaje
- Extraer e interpretar metadatos técnicos EXIF (`DateTimeOriginal`, `OffsetTimeOriginal`, `GPSImgDirection`, hemisferios `South`/`West`).
- Realizar triangulación visual (*landmark triangulation*) correlacionando elementos urbanos, monumentos y orientación acimutal en cartografía abierta (OpenStreetMap / Google Street View).
- Normalizar hallazgos geográficos para construir cadenas de respuesta deterministas.

## 5. Contexto inicial para el participante
Recibes dos artefactos recopilados de la transmisión del auditor. Tu misión es identificar el nombre exacto del muelle histórico donde se encontraba parado el observador, la ciudad correspondiente y el código postal de 5 dígitos del sector, entregando la respuesta en el formato `DUOC{<recinto>_<ciudad>_<codigo_postal>}` (todo en minúsculas, sin tildes y separado por guiones bajos).

## 6. Material y evidencias disponibles
- [`evidencias/reporte_exif_captura.json`](evidencias/reporte_exif_captura.json): Volcado JSON de metadatos EXIF de la fotografía original.
- [`evidencias/bitacora_observacion_visual.txt`](evidencias/bitacora_observacion_visual.txt): Descripción de puntos de referencia visuales en los cuatro cuadrantes alrededor del observador.

## 7. Pistas progresivas
1. **Pista 1 (Orientación por metadatos):** Revisa los campos `GPSLatitude_Partial` (`33° 2' S`) y `GPSLongitude_Partial` (`71° 37' W`) en `reporte_exif_captura.json`. Esa latitud y longitud sitúan la escena en la costa central de Chile.
2. **Pista 2 (Triangulación arquitectónica):** La bitácora menciona que a espaldas del observador (suroeste) se encuentra la Plaza Sotomayor y el Monumento a los Héroes de Iquique, mientras que al frente (noreste, acimut 42.5°) hay un embarcadero turístico de lanchas.
3. **Pista 3 (Construcción de la flag):** El embarcadero contiguo a la Plaza Sotomayor en Valparaíso es el **Muelle Prat**, y el código postal de referencia indicado en los metadatos es `23801`.

## 8. Flag esperada (Plantilla)
```text
DUOC{muelle_prat_valparaiso_23801}
```

## 9. Solución detallada
Consulta el documento [`SOLUCION.md`](SOLUCION.md) para ver la guía paso a paso destinada a instructores y auditores del laboratorio.

## 10. Criterios de validación
- La cadena debe cumplir exactamente la expresión regular `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$`.
- El participante debe demostrar la correlación entre al menos dos fuentes: los metadatos parciales EXIF (`33° 2' S, 71° 37' W`, código `23801`) y las referencias visuales de la Plaza Sotomayor / Muelle Prat.
- Al clonar esta plantilla para un nuevo reto, reemplaza los archivos en `evidencias/` y actualiza la clave `flag` en `challenge.yml` y `metadata.yml`.
