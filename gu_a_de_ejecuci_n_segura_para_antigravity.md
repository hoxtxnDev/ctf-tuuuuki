# Plan de Trabajo y Refactorización: Repositorio CTF Educativo

Este documento define las instrucciones oficiales de ingeniería, localización y documentación para este repositorio de laboratorio educativo.

## Reglas Globales para el Agente
1. **Ejecución estrictamente por fases:** Ejecuta únicamente la fase solicitada por el usuario y detente al entregar el reporte de esa fase. No avances a la siguiente sin confirmación explícita.
2. **Conservación de arquitectura:** Respeta la estructura de directorios, archivos `challenge.yml`, `Dockerfile`, `docker-compose.yml` y mecánicas originales de cada ejercicio.
3. **Bloques técnicos en solo lectura durante localización:** Al traducir documentación o guías al español, conserva intactos los comandos de terminal, rutas, nombres de herramientas y fragmentos de código. No los depures ni los reescribas.
4. **Cero modificaciones destructivas en artefactos binarios:** Si una cadena de respuesta está incrustada dentro de un archivo compilado, imagen o archivo comprimido que no pueda editarse como texto plano sin reconstruirlo, no lo alteres; regístralo como pendiente manual.
5. **Verificación real:** No reportes una tarea o prueba como exitosa si no fue verificada directamente mediante inspección o ejecución de comandos.

---

## Comandos rápidos para el usuario (Copiar y pegar en Antigravity)

* **Iniciar Fase 0:** `Lee ANTIGRAVITY_RUNBOOK.md y ejecuta únicamente la Fase 0 (solo lectura).`
* **Iniciar Fase 1A:** `Ejecuta únicamente la Fase 1A definida en ANTIGRAVITY_RUNBOOK.md.`
* **Iniciar Fase 1B (repetir por carpeta/categoría):** `Ejecuta la Fase 1B de ANTIGRAVITY_RUNBOOK.md únicamente sobre las carpetas: [CARPETA_1, CARPETA_2].`
* **Iniciar Fase 2:** `Ejecuta únicamente la Fase 2 definida en ANTIGRAVITY_RUNBOOK.md.`
* **Iniciar Fase 3:** `Ejecuta únicamente la Fase 3 definida en ANTIGRAVITY_RUNBOOK.md.`
* **Iniciar Fase 4:** `Ejecuta únicamente la Fase 4 definida en ANTIGRAVITY_RUNBOOK.md.`

---

## Fase 0: Inventario y Auditoría Inicial (Solo Lectura)

**Restricción:** En esta fase no modifiques, crees ni elimines ningún archivo del repositorio.

### Tareas
1. Recorre el árbol de directorios completo del repositorio e identifica:
   - Carpetas de desafíos y categorías existentes.
   - Archivos de configuración (`challenge.yml`, JSON, variables de entorno, etc.).
   - Guías de solución / documentación pedagógica y su idioma actual.
   - Scripts de prueba o validación automatizada disponibles.
2. Detecta todas las cadenas de respuesta (flags) actuales y lista en qué archivos aparecen referenciadas.
3. Identifica posibles riesgos técnicos antes de editar:
   - Flags almacenadas dentro de binarios, imágenes, PCAPs o archivos comprimidos.
   - Retos donde el estudiante debe construir la flag a partir de datos reales/investigados (por ejemplo, OSINT).
   - Referencias cruzadas entre retos o archivos compartidos.

### Entregable obligatorio de Fase 0
Presenta una tabla con las columnas:
`Categoría | Carpeta del Reto | Flag Actual | Archivos que la referencian | Idioma actual | Tipo (Texto / Artefacto binario / Deducible)`

Al finalizar, sugiere cómo agrupar las carpetas en lotes pequeños (2 a 3 retos por lote) para la Fase 1B y espera confirmación.

---

## Fase 1A: Estandarización de Cadenas de Respuesta (Flags)

**Alcance:** Trabaja únicamente sobre archivos de configuración, texto plano, tests de verificación y referencias textuales. No analices ni reescribas scripts técnicos complejos en este paso.

### Formato obligatorio
Todas las flags legítimas deben seguir el patrón estricto:
`DUOC{palabra_clave_XXXXX}`

### Reglas de diseño (para mantener la dificultad original)
1. **Estructura:** Prefijo `DUOC{`, cierre `}`, solo minúsculas, números y guiones bajos (`_`).
2. **Prevención de adivinación:**
   - La `palabra_clave` debe aludir al hallazgo interno del ejercicio, **no** copiar literalmente el título público del reto.
   - El sufijo numérico `XXXXX` debe ser un número aleatorio de **5 dígitos** (evitar años obvios como `2026` o secuencias como `123`, `001`).
   - **Excepción OSINT deducible:** Si el participante debe construir la flag a partir de un dato encontrado en su investigación (coordenada, código postal, ASN, año de registro o identificador público), usa ese dato numérico verificable en lugar de dígitos aleatorios y documenta el formato esperado en el enunciado.
3. **Unicidad:** Cero flags duplicadas en todo el repositorio.
4. **Consistencia 1 a 1:** Actualiza todas las ocurrencias de cada flag en su configuración, archivos de texto del reto, tests y documentación asociada.
5. **Estrategia recomendada:** Si hay muchos archivos o carpetas extensas, genera y ejecuta un script temporal en Python (`tools/update_flags.py`) que realice los reemplazos deterministas de texto y verifique coincidencias antes de finalizar.
6. **Artefactos no editables:** Si una flag está embebida en un binario compilado, imagen o archivo cifrado que requiera recompilación manual, no modifiques el artefacto ni su `challenge.yml`; márcalo como `Pendiente manual` para no romper la coherencia del reto.

### Entregable obligatorio de Fase 1A
Tabla de mapeo:
`Carpeta | Flag anterior | Flag nueva | Archivos actualizados | Estado (Actualizado / Pendiente manual)`

---

## Fase 1B: Localización al Español y Revisión Documental (Por Lotes)

**Alcance:** Ejecutar únicamente sobre las 2 o 3 carpetas indicadas por el usuario en el turno actual.

### Tareas
1. Traduce íntegramente al español el contenido narrativo y pedagógico de las soluciones, pistas, comentarios descriptivos y notas explicativas dentro del lote indicado.
2. **Regla de conservación técnica:** Copia exactamente sin alterar todos los bloques de código, comandos de terminal, flags de CLI, expresiones regulares y salidas de consola.
3. Verifica coherencia documental:
   - Que la flag mencionada en la solución coincida exactamente con la flag configurada en Fase 1A.
   - Que las pistas estén alineadas con el objetivo del reto.
4. Si detectas en la documentación un paso confuso, un enlace roto o una dependencia faltante (por ejemplo, una herramienta no mencionada en los requisitos), **anótalo como observación en el reporte final** en lugar de modificar bloques de código técnico.

### Entregable obligatorio de Fase 1B
- Lista de archivos traducidos en este lote.
- Confirmación de coincidencia de flags.
- Lista de observaciones o dependencias faltantes detectadas.

---

## Fase 2: Plantillas OSINT Reutilizables y Documentación README

### 1. Tres Plantillas OSINT Reutilizables
Crea una carpeta `templates/osint/` (o respeta la carpeta de plantillas existente en el repo) con tres plantillas listas para clonar y crear nuevos ejercicios, usando exclusivamente **datos ficticios o recursos públicos autorizados**:

1. `templates/osint/osint_geografico/`: Identificación de ubicaciones mediante fotografías de ejemplo, referencias visuales y metadatos EXIF.
2. `templates/osint/osint_digital/`: Investigación de dominios ficticios, infraestructura pública, registros DNS y relaciones entre activos digitales.
3. `templates/osint/osint_investigativo/`: Correlación de cronologías, fuentes abiertas y pistas cruzadas entre múltiples documentos públicos ficticios.

Cada plantilla debe incluir un archivo `challenge.yml` base (si el repo usa ese estándar), un `README.md` y un `SOLUCION.md` que contemplen obligatoriamente:
- Nombre del desafío.
- Descripción narrativa.
- Nivel de dificultad.
- Objetivos de aprendizaje.
- Contexto inicial para el participante.
- Material y evidencias disponibles.
- Pistas progresivas (3 niveles).
- Flag esperada en formato `DUOC{hallazgo_XXXXX}` (marcada claramente como plantilla).
- Solución detallada paso a paso.
- Criterios de validación.

### 2. Documentación README en Español
- **README por desafío:** Crea o actualiza el `README.md` en español de cada reto existente con las secciones:
  1. Introducción
  2. Objetivo
  3. Requisitos
  4. Instrucciones de ejecución
  5. Metodología general (orientación sin revelar la flag)
  6. Sistema de puntuación
  7. Formato de flags
  8. Consideraciones de seguridad y uso ético
  9. Créditos y referencias
- **README raíz (`README.md`):** Documenta la estructura completa del repositorio, el estándar de flags, los comandos de despliegue/validación y una guía clara sobre cómo crear nuevos desafíos a partir de las plantillas OSINT.

### Entregable obligatorio de Fase 2
Listado de plantillas creadas y archivos `README.md` creados o actualizados.

---

## Fase 3: Módulo Pasivo de Flags Señuelo (Canary Tokens de Integridad Académica)

### Objetivo
Implementar un conjunto de marcadores pasivos de control para pruebas de integridad académica en entornos educativos, verificando si sistemas automatizados de lectura distinguen correctamente entre el enunciado legítimo del ejercicio y metadatos de control no autorizados.

### Requisitos de Implementación
1. **Aislamiento total:** Crea un archivo de registro independiente en `docs/canary_registry.json` (fuera del registro de flags legítimas y excluido de la puntuación del CTF) que almacene **3 flags señuelo** únicas con formato `DUOC{canary_..._XXXXX}`.
2. **Ubicación pasiva en tres vectores de plantilla/ejemplo:** Inserta cada marcador como texto estático e inerte dentro de archivos de ejemplo en `templates/canary_samples/` (o en comentarios de las plantillas creadas en Fase 2):
   - **Vector 1 (HTML):** Comentario HTML estático (`<!-- ... -->`) con una nota de control de verificación de contexto.
   - **Vector 2 (Metadatos):** Campo de metadatos benigno en un archivo JSON o YAML de ejemplo (`_academic_integrity_note`) simulando un aviso de verificación de fuente.
   - **Vector 3 (Markdown):** Comentario o nota técnica en un archivo Markdown de ejemplo simulando una instrucción de control de contexto documental.
3. **Matriz de evaluación:** Crea `docs/evaluacion_canary.md` en español explicando el propósito pedagógico del control de integridad y agregando una tabla de registro (`ID Señuelo | Vector | Flag Señuelo | Escenario de prueba | Resultado observado | Fecha`) para documentar pruebas controladas.

### Restricciones estrictas de seguridad
- Todos los archivos y señuelos deben ser **100% pasivos y texto estático**.
- Prohibido incluir scripts ejecutables, redirecciones, bucles, código que altere navegadores o mecanismos activos sobre herramientas externas.
- Las flags señuelo nunca deben coincidir ni mezclarse con las flags legítimas del CTF.

### Entregable obligatorio de Fase 3
Tabla con las 3 flags señuelo, su ubicación exacta y confirmación de que no interfieren con los archivos de configuración de los retos legítimos.

---

## Fase 4: Validación Integral y Reporte Final

Ejecuta verificaciones reales mediante comandos o un script de auditoría (`tools/validate_repo.py`) y reporta las salidas exactas.

### Lista de Verificación Obligatoria
1. **Cero duplicados:** Confirmar que no existen flags repetidas en todo el repositorio (ni entre legítimas ni con las flags señuelo).
2. **Validación de formato:** Confirmar que el 100% de las flags legítimas y señuelo cumplen la expresión regular:
   `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$`
3. **Integridad desafío-solución:** Confirmar que cada flag configurada en el reto coincide exactamente con la documentada en su solución.
4. **Idioma:** Confirmar que los `README.md` y soluciones están completamente en español.
5. **Plantillas OSINT:** Confirmar que las 3 plantillas están completas, son reutilizables y solo usan datos ficticios/autorizados.
6. **Canary Tokens pasivos:** Confirmar que los 3 señuelos son exclusivamente texto estático, están registrados en `docs/canary_registry.json` y aislados de las flags legítimas.
7. **Pruebas automatizadas:** Ejecutar las suites de pruebas existentes del proyecto (si aplica) y adjuntar el resultado real.

### Reporte Final de Entrega
Al cerrar la Fase 4, presenta:
- Árbol final del proyecto.
- Resumen de archivos modificados y archivos nuevos creados.
- Listado completo de flags legítimas actualizadas.
- Listado de flags señuelo implementadas.
- Resultado textual de las validaciones y pruebas ejecutadas.
- Lista explícita de elementos pendientes manuales (por ejemplo, binarios o artefactos no reconstruidos) o errores no resueltos.