#!/usr/bin/env python3
"""
Generador de documentación pedagógica en español (Fase 1B y Fase 2):
1. Genera solution/README.md en español para los desafíos que carecían de archivo Markdown en solution/,
   asegurando que los 57 desafíos documenten su procedimiento y citen exactamente su flag DUOC{...}.
2. Genera/actualiza el README.md de cada uno de los 57 desafíos con las 9 secciones obligatorias.
3. Genera el README.md general en la raíz del repositorio.
"""

import os
import re
from tools.update_flags import FLAG_MAPPING

# Metadatos pedagógicos en español para cada uno de los 57 desafíos
CHALLENGE_DOCS = {
    "acaan": {
        "cat": "Pwn / Binarios",
        "title": "ACAAN (Any Code At Any Offset)",
        "intro": "Servicio de red en C que permite abrir cualquier archivo accesible por el proceso y sobrescribir bytes en un desplazamiento arbitrario.",
        "obj": "Comprender cómo funciona el sistema de archivos virtual `/proc/self/mem` en Linux y cómo una escritura arbitraria sobre descriptores de archivo permite modificar páginas de código ejecutable en memoria.",
        "req": "Cliente TCP (`netcat`), Ruby (`socket`), `objdump` y `nasm` (o Docker para ejecutar el contenedor).",
        "meth": "Analizar el binario desensamblado para localizar la llamada a `close@plt`, calcular el desplazamiento de la instrucción siguiente e indicar `/proc/self/mem` como archivo destino para escribir código de lectura de `/flag.txt`.",
        "sol": "El servicio abre la ruta indicada y escribe en el desplazamiento numérico proporcionado antes de invocar `close()`. Al especificar `/proc/self/mem` y el offset de la instrucción posterior a `call close@plt`, el proceso sobrescribe su propio segmento `.text` en memoria y ejecuta las instrucciones que leen `/flag.txt`. Se incluye el verificador automatizado `solve.rb`.",
    },
    "amd": {
        "cat": "Criptografía / Pwn",
        "title": "Advanced Machinecode Defense",
        "intro": "Utilidad de actualización de firmware que valida la clave pública RSA mediante AES-CMAC con una clave simétrica conocida antes de verificar la firma del código.",
        "obj": "Analizar por qué un código de autenticación de mensajes simétrico (AES-CMAC) cuya clave está embebida no proporciona resistencia a preimagen y permite forjar un módulo RSA válido.",
        "req": "Python 3 (`pycryptodome`, `sympy`), `nasm` y `netcat`.",
        "meth": "Invertir los últimos bloques de AES-CMAC en `aes_cmac.py` para construir un módulo de 2048 bits que produzca el CMAC esperado y sea fácilmente factorizable, permitiendo firmar una actualización con `build_forged_blob.py`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "arrow-of-time": {
        "cat": "Criptografía",
        "title": "Arrow of Time",
        "intro": "Reloj criptográfico cuyo estado interno de 64 bits avanza cada segundo aplicando MD5 truncado a 8 bytes, acompañado de un video con marcas de tiempo futuras.",
        "obj": "Aplicar algoritmos de detección de ciclos (algoritmo de Brent) sobre funciones iteradas de espacio finito para retroceder estados dentro de un ciclo periódico.",
        "req": "Compilador C (`gcc`), biblioteca OpenSSL (`libcrypto`), Python 3 y `netcat`.",
        "meth": "Determinar la longitud del ciclo $\\lambda$ del hash MD5 truncado a 64 bits utilizando el algoritmo de Brent (`md5_brent.c`) y avanzar $(\\lambda - (t_{\\text{futuro}} - t_{\\text{actual}})) \\bmod \\lambda$ pasos desde el estado conocido.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "block-cipher": {
        "cat": "Criptografía",
        "title": "Block Cipher",
        "intro": "Servicio web de codificación visual que transforma bloques de tres letras en imágenes compuestas por sub-bloques geométricos y rotaciones según una clave numérica.",
        "obj": "Analizar esquemas de codificación en base mixta y criptoanálisis por texto plano elegido (CPA) mediante inspección de patrones visuales.",
        "req": "Python 3, navegador web o cliente HTTP.",
        "meth": "Enviar entradas de prueba al codificador para identificar la secuencia de símbolos (bases 5, 5 y 7) y las rotaciones (bases 4, 4, 2 y 4), deducir la permutación de la clave y decodificar los bloques de `distfiles/flag.png`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "boxy": {
        "cat": "Seguridad Física (On-Site)",
        "title": "Boxy",
        "intro": "Desafío presencial compuesto por dos cajas de seguridad idénticas (Boxy A y Boxy B) con cerradura de combinación.",
        "obj": "Aplicar técnicas de observación y decodificación mecánica no destructiva sobre cerraduras de combinación en entorno de laboratorio.",
        "req": "Acceso presencial a las cajas de práctica del laboratorio educativo.",
        "meth": "Inspeccionar las holguras mecánicas de los discos de combinación para identificar la secuencia de apertura y recuperar la tarjeta interna.",
        "sol": "Al decodificar la combinación de las cajas de práctica presenciales Boxy A / Boxy B en el área del laboratorio se obtiene la flag configurada.",
    },
    "bug-me": {
        "cat": "Ingeniería Inversa (RE)",
        "title": "Bug Me",
        "intro": "Binario ELF de Linux que implementa mecanismos antidepuración, verificación de suma de comprobación sobre `main()` y validación carácter por carácter mediante residuos modulares.",
        "obj": "Identificar rutinas de verificación de integridad y resolver sistemas de congruencias basados en el Teorema Chino del Resto (CRT) en binarios compilados.",
        "req": "Desensamblador/descompilador (`Ghidra`, `IDA` o `objdump`), Ruby y entorno Linux x86_64.",
        "meth": "Localizar las funciones `match(char c)` añadidas al final del binario, extraer las tres condiciones modulares ($c \\bmod 5$, $c \\bmod 7$, $c \\bmod 11$) para cada posición y reconstruir el carácter ASCII único que las satisface.",
        "sol": "El script `challenge/src/embed.rb` genera para cada carácter tres congruencias ($c \\bmod 5 = a$, $c \\bmod 7 = b$, $c \\bmod 11 = d$). Por el Teorema Chino del Resto en $\\mathbb{Z}_{385}$, estas tres congruencias determinan de forma única el valor ASCII de cada carácter. El script `solution/solve.rb` verifica el binario.",
    },
    "cardx": {
        "cat": "Forense Digital",
        "title": "CardX",
        "intro": "Galería web de 29 cartas coleccionables de alta resolución que contienen patrones esteganográficos de puntos amarillos de impresora.",
        "obj": "Analizar códigos de identificación de máquina (MIC / Xerox DocuColor tracking dots) en el canal azul de imágenes digitales para autenticar documentos y extraer metadatos de fecha y hora.",
        "req": "Visor/editor de imágenes con separación de canales RGB (GIMP, ImageMagick o Python Pillow).",
        "meth": "Aislar el canal azul de cada imagen `.webp`, decodificar la matriz de 15x8 puntos según el estándar Xerox DocuColor, descartar las cartas impresas en 2024 y ordenar cronológicamente por minuto de impresión las cartas auténticas de 1998.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "cert-tool": {
        "cat": "Pwn / Binarios",
        "title": "Cert-Tool",
        "intro": "Herramienta de inspección de certificados TLS en Base64 que invoca a OpenSSL internamente tras decodificar la entrada en un búfer contiguo al comando.",
        "obj": "Identificar vulnerabilidades de subdesbordamiento de índice (*buffer underflow*) causadas por el manejo incorrecto de caracteres de relleno (`=`) en decodificadores Base64 personalizados.",
        "req": "Python 3 y `netcat`.",
        "meth": "Revisar la función de decodificación Base64 para observar que cada carácter `=` resta 2 bits al desplazamiento actual, permitiendo retroceder 128 bytes (512 signos `=`) y sobrescribir el búfer del comando ejecutado por el servidor.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "cipher-block-corruption": {
        "cat": "Criptografía",
        "title": "Cipher Block Corruption",
        "intro": "Imagen PNG cifrada mediante AES-128 en modo CBC utilizando una clave conocida pero un vector de inicialización (IV) aleatorio no registrado.",
        "obj": "Comprender la propiedad de propagación limitada de errores en el descifrado AES-CBC y cómo restaurar el primer bloque a partir de cabeceras de formato conocidas.",
        "req": "Python 3 con `pycryptodome`.",
        "meth": "Descifrar el archivo `distfiles/flag.png.enc` en modo AES-CBC con un IV nulo y reemplazar los primeros 16 bytes corruptos por los 16 bytes estándar de la cabecera PNG (`\\x89PNG...IHDR`).",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "crossworthy": {
        "cat": "Misceláneo",
        "title": "Crossworthy",
        "intro": "Crucigrama temático de ciberseguridad distribuido en formatos HTML interactivo y PNG.",
        "obj": "Reforzar terminología técnica de seguridad informática, cultura hacker y vulnerabilidades mediante la resolución de pistas cruzadas.",
        "req": "Navegador web o visor de imágenes.",
        "meth": "Resolver las pistas horizontales y verticales del crucigrama en `distfiles/crossworthy2025.html` hasta completar la casilla 66 horizontal (66 Across) y envolver el término en el formato de flag.",
        "sol": "Al completar el crucigrama (`crossworthy2025.txt`), la entrada 66 horizontal corresponde al concepto de programa de recompensas por vulnerabilidades (*bug bounty*).",
    },
    "dating": {
        "cat": "Seguridad Web / Pwn",
        "title": "Dragon Dating",
        "intro": "Aplicación web en Java/Tomcat que permite exportar e importar perfiles de usuario serializados en formato XML.",
        "obj": "Comprender los riesgos de deserialización insegura mediante `java.beans.XMLDecoder` y cómo prevenir la ejecución remota de código validando esquemas XML.",
        "req": "Ruby (`httparty`, `uuid`) o cliente HTTP (`curl`).",
        "meth": "Inspeccionar el formato XML de los perfiles en `ProfileServlet`, identificar el uso de `XMLDecoder` y construir un documento XML que invoque un comando para leer `/flag.txt`.",
        "sol": "El endpoint `/ProfileServlet` procesa directamente la entrada XML con `java.beans.XMLDecoder`. El script de verificación `solution/solve.rb` valida la lectura de `/flag.txt` y limpia el archivo temporal creado.",
    },
    "detector": {
        "cat": "Seguridad Web / Pwn",
        "title": "Dragon Detector",
        "intro": "Herramienta web en PHP para diagnóstico de red que bloquea caracteres especiales únicamente mediante validación JavaScript en el navegador.",
        "obj": "Demostrar por qué los controles de validación del lado del cliente no sustituyen la sanitización y parametrización en el servidor.",
        "req": "Cliente HTTP (`curl`, navegador o Ruby con `httparty`).",
        "meth": "Enviar la solicitud HTTP directamente al endpoint `detect-dragon.php` omitiendo la validación JavaScript del formulario para concatenar la lectura del archivo `/app/dragon-detector-ai`.",
        "sol": "El script `detect-dragon.php` concatena el parámetro `ip` directamente en una llamada al sistema sin filtrado en servidor. El verificador `solution/solve.rb` comprueba la obtención de la flag desde `/app/dragon-detector-ai`.",
    },
    "detector-2": {
        "cat": "Seguridad Web / Pwn",
        "title": "Dragon Detector 2",
        "intro": "Segunda versión de la herramienta web de diagnóstico que incorpora una lista negra parcial de caracteres en el servidor PHP.",
        "obj": "Analizar las limitaciones de las listas negras de caracteres (*blacklisting*) frente a mecanismos de sustitución de subshell y por qué debe usarse `escapeshellarg()` o APIs nativas.",
        "req": "Cliente HTTP (`curl`, navegador o Ruby con `httparty`).",
        "meth": "Revisar `distfiles/detect-dragon.php` para identificar qué metacaracteres fueron bloqueados (como `;`, `&`, `|`) y cuáles permanecen permitidos (como la sustitución `$(...)`) para leer `/app/dragon-detector-ai`.",
        "sol": "El filtro en `detect-dragon.php` bloquea `;` pero permite paréntesis y `$`, posibilitando la sustitución de comandos `$(cat /app/dragon-detector-ai)`. El script `solution/solve.rb` automatiza la verificación.",
    },
    "digital-citizen": {
        "cat": "Criptografía",
        "title": "Digital Citizen 1",
        "intro": "Servicio de registro de claves públicas RSA que emula un defecto real de generación de números primos con patrones repetitivos de bits en tarjetas inteligentes.",
        "obj": "Aplicar técnicas de factorización por máximo común divisor por lotes (*Batch GCD*) y análisis de patrones binarios para auditar generadores de números aleatorios defectuosos.",
        "req": "Python 3 (`sympy`) y `netcat`.",
        "meth": "Recolectar módulos RSA generados con la opción de hardware RNG, calcular el MCD entre pares con `gcd_mods.py`, deducir la estructura periódica de bits y factorizar la clave del Ciudadano 0 con `generate_all_pattern_primes.py` y `trial_division.py`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "digital-citizen-2": {
        "cat": "Criptografía",
        "title": "Digital Citizen 2",
        "intro": "Segunda parte del desafío `digital-citizen` (utiliza el mismo servicio en el puerto 6537), enfocada en la clave del Ciudadano 1 cuyos primos contienen 48 bits aleatorios adicionales.",
        "obj": "Comprender y aplicar el método de raíces pequeñas de Coppersmith (`small_roots`) en SageMath para factorizar módulos RSA cuando se conocen las partes altas del factor primo.",
        "req": "SageMath, Python 3 y `netcat`.",
        "meth": "Utilizar la lista de primos candidatos generados por patrón como aproximación de los bits superiores y ejecutar el método de Coppersmith (`trial_coppersmith.sage`) para recuperar los 64 bits inferiores desconocidos de la clave del Ciudadano 1.",
        "sol": "Consulte el procedimiento detallado para la Parte 2 en `digital-citizen/solution/README.md`.",
    },
    "drago-daction": {
        "cat": "Pwn / Binarios",
        "title": "Drago-Daction",
        "intro": "Utilidad en C con permisos elevados que redacta la palabra 'dragon' en archivos de texto, pero presenta un desbordamiento de búfer sobre punteros de estructura.",
        "obj": "Analizar desbordamientos de búfer basados en funciones de cadena (`strlen`/`strcpy`) que permiten redirigir el archivo de salida hacia `/proc/self/mem`.",
        "req": "Ruby, `nasm`, `objdump` y `netcat`.",
        "meth": "Construir una cadena de reemplazo de 128 bytes que sobrescriba el puntero de nombre de archivo de salida por `/proc/self/mem` y el desplazamiento hacia `__stack_chk_fail@plt` para ejecutar la lectura de `/flag.txt`.",
        "sol": "El script `solution/solve.rb` ensambla `shellcode.asm`, calcula el desplazamiento de `__stack_chk_fail@plt` ajustado según la longitud de cadena y redirige la escritura hacia `/proc/self/mem` para recuperar la flag.",
    },
    "dragon-name": {
        "cat": "Seguridad Móvil (Android)",
        "title": "Dragon Name",
        "intro": "Aplicación Android (`dragon-name.apk`) que construye dinámicamente la flag en memoria al pulsar un botón pero no la muestra en pantalla.",
        "obj": "Practicar ingeniería inversa estática de paquetes APK de Android utilizando `apktool` o Android Studio para analizar bytecode Smali/Kotlin y recursos `strings.xml`.",
        "req": "Java y `apktool` (o `jadx` / Android Studio).",
        "meth": "Desempaquetar `distfiles/dragon-name.apk`, localizar el método `createFlag()` en `MainActivity`, decodificar las transformaciones ROT13 y Base64 y recuperar el recurso `R.string.part4` desde `res/values/strings.xml`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "dragon-spell": {
        "cat": "Criptografía",
        "title": "Dragon Spell",
        "intro": "Pergamino ilustrado (`dragon-spell.png`) escrito con un alfabeto rúnico personalizado que oculta un conjuro en inglés y la flag al final.",
        "obj": "Aplicar análisis de frecuencias y reconocimiento de patrones léxicos para resolver un cifrado por sustitución monoalfabética.",
        "req": "Visor de imágenes y bloc de notas.",
        "meth": "Aprovechar las llaves `{` y `}` sin cifrar al final del texto para identificar las letras iniciales del formato de flag y utilizar palabras cortas frecuentes (`a`, `I`, `the`, `and`) para completar el alfabeto rúnico.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "evidence": {
        "cat": "Seguridad Web",
        "title": "Dragon Evidence",
        "intro": "Portal web en PHP que recibe archivos XML con reportes de avistamientos y expande entidades externas al procesarlos.",
        "obj": "Comprender las vulnerabilidades de Entidades Externas XML (XXE) y cómo deshabilitar la carga de DTDs externas en analizadores XML.",
        "req": "Cliente HTTP (`curl`, navegador o Ruby con `httparty`).",
        "meth": "Declarar una entidad externa `<!ENTITY xxe SYSTEM \"file:///flag.txt\">` dentro del bloque `<!DOCTYPE>` del archivo XML subido y referenciarla como `&xxe;` dentro de la etiqueta `<proof>`.",
        "sol": "El servidor procesa el XML habilitando la sustitución de entidades externas (`LIBXML_NOENT`). El archivo `solution/payload.xml` y el script `solution/solve.rb` demuestran la extracción de `/flag.txt`.",
    },
    "extinction": {
        "cat": "Seguridad Web / Criptografía",
        "title": "Dragon Extinction",
        "intro": "Panel de autenticación en PHP que recibe credenciales en Base64 (`encoded_creds`), bloquea la cadena exacta `YWRtaW46YWRtaW4=` antes de decodificar y luego verifica si el resultado decodificado es `admin:admin`.",
        "obj": "Comprender la maleabilidad de los bits de relleno (*padding bits*) en la codificación Base64 cuando se compara la cadena codificada en lugar del valor decodificado canónico.",
        "req": "Cliente HTTP (`curl` o Ruby con `httparty`).",
        "meth": "Modificar el último carácter antes del signo `=` en `YWRtaW46YWRtaW4=` alterando únicamente los 2 bits inferiores de relleno (por ejemplo, `YWRtaW46YWRtaW5=`), de modo que la cadena Base64 sea distinta pero decodifique exactamente a `admin:admin`.",
        "sol": "En Base64, cuando el último grupo tiene un carácter `=` de relleno, los 2 bits menos significativos del tercer carácter no forman parte del byte decodificado. Enviar `encoded_creds=YWRtaW46YWRtaW5=` evade la comparación literal y decodifica a `admin:admin`.",
    },
    "extra-effed-system": {
        "cat": "Forense Digital",
        "title": "Extra Effed System",
        "intro": "Imagen de disco comprimida (`exefs.bin.xz`) que contiene un sistema de archivos XFS con metadatos de inodos corruptos.",
        "obj": "Utilizar herramientas de diagnóstico forense de sistemas de archivos (`xfs_db`, `xfs_repair` y `dd`) para localizar extents de datos y reconstruir archivos fragmentados.",
        "req": "Herramientas `xz`, `xfsprogs` (`xfs_db` / `xfs_repair`) y `dd`.",
        "meth": "Descomprimir `exefs.bin.xz`, consultar los bloques de datos asignados al inodo de `/flag.jpg` mediante `xfs_db -c 'path /flag.jpg' -c 'print'` y extraer los dos extents con `dd` (`bs=4k`).",
        "sol": "Consulte el procedimiento detallado en `solution/solution.txt`.",
    },
    "flag-search": {
        "cat": "Ingeniería Inversa (RE)",
        "title": "Flag Search",
        "intro": "Binario interactivo que valida una clave hexadecimal de 128 bits mediante 28 comprobaciones incrementales antes de usarla para descifrar la flag con AES-128-ECB.",
        "obj": "Modelar restricciones sobre prefijos de bits extraídas de un binario desensamblado e implementar un algoritmo de búsqueda con retroceso (*backtracking*) para recuperar claves criptográficas.",
        "req": "Python 3, desensamblador (`Ghidra` / `objdump`) y `netcat`.",
        "meth": "Extraer las condiciones del switch sobre la longitud de bits $i \\in [4, 128]$ en la función de validación e implementar una búsqueda recursiva en profundidad (`solve_search.py`) que pode las ramas que incumplan cada condición.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "go-back": {
        "cat": "Misceláneo / Ingeniería Inversa",
        "title": "Go Back",
        "intro": "Entorno de terminal con un binario SUID (`go-back`) que compara el argumento recibido con `/home/ctf/flag.txt` y devuelve el resultado de `strcmp` como código de salida del proceso.",
        "obj": "Analizar fugas de información por canal lateral basadas en códigos de retorno de procesos (*exit status oracle*) y por qué las comparaciones de secretos deben devolver únicamente un estado binario de tiempo constante.",
        "req": "Acceso por terminal TCP (`netcat`) y Ruby o Bash.",
        "meth": "Ejecutar `./go-back` carácter por carácter verificando el código de salida `$?` (`0` si coincide, `1` o `255` según el signo de la diferencia ASCII en `strcmp`) para reconstruir la flag secuencialmente.",
        "sol": "El binario devuelve el signo de la diferencia entre el carácter probado y el carácter real de la flag mediante su código de salida (`exitstatus`). Los scripts `solution/solve.rb` y `solution/solve-internal.rb` automatizan la extracción carácter por carácter.",
    },
    "go-git-it": {
        "cat": "Seguridad Web",
        "title": "Go Git It",
        "intro": "Sitio web estático cuyo servidor Nginx expone por error el directorio de control de versiones `/git/` con listado automático de archivos (`autoindex on`).",
        "obj": "Comprender el riesgo de exponer directorios `.git` en servidores web de producción y cómo auditar el historial de commits para identificar secretos eliminados en revisiones previas.",
        "req": "Cliente HTTP (`wget` o `curl`) y `git`.",
        "meth": "Inspeccionar el código fuente HTML para hallar la nota sobre `/git/`, descargar el repositorio expuesto, listar los commits con `git log --name-status` y recuperar el archivo eliminado `flag.html` con `git show`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "goto-zero": {
        "cat": "Pwn / Binarios",
        "title": "Goto Zero",
        "intro": "Binario SUID con vulnerabilidad de desbordamiento de búfer en la pila, compilado sin PIE pero con aleatorización del espacio de direcciones (ASLR) activa en el sistema.",
        "obj": "Construir cadenas de programación orientada a retorno (ROP) en dos etapas: filtración de direcciones de `libc` mediante la tabla GOT/PLT con retorno a `main()`, seguida de lectura del archivo de la flag.",
        "req": "Ruby, `objdump`/`gdb` y cliente TCP (`netcat`).",
        "meth": "Enviar una primera carga útil ROP que invoque `puts(puts@GOT)` y retorne a `main()`, calcular la dirección base de `libc` a partir de la dirección filtrada y enviar una segunda cadena ROP que ejecute `open`/`read`/`puts` sobre `/home/ctf/flag.txt`.",
        "sol": "El script `solution/exploit_script.rb` (ejecutado remotamente por `solution/solve.rb`) realiza el ROP en dos fases: filtra la entrada GOT de `puts`, retorna a `main()`, calcula la base de `libc.so.6` y ejecuta `open`/`read`/`puts` sobre `/home/ctf/flag.txt`.",
    },
    "hangman-one": {
        "cat": "Seguridad Web",
        "title": "Hangman One",
        "intro": "Juego web del ahorcado en Flask donde todos los usuarios comparten la misma palabra objetivo estática, pero cada cuenta dispone únicamente de 4 vidas.",
        "obj": "Identificar fallas de lógica de negocio cuando un secreto compartido carece de límite global de intentos entre distintas cuentas de usuario.",
        "req": "Python 3 (`requests`, `beautifulsoup4`).",
        "meth": "Registrar múltiples cuentas de usuario sucesivas para probar distintos subconjuntos del alfabeto alfanumérico sin que el límite de 4 errores por usuario impida descubrir las letras que componen la palabra.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "hangman-two": {
        "cat": "Seguridad Web",
        "title": "Hangman Two",
        "intro": "Segunda versión del juego del ahorcado donde cada usuario recibe una palabra aleatoria de 25 caracteres, vinculada en la base de datos mediante una cookie llamada `state`.",
        "obj": "Analizar vulnerabilidades de desvinculación entre estado de sesión y autorización (IDOR en cookies de estado) cuando el contador de intentos fallidos se almacena en el usuario pero el recurso objetivo se referencia por una cookie manipulable.",
        "req": "Python 3 (`requests`, `beautifulsoup4`).",
        "meth": "Capturar la cookie `state` generada para el primer usuario y reutilizarla en nuevas cuentas registradas (probando 3 letras por cuenta) para descubrir los caracteres de la misma palabra aleatoria sin perder las 4 vidas.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "hangman-three": {
        "cat": "Seguridad Web / Criptografía",
        "title": "Hangman Three",
        "intro": "Tercera versión del juego del ahorcado que almacena el contador de vidas perdidas (`life_lost`) dentro de un JSON Web Token (JWT) firmado con HS256.",
        "obj": "Auditar la fortaleza de secretos de firma HMAC en tokens JWT y comprender cómo una clave débil de diccionario permite falsificar reclamaciones (*claims*) de estado.",
        "req": "Python 3 (`requests`, `beautifulsoup4`, `pyjwt`) y `hashcat` (o diccionario `jwt.secrets.list`).",
        "meth": "Extraer la cookie `access_token_cookie`, recuperar la clave secreta HMAC (`tobemodified`) mediante ataque de diccionario y firmar tokens JWT propios fijando `\"life_lost\": \"0\"` en cada intento.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "hidden-reports": {
        "cat": "Seguridad Web",
        "title": "Hidden Reports",
        "intro": "Formulario web en PHP que protege el acceso a reportes confidenciales verificando una frase de paso mediante una consulta SQL construida por concatenación directa.",
        "obj": "Identificar vulnerabilidades de Inyección SQL (SQLi) por tautología booleana en formularios de autenticación y aprender a mitigarlas mediante consultas preparadas (*prepared statements*).",
        "req": "Navegador web, `curl` o Ruby (`httparty`).",
        "meth": "Ingresar una condición lógica siempre verdadera en el campo `passphrase` (como `test' or '1'='1`) para que la cláusula `WHERE` devuelva los reportes protegidos.",
        "sol": "El archivo `challenge/app/index.php` interpola directamente `$_POST['passphrase']` en la consulta SQL sin parametrización. El script `solution/solve.rb` envía `test' or '1'='1` y verifica la obtención de la flag.",
    },
    "hoard": {
        "cat": "Seguridad Web / Pwn",
        "title": "Dragon Hoard",
        "intro": "Calculadora web de tesoros cuyo backend en PHP (`backend.php`) recibe un objeto JSON e invoca un binario del sistema pasando los campos numéricos dentro de una cadena de shell.",
        "obj": "Analizar vulnerabilidades de inyección de comandos en APIs JSON cuando se confía en la validación de tipos del frontend sin sanitizar los argumentos en el backend.",
        "req": "Cliente HTTP (`curl` o Ruby con `httparty`).",
        "meth": "Inspeccionar `distfiles/backend.php`, observar cómo se interpola el campo `artifacts` entre comillas simples en la llamada a `exec()` e inyectar el cierre de comilla simple seguido de la lectura de `/flag.txt`.",
        "sol": "El endpoint `backend.php` pasa el campo `artifacts` del JSON a un comando de shell entre comillas simples sin usar `escapeshellarg()` ni convertirlo a entero. El script `solution/solve.rb` automatiza la prueba.",
    },
    "last": {
        "cat": "Seguridad Web / Criptografía",
        "title": "NextPM",
        "intro": "Gestor de contraseñas desarrollado en Next.js que protege sus rutas de API (`/api/users`, `/api/keybag/[user]`) mediante un middleware de autenticación y cifra los cofres de claves con Argon2id y NaCl SecretBox.",
        "obj": "Comprender la vulnerabilidad de evasión de middleware en Next.js (CVE-2025-29927) mediante la cabecera `X-Middleware-Subrequest` y auditar el almacenamiento de hashes bcrypt débiles que protegen bóvedas cifradas.",
        "req": "Python 3 (`requests`, `bcrypt`, `pynacl`).",
        "meth": "Enviar la cabecera `X-Middleware-Subrequest: middleware:middleware:middleware:middleware:middleware` a `/api/users` para omitir la verificación de sesión, obtener el hash bcrypt del usuario `bingo`, recuperar su contraseña (`banditthedog`), descargar `/api/keybag/bingo` y descifrar la bóveda con libsodium/PyNaCl.",
        "sol": "El script `solution/solve.py` explota la evasión de middleware en Next.js enviando la cabecera `X-Middleware-Subrequest` a `/api/users` y `/api/keybag/bingo`, recupera la contraseña del usuario `bingo` (`banditthedog`) a partir de su hash bcrypt y deriva la clave Argon2id para abrir el `SecretBox` de NaCl donde se almacena la entrada `flag`.",
    },
    "locky": {
        "cat": "Seguridad Física (On-Site)",
        "title": "Locky",
        "intro": "Desafío presencial de apertura de cerraduras físicas (*lockpicking*) dispuesto en la mesa de laboratorio.",
        "obj": "Comprender el funcionamiento mecánico interno de los cilindros de pines (*pin tumbler locks*) y las técnicas de tensión y rastrillado/ganzuado pin por pin.",
        "req": "Acceso presencial al cilindro de práctica y herramientas de ganzuado del laboratorio.",
        "meth": "Aplicar tensión ligera al rotor del cilindro y alinear cada contraperno sobre la línea de corte hasta girar el cilindro y obtener el código de validación.",
        "sol": "Al abrir el cilindro físico de práctica en la mesa del laboratorio presencial, los instructores validan la apertura y entregan la flag configurada.",
    },
    "magic": {
        "cat": "Forense Digital",
        "title": "Magic",
        "intro": "Archivo de imagen (`magic.png`) que los visores gráficos rechazan abrir debido a una alteración en sus primeros bytes.",
        "obj": "Comprender la estructura de firmas de archivo (*magic bytes*) y cómo identificar y reparar cabeceras PNG corruptas mediante análisis hexadecimal.",
        "req": "Editor hexadecimal (`xxd`, `hexedit` o Python).",
        "meth": "Inspeccionar los primeros 8 bytes de `distfiles/magic.png`, observar que los primeros 4 bytes fueron reemplazados por `616e 7368` y restaurarlos al valor estándar PNG `8950 4e47`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "matryoshkafs": {
        "cat": "Forense Digital",
        "title": "MatryoshkaFS",
        "intro": "Archivo comprimido (`fs.xz`) que contiene 16 imágenes de sistemas de archivos históricos y modernos anidados uno dentro de otro como una muñeca rusa.",
        "obj": "Identificar, montar y extraer datos de múltiples sistemas de archivos y tablas de particiones heterogéneas (ReiserFS, Amiga AFFS, CramFS, HFS, GPT/Minix, SquashFS, HPFS, ISO9660, UDF, SGI/F2FS, Sun/NILFS2, exFAT, NTFS, JFS, Btrfs y XFS con sectores de 8 KB).",
        "req": "Entorno Linux con utilidades de montaje loop (`losetup`, `mount`, `xfs_db`, `mmls`, `xzcat`).",
        "meth": "Inspeccionar cada capa con `file` y `mmls`, descomprimir o montar en bucle cada sistema de archivos sucesivo (y extraer con `xfs_db`/`dd` en la capa XFS de sectores de 8192 bytes) hasta recuperar `flag.heic` en la última capa.",
        "sol": "Consulte la bitácora completa de comandos de extracción de las 19 etapas y sus sumas SHA-256 en `solution/solution.txt`.",
    },
    "meow": {
        "cat": "Terminal / Introductorio (101)",
        "title": "Meow",
        "intro": "Desafío introductorio de conexión a una consola remota Linux donde la flag se encuentra almacenada en el directorio personal del usuario.",
        "obj": "Familiarizarse con la conexión a servicios de terminal interactiva en un CTF y el uso de comandos básicos de lectura de archivos en Unix/Linux (`ls`, `cat`).",
        "req": "Cliente TCP (`netcat` / `nc`).",
        "meth": "Conectarse al puerto TCP 4445 del desafío, listar los archivos del directorio `/home/ctf` con `ls` y mostrar el contenido de `/home/ctf/flag.txt` mediante el comando `cat` (en alusión al nombre del reto, *meow*).",
        "sol": "Al conectarse a la terminal del contenedor y ejecutar `cat /home/ctf/flag.txt` se obtiene directamente la flag configurada.",
    },
    "moa-station": {
        "cat": "Seguridad Web / Extensiones de Navegador",
        "title": "MoA Station",
        "intro": "Servicio de revisión automatizada de visas que visita la URL enviada utilizando un navegador Chromium con una extensión personalizada instalada.",
        "obj": "Analizar la superficie de ataque de las extensiones de navegador (`content_scripts` y `background.js`), la inyección de eventos DOM simulados y el abuso de endpoints JSONP permitidos por la CSP de la extensión.",
        "req": "Servidor HTTP público o local accesible por el bot y cliente HTTP (`curl`).",
        "meth": "Examinar el código de la extensión en `distfiles/`, identificar la secuencia de teclas que activa el modo de depuración en el script de contenido, despachar eventos `KeyboardEvent` sintéticos desde una página HTML controlada e inyectar un callback JSONP permitido por la política de seguridad para leer `localStorage.getItem('secret')`.",
        "sol": "La extensión almacena la flag en `localStorage.setItem('secret', ...)` dentro de `background.js`. El archivo `solution/exploit.html` simula los eventos de teclado requeridos por el script de contenido para inyectar una etiqueta `<script>` que abusa de un endpoint con soporte `callback` permitido en la CSP de la extensión y exfiltra `localStorage.getItem('secret')`.",
    },
    "nearest-neighbor": {
        "cat": "Forense Digital / Esteganografía",
        "title": "Nearest Neighbor",
        "intro": "Imagen de fondo de pantalla de alta resolución (`4096x3072`, `flag.webp`) que oculta una segunda imagen intercalada cada 16 píxeles en ambos ejes.",
        "obj": "Comprender las diferencias entre algoritmos de interpolación de imágenes (bilineal, bicúbico vs. vecino más cercano) y cómo el submuestreo periódico permite ocultar información visual.",
        "req": "ImageMagick (`magick` / `convert`) o Python con Pillow.",
        "meth": "Inspeccionar la imagen con zoom para observar la rejilla de píxeles cada 16 posiciones y redimensionar `distfiles/flag.webp` a `256x192` especificando interpolación `nearest-neighbor`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "obscuratron": {
        "cat": "Ingeniería Inversa / Criptografía (101)",
        "title": "Obscuratron",
        "intro": "Documento PDF confidencial cifrado (`memo.pdf.enc`) acompañado del binario ELF (`obscuratron`) que se utilizó para cifrarlo.",
        "obj": "Desensamblar una utilidad de cifrado simple para identificar su algoritmo byte a byte e implementar la rutina inversa de descifrado.",
        "req": "Desensamblador (`Ghidra` / `objdump`) y Ruby o Python.",
        "meth": "Analizar la función `main` del binario `distfiles/obscuratron`, observar que inicializa una clave de un byte en `0xab`, aplica XOR con cada byte de entrada y actualiza la clave con el byte cifrado resultante (`c_i = p_i ^ c_{i-1}`), e invertir la operación para recuperar `memo.pdf`.",
        "sol": "El binario cifra cada byte como `c[i] = p[i] ^ key` y luego asigna `key = c[i]` (con valor inicial `key = 0xab`). El script `solution/solve.rb` invierte la operación (`p[i] = c[i] ^ key; key = c[i]`), verifica el hash SHA-256 contra `memo.pdf` y recupera el documento con la flag.",
    },
    "oh-say-can-you-see": {
        "cat": "IA / Machine Learning / Forense",
        "title": "Oh Say Can You See",
        "intro": "Modelo clasificador de imágenes en formato Keras (`flag_classifier.keras`) sobreajustado sobre 4 imágenes en escala de grises de 256x256 píxeles.",
        "obj": "Comprender los riesgos de privacidad y memorización de datos de entrenamiento en redes neuronales sobreparametrizadas mediante ataques de inversión de modelos (*model inversion*).",
        "req": "Python 3 (`tensorflow`, `keras`, `numpy`, `pillow`).",
        "meth": "Inspeccionar la arquitectura del modelo con `model_summary.py` y ejecutar optimización por descenso de gradiente sobre el tensor de entrada (`invert_model.py`) para reconstruir las 4 imágenes memorizadas por las clases de salida.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "oh-the-places-youll-go": {
        "cat": "OSINT Geográfico",
        "title": "Oh The Places You'll Go (Parte 1)",
        "intro": "Conjunto de 11 capturas de Google Street View frente a monumentos históricos mundiales junto con un mapa guía (`places.tar.gz`).",
        "obj": "Aplicar técnicas de geolocalización visual (orientación de brújula, perspectiva arquitectónica y búsqueda en Street View) para ubicar puntos exactos e identificar caracteres en elementos del entorno.",
        "req": "Navegador web con acceso a Google Maps / Street View y descompresor `tar`.",
        "meth": "Localizar cada una de las 11 vistas en Google Street View, extraer el número o palabra señalada por el recuadro en cada ubicación y ensamblar el mensaje según el orden del mapa.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "oh-the-places-youll-go-2": {
        "cat": "OSINT Geográfico",
        "title": "Oh The Places You'll Go (Parte 2)",
        "intro": "Segunda etapa del desafío de geolocalización OSINT compuesta por 12 fotografías de carreteras y costas sin monumentos famosos.",
        "obj": "Utilizar metadatos visuales avanzados de geolocalización (formato de matrículas, bolardos, señalética vial, posición solar y vehículos de captura) para determinar coordenadas geográficas exactas.",
        "req": "Navegador web con acceso a Google Maps / Street View, guías de geolocalización (Plonk It / GeoHints).",
        "meth": "Identificar el país y punto exacto de las 12 imágenes, tomar los dos primeros dígitos decimales de la latitud y longitud de cada punto (4 dígitos por imagen, 48 dígitos en total) y construir la flag en el formato `DUOC{coordenadas_<48_digitos>}`.",
        "sol": "Consulte el desglose completo de las 12 ubicaciones y sus coordenadas en `oh-the-places-youll-go/solution/README.md`.",
    },
    "pascals-homomorphism": {
        "cat": "Criptografía",
        "title": "Pascal's Homomorphism 1",
        "intro": "Servicio interactivo que implementa el criptosistema homomórfico de Paillier con una clave inicial débil de 192 bits para cifrar la primera flag.",
        "obj": "Comprender la estructura matemática del criptosistema de Paillier ($g = n + 1$, módulo $n^2$) y cómo recuperar el texto plano cuando el módulo $n = p \\cdot q$ puede factorizarse.",
        "req": "GP/PARI (o Python / SageMath) y `netcat`.",
        "meth": "Conectarse al servicio, obtener el módulo débil $n$ de 192 bits y el texto cifrado de la primera flag (`getflag`), factorizar $n = p \\cdot q$ para calcular $\\lambda = (p-1)(q-1)$ y $u = \\lambda^{-1} \\bmod n$, y aplicar la función de descifrado de Paillier.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "pascals-homomorphism-2": {
        "cat": "Criptografía",
        "title": "Pascal's Homomorphism 2",
        "intro": "Segunda parte del desafío sobre el criptosistema de Paillier (mismo servicio en el puerto 1999), utilizando una clave fuerte de 1024 bits y un oráculo de descifrado limitado a entradas menores de 2000 bits.",
        "obj": "Explotar la propiedad homomórfica aditiva del criptosistema de Paillier ($\\text{Dec}(c_1 \\cdot c_2 \\bmod n^2) = (m_1 + m_2) \\bmod n$) para eludir restricciones de longitud en un oráculo de descifrado.",
        "req": "GP/PARI (o Python / SageMath) y `netcat`.",
        "meth": "Generar una clave fuerte (`genkey strong`), obtener la segunda flag cifrada $c$ (~2048 bits), extraer factores primos pequeños de $c$ hasta que el cofactor restante sea menor de 2000 bits, descifrar cada factor en el oráculo (`decrypt`) y sumar los textos planos resultantes módulo $n$.",
        "sol": "Consulte el procedimiento detallado para la segunda flag en `pascals-homomorphism/solution/README.md`.",
    },
    "pathing": {
        "cat": "Seguridad Web (101)",
        "title": "Pathing",
        "intro": "Servidor web minimalista que resuelve rutas de archivos estáticos sin normalizar secuencias de salto de directorio (`../`).",
        "obj": "Comprender las vulnerabilidades de Path Traversal (Directory Traversal) a nivel de servidor HTTP y la importancia de canonicalizar rutas dentro del directorio raíz permitido.",
        "req": "Cliente HTTP que no normalice rutas antes de enviarlas (`curl --path-as-is` o Ruby con `httparty`).",
        "meth": "Solicitar directamente `/../../../../../../flag.txt` desactivando la normalización local de URL en el cliente HTTP (`curl --path-as-is`).",
        "sol": "El servidor web concatena la ruta de la solicitud HTTP sin filtrar `../`. El script `solution/solve.rb` realiza la petición con secuencias `../` y verifica la flag.",
    },
    "qr-decomp": {
        "cat": "Criptografía / Matemáticas (On-Site 101)",
        "title": "QR Decomposition",
        "intro": "Cinco fragmentos de códigos QR que contienen las matrices ortogonal $Q$ y triangular superior $R$ resultantes de la descomposición QR de una matriz $M_{4\\times 4}$ con los caracteres de la flag.",
        "obj": "Relacionar el concepto de códigos QR con la descomposición matricial $M = Q \\cdot R$ del álgebra lineal para reconstruir información codificada en matrices numéricas.",
        "req": "Lector de códigos QR y entorno de cálculo matricial (GP/PARI, Python NumPy o Octave).",
        "meth": "Ensamblar y escanear los fragmentos de los códigos QR 1, 2a/2b y 3a/3b para obtener las matrices $Q$ y $R$, multiplicar $Q \\times R$, redondear al entero más cercano y convertir los 16 valores ASCII a texto.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "ruthless-dot-flag": {
        "cat": "Forense Digital (101)",
        "title": "Ruthless.flag (Parte 1)",
        "intro": "Archivo gráfico en formato propietario `.r16` (`flags.r16`) procedente del videojuego clásico de 1998 *Tom Clancy's ruthless.com*.",
        "obj": "Practicar ingeniería inversa de formatos binarios de imagen sin compresión (cabecera de dimensiones y píxeles RGB555 de 16 bits little-endian).",
        "req": "Python 3, GIMP (modo Raw Image Data) o `hexdump`.",
        "meth": "Analizar la cabecera de 18 bytes (`0x0320` = 800 de ancho, `0x0258` = 600 de alto) y decodificar cada par de bytes little-endian como 5 bits por canal RGB (`r16_to_ppm.py`) para visualizar la imagen.",
        "sol": "Consulte el procedimiento detallado en `solution/solution.txt`.",
    },
    "ruthless-dot-flag-2": {
        "cat": "Forense Digital / Esteganografía",
        "title": "Ruthless.flag (Parte 2)",
        "intro": "Segunda capa oculta dentro del mismo archivo `flags.r16` del desafío `ruthless-dot-flag`.",
        "obj": "Identificar canales de datos ignorados por el renderizador (el bit de transparencia alfa en píxeles de 16 bits ARGB1555 cuando la cabecera desactiva el canal alfa) para extraer archivos incrustados bit a bit.",
        "req": "Python 3 (`struct`).",
        "meth": "Extraer el bit más significativo (`(rgba & 0x8000) >> 15`) de cada uno de los $800 \\times 600$ píxeles de `flags.r16` utilizando `r16_extract_hidden_data.py` y empaquetar los bits en bytes para obtener la imagen con la segunda flag.",
        "sol": "Consulte el procedimiento detallado para la segunda flag en `ruthless-dot-flag/solution/solution.txt`.",
    },
    "sighting": {
        "cat": "Seguridad Web (101)",
        "title": "Dragon Sighting",
        "intro": "Aplicación web en PHP que carga imágenes dinámicamente a través del endpoint `picture.php?file=...` sin validar que el archivo pertenezca al directorio permitido.",
        "obj": "Identificar y corregir vulnerabilidades de Inclusión Local de Archivos (LFI) / Path Traversal en parámetros de consulta PHP.",
        "req": "Navegador web, `curl` o Ruby (`httparty`).",
        "meth": "Modificar el parámetro `file` en `picture.php?file=../../../../../../flag.txt` para atravesar directorios hasta la raíz del sistema de archivos y leer `/flag.txt`.",
        "sol": "El script `picture.php` lee el archivo indicado en el parámetro GET `file` sin sanitizar `../`. El verificador `solution/solve.rb` recupera `/flag.txt` y comprueba la flag.",
    },
    "slackblock-steg": {
        "cat": "Forense Digital / Esteganografía",
        "title": "SlackBlock Steg",
        "intro": "Aplicación web y archivo JPEG (`flag.jpg`) que ocultan datos binarios en los píxeles de relleno (*slack pixels*) fuera de las dimensiones visibles cuando el ancho o alto no es múltiplo de 8.",
        "obj": "Comprender cómo los bloques MCU de $8\\times 8$ del estándar JPEG conservan píxeles adicionales cuando se recortan las dimensiones en el segmento SOF0 y cómo inspeccionarlos modificando la cabecera JPEG.",
        "req": "Python 3 y visor de imágenes.",
        "meth": "Ejecutar `jpeg_uncrop.py` sobre `distfiles/flag.jpg` para redondear el ancho y alto en el marcador SOF0 al siguiente múltiplo de 8 y decodificar los bits blanco/negro almacenados en la fila/columna adicional.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "soothsayer": {
        "cat": "Seguridad Móvil (Android) / Criptografía",
        "title": "Soothsayer",
        "intro": "Aplicación Android conectada a Firebase Firestore y un servidor Python donde el jugador debe acertar 30 predicciones binarias consecutivas generadas mediante Mersenne Twister.",
        "obj": "Analizar vulnerabilidades de control de acceso y exposición de estado cuando la semilla del generador pseudoaleatorio (PRNG) y el puntaje se almacenan en documentos de Firestore accesibles o manipulables desde el cliente mediante Frida.",
        "req": "Python 3 (`numpy`, `requests`, `firebase-admin`) o emulador Android con `adb` y `frida`.",
        "meth": "Instrumentar la aplicación Android con Frida (`solver.js`) o consultar la semilla almacenada en el documento del usuario en Firestore para precalcular las 30 elecciones de `numpy.random` y solicitar `/get-flag`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "subprime": {
        "cat": "Criptografía (101)",
        "title": "Subprime",
        "intro": "Archivo de texto con una clave pública RSA de módulo pequeño ($n = 98563159, e = 1009$) y un arreglo de enteros que representan los caracteres de la flag cifrados individualmente.",
        "obj": "Comprender los fundamentos matemáticos de RSA y por qué la seguridad del esquema depende de que el módulo $n = p \\cdot q$ no pueda factorizarse en tiempo razonable.",
        "req": "Python 3.",
        "meth": "Factorizar $n = 98563159 = 9883 \\times 9973$, calcular $\\phi(n) = 98543304$ y la clave privada $d = e^{-1} \\bmod \\phi(n) = 31545577$, y descifrar cada entero $c_i$ del archivo `distfiles/cipher.txt` como $m_i = c_i^d \\bmod n$.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "tarnation": {
        "cat": "Forense Digital (101)",
        "title": "Tarnation",
        "intro": "Respaldo comprimido (`tarnation.tar.xz`) formado por múltiples archivos `.tar` concatenados que contienen tres versiones distintas de un archivo llamado `.`.",
        "obj": "Comprender el comportamiento de los archivos tar concatenados y cómo listar y extraer ocurrencias específicas de archivos cuyo nombre colisiona con el directorio actual (`.`).",
        "req": "Utilidad `tar` con soporte `xz` (o `binwalk`).",
        "meth": "Listar todas las entradas con `tar -Jtiv -f tarnation.tar.xz` y extraer la segunda ocurrencia del archivo `.` hacia la salida estándar con `tar -Jiv -x '.' -f tarnation.tar.xz -O --occurrence=2 > flag.jpg`.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "taxonomy": {
        "cat": "Seguridad Web (101)",
        "title": "Dragon Taxonomy",
        "intro": "Directorio web de especies de dragones respaldado por SQLite que oculta los registros marcados con `is_classified = 0` pero concatena el término de búsqueda directamente dentro de paréntesis en la consulta SQL.",
        "obj": "Aprender a identificar la estructura de consultas SQL con condiciones agrupadas por paréntesis y cómo evitar la inyección SQL utilizando parámetros vinculados (*bound parameters*).",
        "req": "Navegador web, `curl` o Ruby (`httparty`).",
        "meth": "Cerrar la comilla simple y el paréntesis de la condición de búsqueda en el parámetro `?search=Nano' OR 1=1) --` para anular el filtro `AND is_classified = 0` y listar el registro `Dragon-000`.",
        "sol": "La consulta en `challenge/app/index.php` tiene la forma `SELECT ... WHERE (name LIKE '%$search%' ...) AND is_classified = 0`. Al enviar `?search=Nano' OR 1=1) --` se cierra el paréntesis y se comenta el filtro de clasificación. El script `solution/solve.rb` automatiza la verificación.",
    },
    "toothless": {
        "cat": "Forense de Redes (101)",
        "title": "Toothless",
        "intro": "Captura de tráfico de red (`toothless.pcap`) con decenas de paquetes ICMP Echo Request y Echo Reply entre dos hosts.",
        "obj": "Utilizar herramientas de análisis de tráfico de red (Wireshark / `tshark`) para filtrar conversaciones ICMP e identificar paquetes anómalos sin respuesta que transportan datos exfiltrados.",
        "req": "Wireshark, `tshark` o Python / `strings` + `base64`.",
        "meth": "Filtrar los paquetes ICMP en `distfiles/toothless.pcap`, localizar la única solicitud ICMP Echo Request (secuencia 29) que carece de Echo Reply, extraer la cadena Base64 de su campo de datos y decodificarla.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "web-tutorial-1": {
        "cat": "Seguridad Web (101)",
        "title": "Web Tutorial 1 (XSS)",
        "intro": "Aplicación web educativa con un bot administrador que revisa las cargas útiles enviadas y una política CSP permisiva que acepta scripts en línea.",
        "obj": "Comprender el funcionamiento de Cross-Site Scripting (XSS) cuando la cabecera Content-Security-Policy incluye `'unsafe-inline'` y cómo proteger endpoints sensibles y cookies de sesión.",
        "req": "Navegador web, endpoint receptor HTTP (webhook/requestbin) o Python 3 (`requests`).",
        "meth": "Enviar una etiqueta `<script>` que realice una petición `XMLHttpRequest` interna a `/xss-one-flag` desde el contexto del navegador del administrador y reenvíe la respuesta a un receptor externo.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "web-tutorial-2": {
        "cat": "Seguridad Web / Cloud",
        "title": "Web Tutorial 2 (CSP Bypass)",
        "intro": "Segunda parte del tutorial de XSS donde la política Content-Security-Policy bloquea scripts en línea pero autoriza la carga de scripts desde cualquier subdominio `*.us-central1.run.app`.",
        "obj": "Analizar el riesgo de autorizar comodines de plataformas de nube compartidas (`*.run.app`, `*.appspot.com`) dentro de la directiva `script-src` de Content-Security-Policy.",
        "req": "Python 3 (`requests`) o cuenta en Google Cloud Run / Cloud Functions.",
        "meth": "Inyectar una etiqueta `<script src='...'>` apuntando a un servicio en `*.us-central1.run.app` que sirva el código JavaScript encargado de leer `/xss-two-flag` y exfiltrar su contenido.",
        "sol": "Consulte el procedimiento detallado en `solution/README.md`.",
    },
    "your-browser-hates-you": {
        "cat": "Seguridad Web / TLS (101)",
        "title": "Your Browser Hates You",
        "intro": "Servidor HTTPS en el puerto 443 configurado intencionalmente con un certificado TLS autofirmado/inválido que los navegadores modernos bloquean de forma estricta.",
        "obj": "Comprender cómo funcionan las validaciones de cadena de confianza de certificados X.509/TLS y cómo inspeccionar servicios HTTPS de laboratorio mediante herramientas de línea de comandos (`curl -k`).",
        "req": "`curl`, `openssl s_client` o Ruby (`httparty`).",
        "meth": "Realizar una petición HTTPS omitiendo la verificación de autoridad certificadora (`curl -k https://<host>:443/`) para inspeccionar el código HTML devuelto por el servidor.",
        "sol": "El servidor HTTPS devuelve la flag directamente en el documento HTML (`challenge/app/index.html`) cuando se establece la conexión TLS ignorando la advertencia del certificado (`curl -k` o `HTTParty.get(PATH, verify: false)` en `solution/solve.rb`).",
    },
}


def get_exec_instructions(ch):
    has_compose = os.path.exists(os.path.join(ch, "challenge", "docker-compose.yml"))
    has_docker = os.path.exists(os.path.join(ch, "challenge", "Dockerfile"))
    dist_dir = os.path.join(ch, "distfiles")
    dist_files = []
    if os.path.exists(dist_dir):
        dist_files = [f for f in os.listdir(dist_dir) if f != ".keep" and not f.startswith(".")]

    lines = []
    if has_compose:
        lines.append("1. Para levantar el entorno del desafío localmente con Docker Compose:")
        lines.append("   ```bash")
        lines.append(f"   cd {ch}/challenge && docker compose up --build")
        lines.append("   ```")
    elif has_docker:
        lines.append("1. Para construir y ejecutar el contenedor del desafío con Docker:")
        lines.append("   ```bash")
        lines.append(f"   cd {ch}/challenge && docker build -t ctf-{ch} . && docker run --rm -it -P ctf-{ch}")
        lines.append("   ```")
    else:
        lines.append("1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).")

    if dist_files:
        files_str = ", ".join(f"`distfiles/{f}`" for f in sorted(dist_files))
        lines.append(f"2. Archivos distribuidos al participante: {files_str}.")
    else:
        lines.append("2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.")
    return "\n".join(lines)


def generate_all():
    created_sol_readmes = []
    created_chall_readmes = []

    for ch, (old_f, new_f, is_bin, extra_files) in sorted(FLAG_MAPPING.items()):
        info = CHALLENGE_DOCS[ch]

        # 1. Si no existe solution/README.md, crearlo en español con la flag oficial
        sol_dir = os.path.join(ch, "solution")
        os.makedirs(sol_dir, exist_ok=True)
        sol_readme = os.path.join(sol_dir, "README.md")
        if not os.path.exists(sol_readme):
            sol_content = f"""# Guía de Solución — `{ch}` ({info['title']})

## Categoría
{info['cat']}

## Procedimiento de Resolución
{info['sol']}

## Flag Esperada
```text
{new_f}
```
"""
            with open(sol_readme, "w", encoding="utf-8") as f:
                f.write(sol_content)
            created_sol_readmes.append(sol_readme)
        else:
            # Asegurar que la flag oficial estandarizada figure en solution/README.md
            with open(sol_readme, "r", encoding="utf-8") as f:
                sc = f.read()
            if new_f not in sc:
                sc += f"\n\n## Flag Estandarizada\n```text\n{new_f}\n```\n"
                with open(sol_readme, "w", encoding="utf-8") as f:
                    f.write(sc)

        # 2. Crear/actualizar <reto>/README.md en español con las 9 secciones obligatorias
        chall_readme = os.path.join(ch, "README.md")
        exec_instr = get_exec_instructions(ch)

        meta_path = os.path.join(ch, "metadata.yml")
        author = "Equipo CTF"
        points = "1000"
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                mc = f.read()
            m_auth = re.search(r"^author:\s*['\"]?([^'\"\n]+)['\"]?", mc, re.M)
            if m_auth:
                author = m_auth.group(1).strip()
            m_val = re.search(r"^value:\s*(\d+)", mc, re.M)
            if m_val:
                points = m_val.group(1).strip()

        chall_content = f"""# Desafío CTF: `{ch}` — {info['title']}

## 1. Introducción
{info['intro']}
- **Categoría:** {info['cat']}

## 2. Objetivo
{info['obj']}

## 3. Requisitos
- {info['req']}

## 4. Instrucciones de ejecución
{exec_instr}

## 5. Metodología de resolución
{info['meth']}

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `{points}` puntos (configurado en `metadata.yml`).
- El desafío otorga el puntaje al validar la cadena de respuesta exacta en la plataforma del CTF.

## 7. Formato de flags
La flag de este desafío sigue el estándar institucional del laboratorio:
```text
DUOC{{palabra_clave_XXXXX}}
```

## 8. Consideraciones de seguridad
- Este ejercicio debe ejecutarse exclusivamente dentro del entorno de laboratorio aislado o sobre los archivos provistos en `distfiles/`.
- No utilices las técnicas estudiadas fuera de entornos educativos expresamente autorizados.

## 9. Créditos y referencias
- **Autor original:** `{author}`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
"""
        with open(chall_readme, "w", encoding="utf-8") as f:
            f.write(chall_content)
        created_chall_readmes.append(chall_readme)

    print(f"[OK] Creados {len(created_sol_readmes)} archivos solution/README.md faltantes.")
    print(f"[OK] Creados/actualizados {len(created_chall_readmes)} archivos <reto>/README.md en español.")


if __name__ == "__main__":
    generate_all()
