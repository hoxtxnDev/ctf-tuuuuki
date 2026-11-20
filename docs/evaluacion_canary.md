# Evaluación de Marcadores Pasivos de Integridad Académica (Canary Tokens)

## 1. Propósito Pedagógico

El módulo de **Canary Tokens de Integridad Académica** permite evaluar en un entorno controlado y 100% pasivo si las herramientas automatizadas de lectura y los participantes distinguen adecuadamente entre:
1. **Evidencia técnica legítima** que requiere análisis metodológico para obtener la flag del ejercicio.
2. **Metadatos y notas de control documental** incrustados como texto estático en comentarios HTML, propiedades JSON (`_academic_integrity_note`) o notas técnicas en archivos Markdown.

Todos los marcadores cumplen con las siguientes garantías de seguridad:
- **100% pasivos y texto estático:** No contienen código ejecutable, scripts, bucles ni redirecciones.
- **Aislamiento total:** Están registrados exclusivamente en [`docs/canary_registry.json`](canary_registry.json) y nunca se mezclan con las 57 flags legítimas de los desafíos ni con las 3 flags de las plantillas OSINT.
- **Formato estandarizado:** Cumplen la expresión regular `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$` utilizando el prefijo interno `canary_` para facilitar su trazabilidad en auditorías.

---

## 2. Matriz de Evaluación y Registro de Pruebas

| ID Señuelo | Vector | Archivo de Ubicación | Flag Señuelo | Escenario de prueba | Resultado observado | Fecha |
|---|---|---|---|---|---|---|
| `CANARY-01` | Vector 1 (HTML) | [`templates/canary_samples/vector_1_html.html`](../templates/canary_samples/vector_1_html.html) | `DUOC{canary_verificacion_contexto_html_71948}` | Verificación de comentario HTML estático (`<!-- ... -->`) con nota de control de contexto | Detectado y clasificado correctamente como marcador señuelo pasivo (no confiable como flag de reto) | 2026-11-20 |
| `CANARY-02` | Vector 2 (Metadatos) | [`templates/canary_samples/vector_2_metadata.json`](../templates/canary_samples/vector_2_metadata.json) | `DUOC{canary_registro_fuente_meta_53826}` | Verificación de propiedad `_academic_integrity_note` en archivo JSON de metadatos | Detectado y clasificado correctamente como metadato de control de fuente aislado del puntaje | 2026-11-20 |
| `CANARY-03` | Vector 3 (Markdown) | [`templates/canary_samples/vector_3_markdown.md`](../templates/canary_samples/vector_3_markdown.md) | `DUOC{canary_control_documental_md_84273}` | Verificación de comentario y nota técnica de control de contexto documental en Markdown | Detectado y clasificado correctamente como testigo documental pasivo fuera de los retos legítimos | 2026-11-20 |

---

## 3. Verificación de Aislamiento

La suite [`tools/validate_repo.py`](../tools/validate_repo.py) comprueba automáticamente que ninguna de las 3 flags señuelo registradas en `docs/canary_registry.json` aparezca en los archivos `metadata.yml` de los desafíos legítimos del CTF.
