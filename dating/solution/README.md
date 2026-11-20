# Guía de Solución — `dating` (Dragon Dating)

## Categoría
Seguridad Web / Pwn

## Procedimiento de Resolución
El endpoint `/ProfileServlet` procesa directamente la entrada XML con `java.beans.XMLDecoder`. El script de verificación `solution/solve.rb` valida la lectura de `/flag.txt` y limpia el archivo temporal creado.

## Flag Esperada
```text
DUOC{deserializacion_xmldecoder_86429}
```
