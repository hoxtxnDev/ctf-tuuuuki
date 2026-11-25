# Guía de Implementación para el Administrador del CTF (Panel CTFd y Despliegue de Retos)

Este documento explica paso a paso cómo cargar, configurar, desplegar y monitorear los desafíos del repositorio en la interfaz de administración de **CTFd**, tanto de forma manual desde el navegador como de forma automatizada mediante los scripts incluidos (`subir_uno.py` y `subir_archivos.py`).

---

## 1. Clasificación Operativa: Retos Offline vs. Retos con Contenedor Activo

Antes de cargar un reto en CTFd, identifica su modalidad en la tabla del [`README.md`](../README.md):

1. **Retos Offline (Solo archivos descargables en CTFd):**
   - No requieren levantar ningún servidor adicional.
   - El participante descarga los archivos de la carpeta `<categoria>/<reto>/distfiles/` directamente desde la tarjeta del desafío en CTFd y los analiza en su máquina para obtener la flag `DUOC{...}`.
   - **Ejemplos:** `criptografia/subprime`, `criptografia/cipher-block-corruption`, `criptografia/dragon-spell`, `forense-y-esteganografia/toothless`, `forense-y-esteganografia/magic`, `forense-y-esteganografia/nearest-neighbor`, `forense-y-esteganografia/ruthless-dot-flag`, `forense-y-esteganografia/tarnation`, `ingenieria-inversa/obscuratron`, `seguridad-movil/dragon-name`, `fisica-y-miscelaneos/crossworthy`.

2. **Retos con Servicio Activo (Docker HTTP / HTTPS / TCP):**
   - Requieren levantar su contenedor Docker en el servidor de desafíos (`challenge/`) y publicar un puerto (`-p <PUERTO_EXTERNO>:<PUERTO_INTERNO>`).
   - En la descripción del reto dentro de CTFd debes incluir la URL o el comando `nc <IP_SERVIDOR> <PUERTO_EXTERNO>` para que los participantes se conecten.
   - Si el reto además tiene archivos en `distfiles/` (por ejemplo, el binario ELF o el código fuente de referencia), también se suben a la sección **Files** de CTFd.

---

## 2. Cómo Cargar un Desafío Manualmente en la Interfaz Web de CTFd

1. Inicia sesión con tu cuenta de administrador en `http://<TU_IP_CTFD>/login`.
2. En la barra superior, haz clic en **Admin Panel** y dirígete a **Challenges** $\rightarrow$ botón **`+` (Create Challenge)** (`/admin/challenges/new`).
3. Selecciona el tipo **`standard`** y completa los campos tomando los datos de `<categoria>/<reto>/metadata.yml` y `<categoria>/<reto>/README.md`:
   - **Name:** Nombre del desafío (por ejemplo, `Hidden Reports` o `Subprime`).
   - **Category:** Categoría en español correspondente a su carpeta (`Seguridad Web`, `Criptografía`, `Forense y Esteganografía`, `Explotación Binaria`, `Ingeniería Inversa`, `OSINT`, `Seguridad Móvil`, `IA / Machine Learning` o `Misceláneo`).
   - **Message (Descripción para el jugador):**
     - Copia la introducción y el objetivo desde `<categoria>/<reto>/README.md` (nunca desde `solution/README.md`).
     - Recuerda indicar el formato esperado: `DUOC{palabra_clave_XXXXX}`.
     - Si es un reto con contenedor activo, agrega al final la dirección de conexión (por ejemplo: `http://<IP_SERVIDOR>:8081` o `nc <IP_SERVIDOR> 4113`).
   - **Value:** Puntaje del desafío (por ejemplo, `100`, `250`, `500` o el campo `value` de `metadata.yml`).
4. Haz clic en **Create**. Se abrirá la ventana modal de configuración de **Flags**, **Files** y **State**:
   - **Flag:**
     - Tipo: **`Static`** (Sensible a mayúsculas/minúsculas: **`Case Sensitive`**).
     - Contenido: Copia **exactamente** el valor del campo `flag:` de `<categoria>/<reto>/metadata.yml` (también listado en la sección 3.1 y sección 4 del [`README.md`](../README.md)).
   - **Files (Archivos Adjuntos):**
     - Sube todos los archivos que se encuentren dentro de `<categoria>/<reto>/distfiles/` (ignora el archivo vacío `.keep`).
     - **Importante:** Nunca subas archivos de la carpeta `challenge/` que contengan la flag en texto plano (como `flag.txt` o `dragons.db`), ni archivos de la carpeta `solution/`. Solo sube el contenido de `distfiles/`.
   - **State:**
     - Déjalo en **`Hidden`** mientras pruebas el reto y cámbialo a **`Visible`** cuando inicie la competencia.

---

## 3. Carga Automatizada mediante API de CTFd (`subir_uno.py` y `subir_archivos.py`)

El repositorio incluye dos scripts en la raíz para crear desafíos, registrar su flag `DUOC{...}` y adjuntar sus archivos `distfiles/*` automáticamente contra la API REST v1 de CTFd (`/api/v1/challenges`, `/api/v1/flags`, `/api/v1/files`):

### 3.1 Crear un desafío completo con flag y archivos ([`subir_uno.py`](../subir_uno.py))

1. Edita las constantes al inicio de [`subir_uno.py`](../subir_uno.py):
   ```python
   CTFD_URL = "http://192.168.100.121"  # URL de tu instancia CTFd
   USERNAME = "tu_usuario_admin"
   PASSWORD = "tu_password_admin"

   CARPETA = "criptografia/subprime"
   NOMBRE = "Subprime"
   CATEGORIA = "Criptografía"
   DESCRIPCION = "Factoriza la clave RSA para recuperar la flag en formato DUOC{...}."
   FLAG = "DUOC{exponente_privado_factorizado_51739}"
   ARCHIVOS = [f"{CARPETA}/distfiles/cipher.txt", f"{CARPETA}/distfiles/pubkeypair.txt"]
   VALOR = 100
   ```
2. Ejecuta:
   ```bash
   python3 subir_uno.py
   ```
   El script iniciará sesión en CTFd, obtendrá el `csrfNonce`, creará el reto en estado `hidden`, registrará la flag estática y subirá los archivos de `distfiles/`.

### 3.2 Subir archivos a un desafío ya existente ([`subir_archivos.py`](../subir_archivos.py))

Si ya creaste el desafío en la interfaz web de CTFd y solo quieres adjuntarle todos los archivos de su carpeta `distfiles/`:
1. Configura `CHALL_ID` (el ID numérico del reto en `/admin/challenges/<ID>`) y `CARPETA = "<categoria>/<reto>"` en [`subir_archivos.py`](../subir_archivos.py).
2. Ejecuta:
   ```bash
   python3 subir_archivos.py
   ```

---

## 4. Despliegue de Contenedores Docker para los Retos Activos

Para los desafíos que requieren un servicio en ejecución, entra a su carpeta `challenge/` y levántalos mapeando un puerto libre del host:

| Ruta del Desafío | Puerto Interno del Contenedor | Comando de Despliegue Recomendado en el Servidor | Archivos a subir en CTFd (`distfiles/`) |
|---|---|---|---|
| `seguridad-web/hidden-reports` | HTTP `80` | `cd seguridad-web/hidden-reports/challenge && docker build -t ctf-hidden-reports . && docker run -d --restart unless-stopped -p 8081:80 ctf-hidden-reports` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/taxonomy` | HTTP `80` | `cd seguridad-web/taxonomy/challenge && docker build -t ctf-taxonomy . && docker run -d --restart unless-stopped -p 8082:80 ctf-taxonomy` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/go-git-it` | HTTP `80` | `cd seguridad-web/go-git-it/challenge && docker compose up -d --build` (o `-p 8083:80`) | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/your-browser-hates-you` | HTTPS `443` | `cd seguridad-web/your-browser-hates-you/challenge && docker build -t ctf-ybhy . && docker run -d --restart unless-stopped -p 8443:443 ctf-ybhy` | *(Ninguno — reto de caja negra HTTPS)* |
| `seguridad-web/sighting` | HTTP `80` | `cd seguridad-web/sighting/challenge && docker build -t ctf-sighting . && docker run -d --restart unless-stopped -p 8084:80 ctf-sighting` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/pathing` | HTTP `4000` | `cd seguridad-web/pathing/challenge && docker build -t ctf-pathing . && docker run -d --restart unless-stopped -p 4000:4000 ctf-pathing` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/hangman-one` | HTTP `8000` | `cd seguridad-web/hangman-one/challenge && docker compose up -d --build` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/last` | HTTP `3000` | `cd seguridad-web/last/challenge && docker build -t ctf-last . && docker run -d --restart unless-stopped -p 3000:3000 ctf-last` | *(Ninguno — reto de caja negra web)* |
| `seguridad-web/detector` | HTTP `80` | `cd seguridad-web/detector/challenge && docker build -t ctf-detector . && docker run -d --restart unless-stopped -p 8085:80 ctf-detector` | `distfiles/index.php`, `distfiles/detect-dragon.php` |
| `seguridad-web/detector-2` | HTTP `80` | `cd seguridad-web/detector-2/challenge && docker build -t ctf-detector2 . && docker run -d --restart unless-stopped -p 8086:80 ctf-detector2` | `distfiles/index.php`, `distfiles/detect-dragon.php` |
| `seguridad-web/evidence` | HTTP `80` | `cd seguridad-web/evidence/challenge && docker build -t ctf-evidence . && docker run -d --restart unless-stopped -p 8087:80 ctf-evidence` | `distfiles/index.php` |
| `seguridad-web/extinction` | HTTP `80` | `cd seguridad-web/extinction/challenge && docker build -t ctf-extinction . && docker run -d --restart unless-stopped -p 8088:80 ctf-extinction` | `distfiles/index.php` |
| `seguridad-web/hoard` | HTTP `80` | `cd seguridad-web/hoard/challenge && docker build -t ctf-hoard . && docker run -d --restart unless-stopped -p 8089:80 ctf-hoard` | `distfiles/backend.php` |
| `criptografia/block-cipher` | HTTP `55744` | `cd criptografia/block-cipher/challenge && docker build -t ctf-block-cipher . && docker run -d --restart unless-stopped -p 55744:55744 ctf-block-cipher` | `distfiles/flag.png` |
| `forense-y-esteganografia/slackblock-steg` | HTTP `8888` | `cd forense-y-esteganografia/slackblock-steg/challenge && docker build -t ctf-slackblock . && docker run -d --restart unless-stopped -p 8888:8888 ctf-slackblock` | `distfiles/flag.jpg` |
| `ingenieria-inversa/bug-me` | Offline / Binario ELF | *(No requiere servidor si se entrega el binario ELF; o TCP `4445` con Docker)* | `distfiles/bug-me` |
| `ingenieria-inversa/flag-search` | TCP `11010` | `cd ingenieria-inversa/flag-search/challenge && docker build -t ctf-flag-search . && docker run -d --restart unless-stopped -p 11010:11010 ctf-flag-search` | `distfiles/flag-search` |

---

## 5. Monitoreo de Honeypots y Flags Señuelo Anti-IA en CTFd

Durante la competencia, puedes abrir en CTFd la vista **Admin Panel $\rightarrow$ Submissions $\rightarrow$ Incorrect** (`/admin/submissions?type=incorrect`) para monitorear si algún participante o agente automatizado activó los honeypots:

### 5.1 Flags Señuelo de Honeypots Criptográficos Camuflados (Exclusivos para CLI / Scrapers / IA)
Estos strings **no existen en texto plano** en ningún archivo del repositorio y **se autodestruyen en navegadores gráficos reales**; solo pueden obtenerse si un participante o su agente de IA descarga el HTML crudo por CLI (`curl`) e invierte la ecuación modular del honeypot JavaScript:

| Flag Señuelo Recibida en CTFd | Reto de Origen | Cómo se generó |
|---|---|---|
| `DUOC{x509_tls_session_cipher_suite_71948}` | `seguridad-web/your-browser-hates-you` | El agente invirtió `verifyTlsCertPin(49157)` del HTML crudo e ignoró la flag real visible en pantalla (`DUOC{omision_certificado_autofirmado_37614}`). |
| `DUOC{git_packfile_delta_reflog_84273}` | `seguridad-web/go-git-it` | El agente invirtió `verifyPackRevision(38419)` del HTML crudo en lugar de inspeccionar el commit inicial de `/git/`. |
| `DUOC{uri_unescape_posix_realpath_53826}` | `seguridad-web/pathing` | El agente invirtió `verifyVfsRouteToken(52913)` del HTML crudo en lugar de solicitar `/../flag.txt`. |

### 5.2 Tarpits Activos y Homógrafos Cirílicos en Logs HTTP de Nginx
En los contenedores de `hidden-reports`, `taxonomy` y `sighting`, puedes inspeccionar los logs con `docker logs <contenedor>`:
- **Peticiones a `/?wal_frame=...`, `/?schema_shard=...` o `/?exif_shard=...`:** Indican que un agente automatizado siguió el comentario `TODO(dba)` (invisible para navegadores humanos gracias al filtro `Sec-Fetch-Mode: navigate`) y quedó atrapado recibiendo páginas JSON a `4 KB/s` (`limit_rate 4k` en Nginx, sin consumir *workers* de PHP-FPM).
- **Peticiones con `%D0%B0` (`а` cirílica) o `%D1%96` (`і` cirílica) en `drаgonwаtch`, `Drаgon-000` o `pіcture.php`:** Indican que el participante o su IA copió literalmente el identificador desde el comentario señuelo de CLI/portapapeles.
