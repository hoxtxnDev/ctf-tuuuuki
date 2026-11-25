# Guía de Solución — `detector-2` (Dragon Detector 2)

## Categoría
Seguridad Web / Pwn

## Procedimiento de Resolución
El filtro en `detect-dragon.php` bloquea `;` pero permite paréntesis y `$`, posibilitando la sustitución de comandos `$(cat /app/dragon-detector-ai)`. El script `solution/solve.rb` automatiza la verificación.

## Flag Esperada
```text
DUOC{sustitucion_subshell_filtro_74832}
```
