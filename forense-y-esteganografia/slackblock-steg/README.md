# Desafío CTF: `slackblock-steg` — SlackBlock Steg

## 1. Introducción
Aplicación web y archivo JPEG (`flag.jpg`) que ocultan datos binarios en los píxeles de relleno (*slack pixels*) fuera de las dimensiones visibles cuando el ancho o alto no es múltiplo de 8.
- **Categoría:** Forense Digital / Esteganografía

## 2. Objetivo
Comprender cómo los bloques MCU de $8\times 8$ del estándar JPEG conservan píxeles adicionales cuando se recortan las dimensiones en el segmento SOF0 y cómo inspeccionarlos modificando la cabecera JPEG.

## 3. Requisitos
- Python 3 y visor de imágenes.

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd slackblock-steg/challenge && docker build -t ctf-slackblock-steg . && docker run --rm -it -P ctf-slackblock-steg
   ```
2. Archivos distribuidos al participante: `distfiles/flag.jpg`.

## 5. Metodología de resolución
Ejecutar `jpeg_uncrop.py` sobre `distfiles/flag.jpg` para redondear el ancho y alto en el marcador SOF0 al siguiente múltiplo de 8 y decodificar los bits blanco/negro almacenados en la fila/columna adicional.

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
