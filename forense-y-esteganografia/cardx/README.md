# Desafío CTF: `cardx` — CardX

## 1. Introducción
Galería web de 29 cartas coleccionables de alta resolución que contienen patrones esteganográficos de puntos amarillos de impresora.
- **Categoría:** Forense Digital

## 2. Objetivo
Analizar códigos de identificación de máquina (MIC / Xerox DocuColor tracking dots) en el canal azul de imágenes digitales para autenticar documentos y extraer metadatos de fecha y hora.

## 3. Requisitos
- Visor/editor de imágenes con separación de canales RGB (GIMP, ImageMagick o Python Pillow).

## 4. Instrucciones de ejecución
1. Para levantar el entorno del desafío localmente con Docker Compose:
   ```bash
   cd cardx/challenge && docker compose up --build
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Aislar el canal azul de cada imagen `.webp`, decodificar la matriz de 15x8 puntos según el estándar Xerox DocuColor, descartar las cartas impresas en 2024 y ordenar cronológicamente por minuto de impresión las cartas auténticas de 1998.

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
- **Autor original:** `itsc0rg1 & symmetric`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
