# Guía de Solución — `evidence` (Dragon Evidence)

## Categoría
Seguridad Web

## Procedimiento de Resolución
El servidor procesa el XML habilitando la sustitución de entidades externas (`LIBXML_NOENT`). El archivo `solution/payload.xml` y el script `solution/solve.rb` demuestran la extracción de `/flag.txt`.

## Flag Esperada
```text
DUOC{entidad_externa_xml_29483}
```
