# Guía de Solución — `obscuratron` (Obscuratron)

## Categoría
Ingeniería Inversa / Criptografía (101)

## Procedimiento de Resolución
El binario cifra cada byte como `c[i] = p[i] ^ key` y luego asigna `key = c[i]` (con valor inicial `key = 0xab`). El script `solution/solve.rb` invierte la operación (`p[i] = c[i] ^ key; key = c[i]`), verifica el hash SHA-256 contra `memo.pdf` y recupera el documento con la flag.

## Flag Esperada
```text
DUOC{flujo_xor_encadenado_94716}
```
