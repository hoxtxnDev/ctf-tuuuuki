# Desafío CTF: `bug-me` — Bug Me

## 1. Introducción
Binario ELF de Linux que implementa mecanismos antidepuración, verificación de suma de comprobación sobre `main()` y validación carácter por carácter mediante residuos modulares.
- **Categoría:** Ingeniería Inversa (RE)

## 2. Objetivo
Identificar rutinas de verificación de integridad y resolver sistemas de congruencias basados en el Teorema Chino del Resto (CRT) en binarios compilados.

## 3. Requisitos
- Desensamblador/descompilador (`Ghidra`, `IDA` o `objdump`), Ruby y entorno Linux x86_64.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd bug-me/challenge && docker build -t ctf-bug-me . && docker run --rm -it -P ctf-bug-me
   ```
2. Archivos distribuidos al participante: `distfiles/bug-me`.

## 5. Metodología de resolución
Localizar las funciones `match(char c)` añadidas al final del binario, extraer las tres condiciones modulares ($c \bmod 5$, $c \bmod 7$, $c \bmod 11$) para cada posición y reconstruir el carácter ASCII único que las satisface.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `1000` puntos (configurado en `metadata.yml`).
- El desafío otorga el puntaje al validar la cadena de respuesta exacta en la plataforma del CTF.

## 7. Formato de flags
La flag de este desafío sigue el estándar institucional del laboratorio:
```text
DUOC{palabra_clave_XXXXX}
```

## 8. Consideraciones de seguridad
- Este ejercicio debe ejecutarse exclusivamente dentro del entorno de laboratorio aislado o sobre los archivos provistos en `distfiles/`.
- No utilices las técnicas estudiadas fuera de entornos educativos expresamente autorizados.

## 9. Créditos y referencias
- **Autor original:** `ron`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
