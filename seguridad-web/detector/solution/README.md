# Guía de Solución — `detector` (Dragon Detector)

## Categoría
Seguridad Web / Pwn

## Procedimiento de Resolución
El script `detect-dragon.php` concatena el parámetro `ip` directamente en una llamada al sistema sin filtrado en servidor. El verificador `solution/solve.rb` comprueba la obtención de la flag desde `/app/dragon-detector-ai`.

## Flag Esperada
```text
DUOC{inyeccion_consola_directa_19574}
```
