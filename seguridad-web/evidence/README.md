# Desafío CTF: `evidence` — Dragon Evidence

## 1. Introducción
Portal web en PHP que recibe archivos XML con reportes de avistamientos y expande entidades externas al procesarlos.
- **Categoría:** Seguridad Web

## 2. Objetivo
Comprender las vulnerabilidades de Entidades Externas XML (XXE) y cómo deshabilitar la carga de DTDs externas en analizadores XML.

## 3. Requisitos
- Cliente HTTP (`curl`, navegador o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd evidence/challenge && docker build -t ctf-evidence . && docker run --rm -it -P ctf-evidence
   ```
2. Archivos distribuidos al participante: `distfiles/index.php`.

## 5. Metodología de resolución
Declarar una entidad externa `<!ENTITY xxe SYSTEM "file:///flag.txt">` dentro del bloque `<!DOCTYPE>` del archivo XML subido y referenciarla como `&xxe;` dentro de la etiqueta `<proof>`.

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
