# Desafío CTF: `dragon-spell` — Dragon Spell

## 1. Introducción
Pergamino ilustrado (`dragon-spell.png`) escrito con un alfabeto rúnico personalizado que oculta un conjuro en inglés y la flag al final.
- **Categoría:** Criptografía

## 2. Objetivo
Aplicar análisis de frecuencias y reconocimiento de patrones léxicos para resolver un cifrado por sustitución monoalfabética.

## 3. Requisitos
- Visor de imágenes y bloc de notas.

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/Dragon-Spell.png`.

## 5. Metodología de resolución
Aprovechar las llaves `{` y `}` sin cifrar al final del texto para identificar las letras iniciales del formato de flag y utilizar palabras cortas frecuentes (`a`, `I`, `the`, `and`) para completar el alfabeto rúnico.

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
