# Guía de Solución — `last` (NextPM)

## Categoría
Seguridad Web / Criptografía

## Procedimiento de Resolución
El script `solution/solve.py` explota la evasión de middleware en Next.js enviando la cabecera `X-Middleware-Subrequest` a `/api/users` y `/api/keybag/bingo`, recupera la contraseña del usuario `bingo` (`banditthedog`) a partir de su hash bcrypt y deriva la clave Argon2id para abrir el `SecretBox` de NaCl donde se almacena la entrada `flag`.

## Flag Esperada
```text
DUOC{cabecera_subrequest_interna_82537}
```
