# Guía de Solución — `hoard` (Dragon Hoard)

## Categoría
Seguridad Web / Pwn

## Procedimiento de Resolución
El endpoint `backend.php` pasa el campo `artifacts` del JSON a un comando de shell entre comillas simples sin usar `escapeshellarg()` ni convertirlo a entero. El script `solution/solve.rb` automatiza la prueba.

## Flag Esperada
```text
DUOC{escape_comillas_parametro_69145}
```
