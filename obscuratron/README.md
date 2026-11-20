# Desafío CTF: `obscuratron` — Obscuratron

## 1. Introducción
Documento PDF confidencial cifrado (`memo.pdf.enc`) acompañado del binario ELF (`obscuratron`) que se utilizó para cifrarlo.
- **Categoría:** Ingeniería Inversa / Criptografía (101)

## 2. Objetivo
Desensamblar una utilidad de cifrado simple para identificar su algoritmo byte a byte e implementar la rutina inversa de descifrado.

## 3. Requisitos
- Desensamblador (`Ghidra` / `objdump`) y Ruby o Python.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/memo.pdf.enc`, `distfiles/obscuratron`.

## 5. Metodología de resolución
Analizar la función `main` del binario `distfiles/obscuratron`, observar que inicializa una clave de un byte en `0xab`, aplica XOR con cada byte de entrada y actualiza la clave con el byte cifrado resultante (`c_i = p_i ^ c_{i-1}`), e invertir la operación para recuperar `memo.pdf`.

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
