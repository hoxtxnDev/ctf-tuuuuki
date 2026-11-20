# Guía de Solución — `bug-me` (Bug Me)

## Categoría
Ingeniería Inversa (RE)

## Procedimiento de Resolución
El script `challenge/src/embed.rb` genera para cada carácter tres congruencias ($c \bmod 5 = a$, $c \bmod 7 = b$, $c \bmod 11 = d$). Por el Teorema Chino del Resto en $\mathbb{Z}_{385}$, estas tres congruencias determinan de forma única el valor ASCII de cada carácter. El script `solution/solve.rb` verifica el binario.

## Flag Esperada
```text
DUOC{residuos_teorema_chino_62841}
```
