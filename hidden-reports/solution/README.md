# Guía de Solución — `hidden-reports` (Hidden Reports)

## Categoría
Seguridad Web

## Procedimiento de Resolución
El archivo `challenge/app/index.php` interpola directamente `$_POST['passphrase']` en la consulta SQL sin parametrización. El script `solution/solve.rb` envía `test' or '1'='1` y verifica la obtención de la flag.

## Flag Esperada
```text
DUOC{tautologia_booleana_sql_47289}
```
