# Guía de Solución (Instructor) — Plantilla OSINT Digital

## 1. Nombre del desafío
**Infraestructura en la Sombra** (`plantilla-osint-digital`)

## 2. Metodología de resolución paso a paso

### Paso 1: Inspección de registros DNS y política SPF
En [`evidencias/zona_dns_pasiva.txt`](evidencias/zona_dns_pasiva.txt):
1. El registro `TXT` (SPF) de `andinacloud-lab.internal.edu` incluye una segunda dirección IP individual fuera de su subred primaria: `ip4:203.0.113.88/32`.
2. El subdominio `dr-sync.andinacloud-lab.internal.edu` apunta mediante un `CNAME` hacia `nodo-respaldo-andino.infra-sur.internal.edu`, el cual resuelve a `203.0.113.88`.

### Paso 2: Confirmación mediante Transparencia de Certificados (CT)
En [`evidencias/transparencia_certificados.json`](evidencias/transparencia_certificados.json):
- El certificado `CT-2026-9942` emitido para `nodo-respaldo-andino.infra-sur.internal.edu` incluye en su extensión SAN a `dr-sync.andinacloud-lab.internal.edu` y reutiliza exactamente la misma clave pública (`spki_sha256: e3b0c442...`) que el portal productivo.

### Paso 3: Atribución de Sistema Autónomo (ASN) en RDAP
En [`evidencias/registro_rdap_asn.txt`](evidencias/registro_rdap_asn.txt):
- El bloque `203.0.113.0/24` que aloja al host `203.0.113.88` pertenece al Sistema Autónomo `AS64512`.
- Normalizando la etiqueta del host (`nodo_respaldo_andino`) y el número del ASN (`64512`), se obtiene la flag.

## 3. Flag esperada (Plantilla)
```text
DUOC{nodo_respaldo_andino_64512}
```

## 4. Criterios de validación y adaptación para nuevos desafíos
- **Seguridad y ética:** Al modificar esta plantilla para nuevos escenarios, utiliza siempre rangos IP de documentación (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24` según RFC 5737) y ASN privados (`64512`–`65534` según RFC 6996).
- **Verificación:** La flag en `SOLUCION.md` coincide exactamente con `challenge.yml` y `metadata.yml`.
