# Guía de Solución — `taxonomy` (Dragon Taxonomy)

## Categoría
Seguridad Web (101)

## Procedimiento de Resolución
La consulta en `challenge/app/index.php` tiene la forma `SELECT ... WHERE (name LIKE '%$search%' ...) AND is_classified = 0`. Al enviar `?search=Nano' OR 1=1) --` se cierra el paréntesis y se comenta el filtro de clasificación. El script `solution/solve.rb` automatiza la verificación.

## Flag Esperada
```text
DUOC{evasion_filtro_clasificado_24861}
```
