# Desafío CTF: `toothless` — Toothless

## 1. Introducción
Captura de tráfico de red (`toothless.pcap`) con decenas de paquetes ICMP Echo Request y Echo Reply entre dos hosts.
- **Categoría:** Forense de Redes (101)

## 2. Objetivo
Utilizar herramientas de análisis de tráfico de red (Wireshark / `tshark`) para filtrar conversaciones ICMP e identificar paquetes anómalos sin respuesta que transportan datos exfiltrados.

## 3. Requisitos
- Wireshark, `tshark` o Python / `strings` + `base64`.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/toothless.pcap`.

## 5. Metodología de resolución
Filtrar los paquetes ICMP en `distfiles/toothless.pcap`, localizar la única solicitud ICMP Echo Request (secuencia 29) que carece de Echo Reply, extraer la cadena Base64 de su campo de datos y decodificarla.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `1000` puntos (configurado en `metadata.yml`).
- El desafío otorga el puntaje al validar la cadena de respuesta exacta en la plataforma del CTF.

## 7. Formato de flags
La flag de este desafío sigue el estándar institucional del laboratorio:
```text
DUOC{palabra_clave_XXXXX}
```

## 8. Consideraciones de seguridad
- Este ejercicio debe ejecutarse exclusivamente dentro del entorno de laboratorio aislado o sobre los archivos provistos en `distfiles/`.
- No utilices las técnicas estudiadas fuera de entornos educativos expresamente autorizados.

## 9. Créditos y referencias
- **Autor original:** `anshc`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
