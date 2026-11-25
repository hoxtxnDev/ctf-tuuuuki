# Desafío CTF: `oh-say-can-you-see` — Oh Say Can You See

## 1. Introducción
Modelo clasificador de imágenes en formato Keras (`flag_classifier.keras`) sobreajustado sobre 4 imágenes en escala de grises de 256x256 píxeles.
- **Categoría:** IA / Machine Learning / Forense

## 2. Objetivo
Comprender los riesgos de privacidad y memorización de datos de entrenamiento en redes neuronales sobreparametrizadas mediante ataques de inversión de modelos (*model inversion*).

## 3. Requisitos
- Python 3 (`tensorflow`, `keras`, `numpy`, `pillow`).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/flagnet.keras`.

## 5. Metodología de resolución
Inspeccionar la arquitectura del modelo con `model_summary.py` y ejecutar optimización por descenso de gradiente sobre el tensor de entrada (`invert_model.py`) para reconstruir las 4 imágenes memorizadas por las clases de salida.

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
