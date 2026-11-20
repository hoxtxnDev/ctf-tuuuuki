# Desafío CTF: `flag-search` — Flag Search

## 1. Introducción
Binario interactivo que valida una clave hexadecimal de 128 bits mediante 28 comprobaciones incrementales antes de usarla para descifrar la flag con AES-128-ECB.
- **Categoría:** Ingeniería Inversa (RE)

## 2. Objetivo
Modelar restricciones sobre prefijos de bits extraídas de un binario desensamblado e implementar un algoritmo de búsqueda con retroceso (*backtracking*) para recuperar claves criptográficas.

## 3. Requisitos
- Python 3, desensamblador (`Ghidra` / `objdump`) y `netcat`.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd flag-search/challenge && docker build -t ctf-flag-search . && docker run --rm -it -P ctf-flag-search
   ```
2. Archivos distribuidos al participante: `distfiles/flag-search`.

## 5. Metodología de resolución
Extraer las condiciones del switch sobre la longitud de bits $i \in [4, 128]$ en la función de validación e implementar una búsqueda recursiva en profundidad (`solve_search.py`) que pode las ramas que incumplan cada condición.

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
- **Autor original:** `symmetric`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
