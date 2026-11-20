# Desafío CTF: `locky` — Locky

## 1. Introducción
Desafío presencial de apertura de cerraduras físicas (*lockpicking*) dispuesto en la mesa de laboratorio.
- **Categoría:** Seguridad Física (On-Site)

## 2. Objetivo
Comprender el funcionamiento mecánico interno de los cilindros de pines (*pin tumbler locks*) y las técnicas de tensión y rastrillado/ganzuado pin por pin.

## 3. Requisitos
- Acceso presencial al cilindro de práctica y herramientas de ganzuado del laboratorio.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Aplicar tensión ligera al rotor del cilindro y alinear cada contraperno sobre la línea de corte hasta girar el cilindro y obtener el código de validación.

## 6. Sistema de puntuación
- **Puntaje base del desafío:** `100` puntos (configurado en `metadata.yml`).
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
- **Autor original:** `Matir/symmetric`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
