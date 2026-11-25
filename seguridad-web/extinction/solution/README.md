# Guía de Solución — `extinction` (Dragon Extinction)

## Categoría
Seguridad Web / Criptografía

## Procedimiento de Resolución
En Base64, cuando el último grupo tiene un carácter `=` de relleno, los 2 bits menos significativos del tercer carácter no forman parte del byte decodificado. Enviar `encoded_creds=YWRtaW46YWRtaW5=` evade la comparación literal y decodifica a `admin:admin`.

## Flag Esperada
```text
DUOC{maleabilidad_bits_base64_57294}
```
