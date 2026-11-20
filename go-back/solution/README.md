# Guía de Solución — `go-back` (Go Back)

## Categoría
Misceláneo / Ingeniería Inversa

## Procedimiento de Resolución
El binario devuelve el signo de la diferencia entre el carácter probado y el carácter real de la flag mediante su código de salida (`exitstatus`). Los scripts `solution/solve.rb` y `solution/solve-internal.rb` automatizan la extracción carácter por carácter.

## Flag Esperada
```text
DUOC{oraculo_codigo_retorno_83715}
```
