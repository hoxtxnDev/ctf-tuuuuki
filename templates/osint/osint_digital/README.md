# Plantilla 2: Desafío de OSINT Digital — *Infraestructura en la Sombra*

> **Nota de plantilla:** Este directorio es una plantilla reutilizable para diseñar desafíos de reconocimiento pasivo de infraestructura digital (DNS, Certificate Transparency, RDAP/ASN) utilizando exclusivamente bloques IP reservados para documentación (RFC 5737) y dominios ficticios `.internal.edu`.

## 1. Nombre del desafío
**Infraestructura en la Sombra** (`plantilla-osint-digital`)

## 2. Descripción narrativa
Durante una auditoría de superficie externa sobre la organización ficticia *Andina Cloud Lab*, el equipo defensivo detectó que una dirección IP externa no documentada estaba autorizada para enviar correo en el registro SPF del dominio principal. Utilizando volcados pasivos de DNS, registros de transparencia de certificados (CT) y consultas RDAP, debes identificar el nombre del nodo de respaldo vinculado y el número de sistema autónomo (ASN) que lo aloja.

## 3. Nivel de dificultad
**Intermedio** (250 – 500 puntos / 1000 puntos en esquema dinámico)

## 4. Objetivos de aprendizaje
- Analizar registros DNS (`SOA`, `A`, `CNAME`, `TXT`/SPF) para descubrir activos vinculados fuera del dominio principal.
- Correlacionar certificados TLS en registros de Certificate Transparency mediante huellas `spki_sha256` y extensiones `Subject Alternative Name` (SAN).
- Consultar registros RDAP/WHOIS para atribuir direcciones IP a su Sistema Autónomo (`ASN`).

## 5. Contexto inicial para el participante
Cuentas con tres archivos de evidencia recolectados de fuentes abiertas pasivas. Identifica la etiqueta de host principal del servidor de contingencia (reemplazando guiones `-` por guiones bajos `_`) y el número de su ASN (solo los 5 dígitos numéricos sin el prefijo `AS`), entregando la flag con el formato `DUOC{<etiqueta_host>_<asn>}`.

## 6. Material y evidencias disponibles
- [`evidencias/zona_dns_pasiva.txt`](evidencias/zona_dns_pasiva.txt): Registros de resolución DNS pasiva del dominio auditado.
- [`evidencias/transparencia_certificados.json`](evidencias/transparencia_certificados.json): Registros de emisión de certificados X.509 y sus hashes SPKI.
- [`evidencias/registro_rdap_asn.txt`](evidencias/registro_rdap_asn.txt): Información de asignación de bloques IPv4 y Sistemas Autónomos.

## 7. Pistas progresivas
1. **Pista 1 (Análisis SPF y CNAME):** En `zona_dns_pasiva.txt`, el registro SPF autoriza la IP `203.0.113.88/32`. Verifica a qué nombre de host resuelve esa dirección IP.
2. **Pista 2 (Pivoteo por Certificado TLS):** En `transparencia_certificados.json`, comprueba qué certificado comparte exactamente el mismo hash de clave pública (`spki_sha256`) que `portal.andinacloud-lab.internal.edu`.
3. **Pista 3 (Atribución ASN):** Busca la IP `203.0.113.88` en `registro_rdap_asn.txt` para confirmar el nombre de host `nodo-respaldo-andino` y su sistema autónomo `AS64512`.

## 8. Flag esperada (Plantilla)
```text
DUOC{nodo_respaldo_andino_64512}
```

## 9. Solución detallada
Consulta el documento [`SOLUCION.md`](SOLUCION.md) para revisar la metodología completa de resolución y adaptación.

## 10. Criterios de validación
- La flag cumple la expresión regular `^DUOC\{[a-z0-9_]*[0-9]+[a-z0-9_]*\}$`.
- Todos los bloques IP utilizados (`198.51.100.0/24` y `203.0.113.0/24`) pertenecen a los rangos reservados para documentación por IETF RFC 5737 (`TEST-NET-2` y `TEST-NET-3`), y los ASN (`64501`, `64512`) pertenecen al rango de uso privado/documentación RFC 6996, garantizando que nunca apunten a infraestructura real de terceros.
