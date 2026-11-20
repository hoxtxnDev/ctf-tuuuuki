# Guía de Solución — `acaan` (ACAAN (Any Code At Any Offset))

## Categoría
Pwn / Binarios

## Procedimiento de Resolución
El servicio abre la ruta indicada y escribe en el desplazamiento numérico proporcionado antes de invocar `close()`. Al especificar `/proc/self/mem` y el offset de la instrucción posterior a `call close@plt`, el proceso sobrescribe su propio segmento `.text` en memoria y ejecuta las instrucciones que leen `/flag.txt`. Se incluye el verificador automatizado `solve.rb`.

## Flag Esperada
```text
DUOC{escritura_memoria_proc_48291}
```
