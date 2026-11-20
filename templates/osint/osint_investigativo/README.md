# Plantilla 3: Desafío de OSINT Investigativo — *Cronología Cruzada*

> **Nota de plantilla:** Este directorio es una plantilla reutilizable para diseñar desafíos de correlación investigativa de fuentes abiertas (cronologías, documentos públicos y repositorios de código) utilizando identidades y organizaciones 100% ficticias.

## 1. Nombre del desafío
**Cronología Cruzada** (`plantilla-osint-investigativo`)

## 2. Descripción narrativa
Un consorcio ficticio de telemetría marítima publicó un comunicado de prensa anunciando la puesta en marcha de una plataforma crítica, omitiendo deliberadamente el nombre clave del proyecto y su folio de expediente. Como analista OSINT, debes correlacionar la fecha y hora exacta del despliegue y el nombre de la responsable técnica con registros públicos de actividad en repositorios y actas de licitación abierta.

## 3. Nivel de dificultad
**Avanzado** (300 – 500 puntos / 1000 puntos en esquema dinámico)

## 4. Objetivos de aprendizaje
- Construir líneas de tiempo (*timelines*) unificando marcas temporales UTC procedentes de fuentes heterogéneas.
- Realizar pivoteo de entidades (*entity pivoting*) entre nombres propios, direcciones de correo electrónico, códigos de proyecto e identificadores administrativos.
- Auditar fugas de información operativa en mensajes de commit y metadatos de documentos públicos.

## 5. Contexto inicial para el participante
Analiza los tres archivos de evidencia pública adjuntos. Determina el nombre clave del proyecto desplegado el `18 de agosto de 2026` y su `folio_expediente` de 5 dígitos. Entrega la flag en formato `DUOC{<nombre_clave_en_minusculas_con_guiones_bajos>_<folio_expediente>}`.

## 6. Material y evidencias disponibles
- [`evidencias/comunicado_prensa_2026.txt`](evidencias/comunicado_prensa_2026.txt): Comunicado oficial con fecha, hora del evento y nombre de la ingeniera principal.
- [`evidencias/registro_commits_publicos.log`](evidencias/registro_commits_publicos.log): Historial de commits de un repositorio público de la organización.
- [`evidencias/acta_licitacion_abierta.csv`](evidencias/acta_licitacion_abierta.csv): Tabla pública de proyectos adjudicados y sus folios administrativos.

## 7. Pistas progresivas
1. **Pista 1 (Correlación temporal y de autor):** El comunicado menciona un despliegue el `18 de agosto de 2026 a las 14:15 UTC` liderado por `Elena Rostova`. Busca esa fecha y autora en `registro_commits_publicos.log`.
2. **Pista 2 (Extracción de identificador pivote):** El commit `9c4e1a2b` de `erostova-dev` a las `14:12:09 UTC` del 18 de agosto de 2026 revela el código interno `PRJ-FA-09`.
3. **Pista 3 (Resolución en el acta administrativa):** Busca `PRJ-FA-09` en `acta_licitacion_abierta.csv` para obtener el nombre clave `Operacion Faro Austral` y el folio `84920`.

## 8. Flag esperada (Plantilla)
```text
DUOC{operacion_faro_austral_84920}
```

## 9. Solución detallada
Consulta el documento [`SOLUCION.md`](SOLUCION.md) para ver el grafo de correlación y la guía completa del instructor.

## 10. Criterios de validación
- La flag cumple la expresión regular `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$`.
- Ninguna fuente individual contiene la respuesta completa: es indispensable cruzar los tres documentos (`Comunicado` -> `Fecha + Autora` -> `Commit Git` -> `Código PRJ-FA-09` -> `Acta CSV` -> `Nombre Clave + Folio`).
