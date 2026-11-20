# Toothless

La idea detrás del desafío es parecer intimidante a primera vista pero resultar directo al inspeccionar las anomalías del tráfico.

Al explorar el archivo PCAP (`toothless.pcap`), observarás una gran cantidad de solicitudes y respuestas ICMP Echo repetidas entre las mismas direcciones IP.
Sin embargo, existe exactamente una solicitud ICMP Echo Request que no tiene respuesta. Ese paquete contiene una cadena codificada en Base64 dentro de su carga útil de datos.
Al decodificar la cadena Base64 se obtiene la flag (`DUOC{carga_icmp_huerfana_68352}`).
