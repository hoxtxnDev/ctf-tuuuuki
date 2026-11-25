# Desafío CTF: `dating` — Dragon Dating

## 1. Introducción
Aplicación web en Java/Tomcat que permite exportar e importar perfiles de usuario serializados en formato XML.
- **Categoría:** Seguridad Web / Pwn

## 2. Objetivo
Comprender los riesgos de deserialización insegura mediante `java.beans.XMLDecoder` y cómo prevenir la ejecución remota de código validando esquemas XML.

## 3. Requisitos
- Ruby (`httparty`, `uuid`) o cliente HTTP (`curl`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd dating/challenge && docker build -t ctf-dating . && docker run --rm -it -P ctf-dating
   ```
2. Archivos distribuidos al participante: `distfiles/ProfileServlet.java`.

## 5. Metodología de resolución
Inspeccionar el formato XML de los perfiles en `ProfileServlet`, identificar el uso de `XMLDecoder` y construir un documento XML que invoque un comando para leer `/flag.txt`.

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
