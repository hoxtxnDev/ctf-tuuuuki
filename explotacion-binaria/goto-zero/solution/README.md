# Guía de Solución — `goto-zero` (Goto Zero)

## Categoría
Pwn / Binarios

## Procedimiento de Resolución
El script `solution/exploit_script.rb` (ejecutado remotamente por `solution/solve.rb`) realiza el ROP en dos fases: filtra la entrada GOT de `puts`, retorna a `main()`, calcula la base de `libc.so.6` y ejecuta `open`/`read`/`puts` sobre `/home/ctf/flag.txt`.

## Flag Esperada
```text
DUOC{cadena_rop_retorno_main_71538}
```
