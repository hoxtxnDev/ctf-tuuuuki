# Laboratorio Educativo Capture The Flag (CTF) — DUOC

Repositorio integral de ciberseguridad educativa, auditoría defensiva y diseño de desafíos **Capture The Flag (CTF)**, completamente localizado al español y estandarizado bajo el formato institucional `DUOC{palabra_clave_XXXXX}`.

---

## Tabla de Contenidos

1. [Resumen Ejecutivo del Contenido](#1-resumen-ejecutivo-del-contenido)
2. [Arquitectura y Estructura del Repositorio](#2-arquitectura-y-estructura-del-repositorio)
3. [Estándar Institucional de Flags](#3-estándar-institucional-de-flags)
4. [Catálogo Completo de los 57 Desafíos por Categoría](#4-catálogo-completo-de-los-57-desafíos-por-categoría)
   - [4.1 Seguridad Web (15 desafíos)](#41-seguridad-web-15-desafíos)
   - [4.2 Criptografía (11 desafíos)](#42-criptografía-11-desafíos)
   - [4.3 Forense Digital y Esteganografía (11 desafíos)](#43-forense-digital-y-esteganografía-11-desafíos)
   - [4.4 Explotación de Binarios — Pwn (4 desafíos)](#44-explotación-de-binarios--pwn-4-desafíos)
   - [4.5 Ingeniería Inversa — RE (4 desafíos)](#45-ingeniería-inversa--re-4-desafíos)
   - [4.6 Inteligencia de Fuentes Abiertas — OSINT (2 desafíos + 3 plantillas)](#46-inteligencia-de-fuentes-abiertas--osint-2-desafíos--3-plantillas)
   - [4.7 Seguridad Móvil — Android (2 desafíos)](#47-seguridad-móvil--android-2-desafíos)
   - [4.8 Inteligencia Artificial / Machine Learning (1 desafío)](#48-inteligencia-artificial--machine-learning-1-desafío)
   - [4.9 Seguridad Física / On-Site y Misceláneos (7 desafíos)](#49-seguridad-física--on-site-y-misceláneos-7-desafíos)
5. [Plantillas Reutilizables de OSINT (`templates/osint/`)](#5-plantillas-reutilizables-de-osint-templatesosint)
6. [Módulo Pasivo de Integridad Académica — Canary Tokens (`docs/` y `templates/canary_samples/`)](#6-módulo-pasivo-de-integridad-académica--canary-tokens-docs-y-templatescanary_samples)
7. [Herramientas de Automatización y Auditoría (`tools/`)](#7-herramientas-de-automatización-y-auditoría-tools)
8. [Guía de Despliegue y Creación de Nuevos Desafíos](#8-guía-de-despliegue-y-creación-de-nuevos-desafíos)
9. [Consideraciones de Seguridad y Uso Ético](#9-consideraciones-de-seguridad-y-uso-ético)

---

## 1. Resumen Ejecutivo del Contenido

Este repositorio contiene:
- **57 desafíos técnicos** con código fuente, contenedores `Dockerfile` / `docker-compose.yml`, archivos distribuibles (`distfiles/`), metadatos (`metadata.yml`), documentación para participantes (`README.md`) y guías de resolución para instructores (`solution/README.md`) íntegramente en español.
- **3 plantillas OSINT reutilizables** (`osint_geografico`, `osint_digital`, `osint_investigativo`) con evidencias sintéticas autorizadas, pistas progresivas de 3 niveles, solución paso a paso y criterios de validación.
- **Módulo pasivo de Canary Tokens** (3 flags señuelo aisladas en `docs/canary_registry.json` y desplegadas en 3 vectores estáticos HTML, JSON y Markdown) para evaluar la resistencia a *prompt injection* y el control de integridad académica.
- **Suite de validación automatizada** (`tools/validate_repo.py`) que audita unicidad de las 63 flags, formato regex, coherencia desafío-solución, localización al español y ejecución de pruebas.

---

## 2. Arquitectura y Estructura del Repositorio

```text
.
├── README.md                                        # Documentación general del proyecto y catálogo completo
├── gu_a_de_ejecuci_n_segura_para_antigravity.md     # Runbook de ingeniería y auditoría por fases
├── <carpeta-del-reto>/                              # 57 directorios de desafíos individuales
│   ├── README.md                                    # Guía del participante en español (9 secciones)
│   ├── metadata.yml                                 # Configuración del reto, puerto, protocolo y flag oficial
│   ├── challenge/                                   # Código fuente, Dockerfile y activos del servicio
│   ├── distfiles/                                   # Archivos públicos entregados al jugador
│   └── solution/
│       ├── README.md                                # Writeup detallado en español con flag sincronizada
│       └── solve.rb / solve.py / solution.py        # Scripts de verificación y resolución automatizada
├── templates/
│   ├── osint/                                       # 3 plantillas base para nuevos desafíos OSINT
│   │   ├── osint_geografico/                        # GEOINT / IMINT (EXIF + triangulación visual)
│   │   ├── osint_digital/                           # DNS pasivo + Certificate Transparency + RDAP/ASN
│   │   └── osint_investigativo/                     # Correlación cronológica y pivoteo multi-documento
│   └── canary_samples/                              # Vectores estáticos de evaluación de integridad académica
│       ├── vector_1_html.html                       # Vector 1: Comentario HTML estático
│       ├── vector_2_metadata.json                   # Vector 2: Propiedad _academic_integrity_note en JSON
│       └── vector_3_markdown.md                     # Vector 3: Nota técnica en Markdown
├── docs/
│   ├── canary_registry.json                         # Registro aislado de las 3 flags señuelo (fuera del puntaje)
│   └── evaluacion_canary.md                         # Matriz de evaluación y registro de pruebas de Canary Tokens
└── tools/
    ├── update_flags.py                              # Script determinista de estandarización de flags
    ├── generate_docs_and_templates.py               # Generador de documentación pedagógica en español
    └── validate_repo.py                             # Suite de validación integral del repositorio
```

---

## 3. Estándar Institucional de Flags

Todas las flags del repositorio siguen estrictamente la estructura:

```text
DUOC{palabra_clave_XXXXX}
```

- **Expresión regular oficial:** `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$`
- **Composición:** Prefijo `DUOC{`, cierre `}`, texto en minúsculas separado por guiones bajos (`_`) que describe el hallazgo técnico interno del ejercicio y un bloque numérico aleatorio de 5 dígitos (o el identificador numérico deducible en desafíos OSINT).
- **Unicidad total:** Las **63 flags** del repositorio (57 de retos + 3 de plantillas OSINT + 3 señuelos Canary) son 100% únicas y sin colisiones.

---

## 4. Catálogo Completo de los 57 Desafíos por Categoría

### 4.1 Seguridad Web (15 desafíos)

| Desafío | Título | Servicio / Puerto | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `dating` | Dragon Dating | HTTP `8080` | Deserialización insegura en Java (`XMLDecoder`) en Tomcat | [README](dating/README.md) · [Solución](dating/solution/README.md) |
| `detector` | Dragon Detector | HTTP `80` | Inyección de comandos en PHP por validación únicamente en cliente (JS) | [README](detector/README.md) · [Solución](detector/solution/README.md) |
| `detector-2` | Dragon Detector 2 | HTTP `80` | Evasión de lista negra de caracteres mediante sustitución `$(...)` | [README](detector-2/README.md) · [Solución](detector-2/solution/README.md) |
| `evidence` | Dragon Evidence | HTTP `80` | Inyección de Entidades Externas XML (XXE) al procesar reportes | [README](evidence/README.md) · [Solución](evidence/solution/README.md) |
| `extinction` | Dragon Extinction | HTTP `80` | Evasión de filtro literal Base64 mediante maleabilidad de bits de relleno | [README](extinction/README.md) · [Solución](extinction/solution/README.md) |
| `go-git-it` | Go Git It | HTTP `80` | Exposición de repositorio `.git` (`/git/`) y recuperación de commits eliminados | [README](go-git-it/README.md) · [Solución](go-git-it/solution/README.md) |
| `hangman-one` | Hangman One | HTTP `8000` | Lógica de negocio: secreto estático compartido sin límite global entre cuentas | [README](hangman-one/README.md) · [Solución](hangman-one/solution/README.md) |
| `hangman-two` | Hangman Two | HTTP `8000` | Persistencia y reutilización cruzada de cookie de estado (`state`) | [README](hangman-two/README.md) · [Solución](hangman-two/solution/README.md) |
| `hangman-three` | Hangman Three | HTTP `8000` | Falsificación de token JWT tras ataque de diccionario sobre secreto HMAC débil | [README](hangman-three/README.md) · [Solución](hangman-three/solution/README.md) |
| `hidden-reports` | Hidden Reports | HTTP `80` | Inyección SQL clásica por tautología booleana en autenticación | [README](hidden-reports/README.md) · [Solución](hidden-reports/solution/README.md) |
| `hoard` | Dragon Hoard | HTTP `80` | Inyección de comandos en API JSON (`backend.php`) por escape de comillas | [README](hoard/README.md) · [Solución](hoard/solution/README.md) |
| `last` | NextPM | HTTP `3000` | Evasión de middleware en Next.js (`X-Middleware-Subrequest`) y descifrado de bóveda NaCl | [README](last/README.md) · [Solución](last/solution/README.md) |
| `moa-station` | MoA Station | HTTP `3003` | Explotación de extensión de Chrome mediante eventos de teclado DOM y callback JSONP | [README](moa-station/README.md) · [Solución](moa-station/solution/README.md) |
| `pathing` | Pathing | HTTP `4000` | Path Traversal directo en ruta HTTP sin normalización (`../`) | [README](pathing/README.md) · [Solución](pathing/solution/README.md) |
| `sighting` | Dragon Sighting | HTTP `80` | Inclusión Local de Archivos (LFI) en parámetro `picture.php?file=` | [README](sighting/README.md) · [Solución](sighting/solution/README.md) |
| `taxonomy` | Dragon Taxonomy | HTTP `80` | Inyección SQL con cierre de paréntesis para anular filtro `is_classified = 0` | [README](taxonomy/README.md) · [Solución](taxonomy/solution/README.md) |
| `web-tutorial-1` | Web Tutorial 1 | HTTP `8000` | Cross-Site Scripting (XSS) reflejado con política CSP `unsafe-inline` | [README](web-tutorial-1/README.md) · [Solución](web-tutorial-1/solution/README.md) |
| `web-tutorial-2` | Web Tutorial 2 | HTTP `8000` | Evasión de política CSP mediante dominios comodín en la nube (`*.us-central1.run.app`) | [README](web-tutorial-2/README.md) · [Solución](web-tutorial-2/solution/README.md) |
| `your-browser-hates-you` | Your Browser Hates You | HTTPS `443` | Inspección de servicio HTTPS con certificado X.509 autofirmado/inválido | [README](your-browser-hates-you/README.md) · [Solución](your-browser-hates-you/solution/README.md) |

### 4.2 Criptografía (11 desafíos)

| Desafío | Título | Servicio / Puerto | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `amd` | Advanced Machinecode Defense | TCP `8664` | Preimagen sobre AES-CMAC con clave conocida para forjar módulo RSA de firmware | [README](amd/README.md) · [Solución](amd/solution/README.md) |
| `arrow-of-time` | Arrow of Time | TCP `54321` | Detección de ciclos de Brent sobre MD5 truncado a 64 bits para invertir estado temporal | [README](arrow-of-time/README.md) · [Solución](arrow-of-time/solution/README.md) |
| `block-cipher` | Block Cipher | HTTP `55744` | Criptoanálisis de esquema visual de codificación en base mixta (5, 5, 7, 4, 4, 2, 4) | [README](block-cipher/README.md) · [Solución](block-cipher/solution/README.md) |
| `cipher-block-corruption` | Cipher Block Corruption | Offline | Descifrado AES-128-CBC sin IV y reconstrucción de cabecera PNG de 16 bytes | [README](cipher-block-corruption/README.md) · [Solución](cipher-block-corruption/solution/README.md) |
| `digital-citizen` | Digital Citizen 1 | TCP `6537` | Factorización RSA mediante Batch GCD y patrones de bits en RNG defectuoso | [README](digital-citizen/README.md) · [Solución](digital-citizen/solution/README.md) |
| `digital-citizen-2` | Digital Citizen 2 | TCP `6537` | Ataque de raíces pequeñas de Coppersmith sobre primos con patrones de bits parciales | [README](digital-citizen-2/README.md) · [Solución](digital-citizen-2/solution/README.md) |
| `dragon-spell` | Dragon Spell | Offline | Criptoanálisis de cifrado por sustitución monoalfabética con runas personalizadas | [README](dragon-spell/README.md) · [Solución](dragon-spell/solution/README.md) |
| `pascals-homomorphism` | Pascal's Homomorphism 1 | TCP `1999` | Criptosistema homomórfico de Paillier con factorización de módulo débil de 192 bits | [README](pascals-homomorphism/README.md) · [Solución](pascals-homomorphism/solution/README.md) |
| `pascals-homomorphism-2` | Pascal's Homomorphism 2 | TCP `1999` | Maleabilidad homomórfica aditiva en Paillier y factorización parcial frente a oráculo | [README](pascals-homomorphism-2/README.md) · [Solución](pascals-homomorphism-2/solution/README.md) |
| `qr-decomp` | QR Decomposition | Offline / On-Site | Descomposición matricial $M = Q \cdot R$ distribuida en fragmentos de códigos QR | [README](qr-decomp/README.md) · [Solución](qr-decomp/solution/README.md) |
| `subprime` | Subprime | Offline | Factorización de módulo RSA pequeño ($n = 98563159$) y descifrado ASCII carácter por carácter | [README](subprime/README.md) · [Solución](subprime/solution/README.md) |

### 4.3 Forense Digital y Esteganografía (8 desafíos)

| Desafío | Título | Modalidad | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `cardx` | CardX | HTTP `8000` | Decodificación de puntos amarillos de rastreo de impresora (Xerox DocuColor MIC) | [README](cardx/README.md) · [Solución](cardx/solution/README.md) |
| `extra-effed-system` | Extra Effed System | Offline | Recuperación forense de extents de inodo en sistema de archivos XFS corrupto (`xfs_db`) | [README](extra-effed-system/README.md) · [Solución](extra-effed-system/solution/README.md) |
| `magic` | Magic | Offline | Reparación de firma de cabecera (*magic bytes* `89 50 4E 47`) en archivo PNG | [README](magic/README.md) · [Solución](magic/solution/README.md) |
| `matryoshkafs` | MatryoshkaFS | Offline | Extracción forense de 16 capas anidadas de sistemas de archivos históricos y modernos | [README](matryoshkafs/README.md) · [Solución](matryoshkafs/solution/README.md) |
| `nearest-neighbor` | Nearest Neighbor | Offline | Esteganografía visual revelada mediante submuestreo con interpolación *nearest-neighbor* | [README](nearest-neighbor/README.md) · [Solución](nearest-neighbor/solution/README.md) |
| `ruthless-dot-flag` | Ruthless.flag 1 | Offline | Ingeniería inversa de formato gráfico propietario `.r16` (16-bit RGB555 little-endian) | [README](ruthless-dot-flag/README.md) · [Solución](ruthless-dot-flag/solution/README.md) |
| `ruthless-dot-flag-2` | Ruthless.flag 2 | Offline | Extracción esteganográfica de imagen oculta en el bit de canal alfa del archivo `.r16` | [README](ruthless-dot-flag-2/README.md) · [Solución](ruthless-dot-flag-2/solution/README.md) |
| `slackblock-steg` | SlackBlock Steg | HTTP `8888` | Datos binarios ocultos en píxeles de holgura (*slack space*) de bloques JPEG $8\times 8$ | [README](slackblock-steg/README.md) · [Solución](slackblock-steg/solution/README.md) |
| `tarnation` | Tarnation | Offline | Extracción de ocurrencias específicas (`--occurrence=2`) en archivos `.tar` concatenados | [README](tarnation/README.md) · [Solución](tarnation/solution/README.md) |
| `toothless` | Toothless | Offline | Análisis de captura `.pcap` para aislar paquete ICMP Echo Request huérfano con Base64 | [README](toothless/README.md) · [Solución](toothless/solution/README.md) |

### 4.4 Explotación de Binarios — Pwn (4 desafíos)

| Desafío | Título | Servicio / Puerto | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `acaan` | ACAAN | TCP `4113` | Primitiva de escritura arbitraria sobre `/proc/self/mem` para inyectar código tras `close@plt` | [README](acaan/README.md) · [Solución](acaan/solution/README.md) |
| `cert-tool` | Cert-Tool | TCP `6464` | Subdesbordamiento de puntero de bits (*buffer underflow*) al procesar relleno `=` en Base64 | [README](cert-tool/README.md) · [Solución](cert-tool/solution/README.md) |
| `drago-daction` | Drago-Daction | TCP `4445` | Desbordamiento de búfer en estructura para redirigir archivo de salida a `/proc/self/mem` | [README](drago-daction/README.md) · [Solución](drago-daction/solution/README.md) |
| `goto-zero` | Goto Zero | TCP `4445` | Cadena ROP en dos etapas: leak de `libc` vía GOT/PLT con retorno a `main()` y lectura de flag | [README](goto-zero/README.md) · [Solución](goto-zero/solution/README.md) |

### 4.5 Ingeniería Inversa — RE (4 desafíos)

| Desafío | Título | Servicio / Puerto | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `bug-me` | Bug Me | TCP `4445` | Antidepuración, checksum de `main()` y validación de caracteres por Teorema Chino del Resto | [README](bug-me/README.md) · [Solución](bug-me/solution/README.md) |
| `flag-search` | Flag Search | TCP `11010` | Algoritmo de búsqueda con retroceso (*backtracking*) sobre 28 restricciones de bits de clave AES | [README](flag-search/README.md) · [Solución](flag-search/solution/README.md) |
| `go-back` | Go Back | TCP `4445` | Oráculo de canal lateral basado en el código de salida (`exitstatus`) de `strcmp` | [README](go-back/README.md) · [Solución](go-back/solution/README.md) |
| `obscuratron` | Obscuratron | Offline | Inversión de algoritmo de cifrado XOR encadenado byte a byte sobre documento PDF | [README](obscuratron/README.md) · [Solución](obscuratron/solution/README.md) |

### 4.6 Inteligencia de Fuentes Abiertas — OSINT (2 desafíos + 3 plantillas)

| Desafío | Título | Modalidad | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `oh-the-places-youll-go` | Oh The Places You'll Go 1 | Offline | Geolocalización visual en Google Street View frente a 11 monumentos mundiales | [README](oh-the-places-youll-go/README.md) · [Solución](oh-the-places-youll-go/solution/README.md) |
| `oh-the-places-youll-go-2` | Oh The Places You'll Go 2 | Offline | Geolocalización avanzada por metadatos viales/regionales para deducir 48 dígitos de coordenadas | [README](oh-the-places-youll-go-2/README.md) · [Solución](oh-the-places-youll-go-2/solution/README.md) |

### 4.7 Seguridad Móvil — Android (2 desafíos)

| Desafío | Título | Servicio / Puerto | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `dragon-name` | Dragon Name | Offline (`.apk`) | Decompilación de APK con `apktool`, análisis de código Smali/Kotlin y recursos `strings.xml` | [README](dragon-name/README.md) · [Solución](dragon-name/solution/README.md) |
| `soothsayer` | Soothsayer | HTTP `8000` + APK | Predicción de generador Mersenne Twister en Firebase Firestore e instrumentación dinámica con Frida | [README](soothsayer/README.md) · [Solución](soothsayer/solution/README.md) |

### 4.8 Inteligencia Artificial / Machine Learning (1 desafío)

| Desafío | Título | Modalidad | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `oh-say-can-you-see` | Oh Say Can You See | Offline (`.keras`) | Ataque de inversión de modelo (*model inversion*) por descenso de gradiente en red Keras sobreajustada | [README](oh-say-can-you-see/README.md) · [Solución](oh-say-can-you-see/solution/README.md) |

### 4.9 Seguridad Física / On-Site y Misceláneos (4 desafíos)

| Desafío | Título | Modalidad | Concepto Técnico Principal | Documentación y Solución |
|---|---|---|---|---|
| `boxy` | Boxy | Presencial (On-Site) | Decodificación física no destructiva de cajas con cerradura de combinación | [README](boxy/README.md) · [Solución](boxy/solution/README.md) |
| `crossworthy` | Crossworthy | Offline (HTML/PNG) | Crucigrama técnico sobre conceptos de seguridad informática y vulnerabilidades | [README](crossworthy/README.md) · [Solución](crossworthy/solution/README.md) |
| `locky` | Locky | Presencial (On-Site) | Apertura práctica de cilindros de pines (*lockpicking*) en laboratorio | [README](locky/README.md) · [Solución](locky/solution/README.md) |
| `meow` | Meow | TCP `4445` | Desafío introductorio (101) de conexión a consola remota y lectura de archivos en Linux | [README](meow/README.md) · [Solución](meow/solution/README.md) |

---

## 5. Plantillas Reutilizables de OSINT (`templates/osint/`)

Se incluyen **3 plantillas modulares** listas para clonar y diseñar nuevos desafíos utilizando exclusivamente datos sintéticos y rangos reservados por estándares IETF (RFC 5737 / RFC 6996):

| Plantilla | Enfoque | Archivos Incluidos | Flag de Plantilla |
|---|---|---|---|
| [`templates/osint/osint_geografico/`](templates/osint/osint_geografico/README.md) | **OSINT Geográfico (GEOINT/IMINT):** Identificación de ubicaciones mediante metadatos EXIF, rumbo acimutal y referencias arquitectónicas. | `challenge.yml`, `metadata.yml`, `README.md`, `SOLUCION.md`, `evidencias/reporte_exif_captura.json`, `evidencias/bitacora_observacion_visual.txt` | `DUOC{muelle_prat_valparaiso_23801}` |
| [`templates/osint/osint_digital/`](templates/osint/osint_digital/README.md) | **OSINT Digital (Infraestructura/DNS):** Reconocimiento pasivo de zonas DNS, políticas SPF, registros Certificate Transparency (`spki_sha256`) y atribución RDAP/ASN. | `challenge.yml`, `metadata.yml`, `README.md`, `SOLUCION.md`, `evidencias/zona_dns_pasiva.txt`, `evidencias/transparencia_certificados.json`, `evidencias/registro_rdap_asn.txt` | `DUOC{nodo_respaldo_andino_64512}` |
| [`templates/osint/osint_investigativo/`](templates/osint/osint_investigativo/README.md) | **OSINT Investigativo (Cronologías):** Correlación temporal y pivoteo de entidades entre comunicados públicos, historiales de commits Git y actas de licitación. | `challenge.yml`, `metadata.yml`, `README.md`, `SOLUCION.md`, `evidencias/comunicado_prensa_2026.txt`, `evidencias/registro_commits_publicos.log`, `evidencias/acta_licitacion_abierta.csv` | `DUOC{operacion_faro_austral_84920}` |

---

## 6. Módulo Pasivo de Integridad Académica — Canary Tokens (`docs/` y `templates/canary_samples/`)

Implementa un sistema **100% pasivo y estático** de marcadores señuelo para evaluar si asistentes automatizados o herramientas de lectura distinguen correctamente entre evidencias legítimas y notas de control documental:

- **Registro aislado (fuera del puntaje del CTF):** [`docs/canary_registry.json`](docs/canary_registry.json)
- **Matriz y protocolo de evaluación:** [`docs/evaluacion_canary.md`](docs/evaluacion_canary.md)
- **Vectores implementados:**
  1. `CANARY-01` ([`templates/canary_samples/vector_1_html.html`](templates/canary_samples/vector_1_html.html)): `DUOC{canary_verificacion_contexto_html_71948}`
  2. `CANARY-02` ([`templates/canary_samples/vector_2_metadata.json`](templates/canary_samples/vector_2_metadata.json)): `DUOC{canary_registro_fuente_meta_53826}`
  3. `CANARY-03` ([`templates/canary_samples/vector_3_markdown.md`](templates/canary_samples/vector_3_markdown.md)): `DUOC{canary_control_documental_md_84273}`

---

## 7. Herramientas de Automatización y Auditoría (`tools/`)

- [`tools/update_flags.py`](tools/update_flags.py): Estandariza de forma determinista todas las flags en archivos `metadata.yml`, archivos de texto de retos, guías de solución y verificadores.
- [`tools/generate_docs_and_templates.py`](tools/generate_docs_and_templates.py): Genera y sincroniza los `README.md` pedagógicos en español y las guías `solution/README.md` de los 57 desafíos.
- [`tools/validate_repo.py`](tools/validate_repo.py): Ejecuta la auditoría integral de 7 puntos sobre todo el repositorio:
  ```bash
  python3 tools/validate_repo.py
  ```

---

## 8. Guía de Despliegue y Creación de Nuevos Desafíos

### Ejecutar un desafío existente con Docker
```bash
# Para desafíos con docker-compose.yml:
cd <nombre-del-reto>/challenge && docker compose up --build

# Para desafíos con Dockerfile estándar:
cd <nombre-del-reto>/challenge && docker build -t ctf-<reto> . && docker run --rm -it -P ctf-<reto>
```

### Crear un nuevo desafío a partir de una plantilla OSINT
```bash
cp -r templates/osint/osint_geografico nuevo-reto-osint
# 1. Reemplaza los archivos en nuevo-reto-osint/evidencias/
# 2. Actualiza la flag DUOC{...} en metadata.yml, challenge.yml, README.md y SOLUCION.md
# 3. Valida el repositorio completo:
python3 tools/validate_repo.py
```

---

## 9. Consideraciones de Seguridad y Uso Ético

Todos los materiales, contenedores, binarios y guías de este repositorio están diseñados exclusivamente para **docencia universitaria, entrenamiento defensivo y auditoría autorizada en entornos de laboratorio aislados**.
