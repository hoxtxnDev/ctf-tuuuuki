# Guía de Solución (Instructor) — Plantilla OSINT Investigativo

## 1. Nombre del desafío
**Cronología Cruzada** (`plantilla-osint-investigativo`)

## 2. Metodología de resolución paso a paso

### Paso 1: Extracción de selectores iniciales en el comunicado
De [`evidencias/comunicado_prensa_2026.txt`](evidencias/comunicado_prensa_2026.txt) se obtienen dos selectores verificables:
- **Marca temporal del hito:** `2026-08-18 14:15 UTC`.
- **Persona responsable:** `Elena Rostova`.

### Paso 2: Pivoteo hacia el historial de commits
En [`evidencias/registro_commits_publicos.log`](evidencias/registro_commits_publicos.log):
- Se localiza el commit `9c4e1a2b` realizado por `erostova-dev <e.rostova@magallanes-tech.internal.edu>` el `Tue Aug 18 14:12:09 2026 +0000` (3 minutos antes del corte anunciado).
- El mensaje del commit expone el identificador interno de proyecto: `PRJ-FA-09`.

### Paso 3: Cruce con el registro de licitaciones
En [`evidencias/acta_licitacion_abierta.csv`](evidencias/acta_licitacion_abierta.csv):
- La fila correspondiente a `PRJ-FA-09` (responsable `E. Rostova`) registra:
  - `nombre_clave_proyecto`: `Operacion Faro Austral`
  - `folio_expediente`: `84920`
- Al normalizar según el formato solicitado (`DUOC{operacion_faro_austral_84920}`), se obtiene la flag.

## 3. Flag esperada (Plantilla)
```text
DUOC{operacion_faro_austral_84920}
```

## 4. Criterios de validación y adaptación para nuevos desafíos
- **Privacidad y datos sintéticos:** Al diseñar variaciones de esta plantilla, utiliza siempre nombres ficticios y dominios `.internal.edu` o `.example.com`.
- **Verificación:** La flag coincide exactamente con `challenge.yml` y `metadata.yml`.
