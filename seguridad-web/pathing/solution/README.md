# Guía de Solución — `pathing` (Pathing)

## Categoría
Seguridad Web (101)

## Procedimiento de Resolución
El servidor web concatena la ruta de la solicitud HTTP sin filtrar `../`. El script `solution/solve.rb` realiza la petición con secuencias `../` y verifica la flag.

## Flag Esperada
```text
DUOC{navegacion_relativa_raiz_52683}
```
