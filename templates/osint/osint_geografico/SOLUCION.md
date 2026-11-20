# Guía de Solución (Instructor) — Plantilla OSINT Geográfico

## 1. Nombre del desafío
**Coordenadas en la Bahía** (`plantilla-osint-geografico`)

## 2. Metodología de resolución paso a paso

### Paso 1: Análisis de metadatos EXIF
Al inspeccionar [`evidencias/reporte_exif_captura.json`](evidencias/reporte_exif_captura.json) se extraen los siguientes indicadores técnicos:
- **Huso horario:** `UTC-03:00` (`OffsetTimeOriginal`).
- **Coordenadas truncadas:** `33° 2' Sur`, `71° 37' Oeste`.
- **Dirección de cámara:** `42.5°` (Noreste).
- **Comentario de metadatos:** Menciona la Plaza Sotomayor y el código postal `23801`.

### Paso 2: Ubicación cartográfica y triangulación visual
1. Ingresando las coordenadas aproximadas `-33.033, -71.617` en OpenStreetMap o Google Maps, el punto cae directamente sobre el barrio puerto de **Valparaíso, Chile**.
2. Al contrastar con [`evidencias/bitacora_observacion_visual.txt`](evidencias/bitacora_observacion_visual.txt):
   - Al suroeste se ubica la **Plaza Sotomayor** y el **Monumento a los Héroes de Iquique**.
   - Avanzando hacia el noreste (acimut `42.5°`) desde la Plaza Sotomayor hacia la línea de costa se encuentra el **Muelle Prat**.

### Paso 3: Normalización y ensamblaje de la flag
Siguiendo el formato solicitado `DUOC{<recinto>_<ciudad>_<codigo_postal>}`:
- Recinto: `muelle_prat`
- Ciudad: `valparaiso`
- Código postal: `23801`

## 3. Flag esperada (Plantilla)
```text
DUOC{muelle_prat_valparaiso_23801}
```

## 4. Criterios de validación y adaptación para nuevos desafíos
- **Verificación de coincidencia:** La flag coincide exactamente con `challenge.yml` y `metadata.yml`.
- **Reutilización:** Para crear un nuevo desafío a partir de esta plantilla:
  1. Copia la carpeta `templates/osint/osint_geografico/` a un nuevo directorio en la raíz del repositorio.
  2. Sustituye los metadatos en `evidencias/reporte_exif_captura.json` (o adjunta una imagen `.jpg` generada con `exiftool`).
  3. Actualiza las referencias visuales en `evidencias/bitacora_observacion_visual.txt`.
  4. Define la nueva flag `DUOC{<hallazgo>_<numero>}` en `metadata.yml`, `challenge.yml`, `README.md` y `SOLUCION.md`.
