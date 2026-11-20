`tarnation.tar.xz` es una cadena comprimida con XZ de archivos tar concatenados, lo cual es válido dentro de la especificación del formato tar.

Existen tres "revisiones" de la imagen de la flag, todas almacenadas con el nombre `.`. La ocurrencia central es la flag verdadera:

    $ tar -Jtiv -f tarnation.tar.xz
    -rw-r--r-- 1000/1000    173262 2025-04-15 18:26 drag_1.jpg
    -rw-r--r-- 1000/1000    173054 2025-04-15 18:26 drag_2.jpg
    -rw-r--r-- 1000/1000    173054 2025-04-15 18:26 drag_2.jpg
    -rw-r--r-- 1000/1000     64541 2025-04-15 18:19 .
    -rw-r--r-- 1000/1000     76418 2025-04-15 18:21 .
    -rw-r--r-- 1000/1000     64541 2025-04-15 18:19 .
    -rw-r--r-- 1000/1000    143056 2025-04-15 18:26 drag_3.jpg


Puedes extraer una ocurrencia específica del archivo (en este caso la segunda ocurrencia) redirigiendo a la salida estándar para evitar la colisión con el directorio actual `.`: `$ tar -Jiv -x '.' -f tarnation.tar.xz -O --occurrence=2 > flag.jpg`.

El tallado de archivos (*file carving*, por ejemplo con `binwalk` o `foremost`) también resuelve este desafío.

flag: DUOC{ocurrencia_archivo_concatenado_96284}
