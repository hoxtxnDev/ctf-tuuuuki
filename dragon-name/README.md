# Desafío CTF: `dragon-name` — Dragon Name

## 1. Introducción
Aplicación Android (`dragon-name.apk`) que construye dinámicamente la flag en memoria al pulsar un botón pero no la muestra en pantalla.
- **Categoría:** Seguridad Móvil (Android)

## 2. Objetivo
Practicar ingeniería inversa estática de paquetes APK de Android utilizando `apktool` o Android Studio para analizar bytecode Smali/Kotlin y recursos `strings.xml`.

## 3. Requisitos
- Java y `apktool` (o `jadx` / Android Studio).

## 4. Instrucciones de ejecución
1. Este desafío se resuelve de forma estática/fuera de línea o presencial (no requiere levantar un contenedor de servicio).
2. Archivos distribuidos al participante: `distfiles/dragon-name.apk`.

## 5. Metodología de resolución
Desempaquetar `distfiles/dragon-name.apk`, localizar el método `createFlag()` en `MainActivity`, decodificar las transformaciones ROT13 y Base64 y recuperar el recurso `R.string.part4` desde `res/values/strings.xml`.

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
- **Autor original:** `itsc0rg1`
- **Adaptación y localización pedagógica:** Laboratorio Educativo de Ciberseguridad DUOC.
- **Documentación de solución para instructores:** [`solution/README.md`](solution/README.md)
