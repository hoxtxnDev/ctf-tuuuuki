# Guía de Solución — `sighting` (Dragon Sighting)

## Categoría
Seguridad Web (101)

## Procedimiento de Resolución
El script `picture.php` lee el archivo indicado en el parámetro GET `file` sin sanitizar `../`. El verificador `solution/solve.rb` recupera `/flag.txt` y comprueba la flag.

## Flag Esperada
```text
DUOC{inclusion_archivo_local_46197}
```
