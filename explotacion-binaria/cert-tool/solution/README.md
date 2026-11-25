## `cert-tool` -- falla lógica en decodificación Base64 al manejar el carácter de relleno

`cert-tool` recibe un certificado TLS codificado en Base64 y lo procesa con OpenSSL para mostrar sus detalles (`openssl x509 -in /dev/stdin -inform DER -text -noout`).

El defecto lógico consiste en que, durante la decodificación Base64, la función lleva el seguimiento del desplazamiento en bits y, cada vez que encuentra un carácter de relleno `=`, resta 2 al desplazamiento de bits sin verificar que el carácter `=` aparezca únicamente al final de la cadena.

En memoria, el búfer de 128 bytes que almacena la cadena del comando precede inmediatamente al búfer de 4096 bytes donde se escribe la entrada decodificada. Al retroceder el puntero de bits en 128 bytes (enviando 512 caracteres `=`), la entrada Base64 subsiguiente se decodifica directamente encima de la cadena del comando ejecutado por `popen()`.

El script `solve.py` construye esta carga útil para leer `/home/ctf/flag.txt` (`DUOC{retroceso_relleno_base64_27465}`):

    ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================Y2F0IC9ob21lL2N0Zi9mbGFnLnR4dDsgI==j

La secuencia `[...]I==j` al final retrocede el puntero para evitar escribir más allá del byte deseado y no corromper el final de la cadena.

![solution in terminal](solved_term.png)
