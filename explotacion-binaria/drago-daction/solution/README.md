# Guía de Solución — `drago-daction` (Drago-Daction)

## Categoría
Pwn / Binarios

## Procedimiento de Resolución
El script `solution/solve.rb` ensambla `shellcode.asm`, calcula el desplazamiento de `__stack_chk_fail@plt` ajustado según la longitud de cadena y redirige la escritura hacia `/proc/self/mem` para recuperar la flag.

## Flag Esperada
```text
DUOC{desbordamiento_puntero_archivo_67391}
```
