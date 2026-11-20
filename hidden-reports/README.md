# Desafío CTF: `hidden-reports` — Hidden Reports

## 1. Introducción
Formulario web en PHP que protege el acceso a reportes confidenciales verificando una frase de paso mediante una consulta SQL construida por concatenación directa.
- **Categoría:** Seguridad Web

## 2. Objetivo
Identificar vulnerabilidades de Inyección SQL (SQLi) por tautología booleana en formularios de autenticación y aprender a mitigarlas mediante consultas preparadas (*prepared statements*).

## 3. Requisitos
- Navegador web, `curl` o Ruby (`httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd hidden-reports/challenge && docker build -t ctf-hidden-reports . && docker run --rm -it -P ctf-hidden-reports
   ```
2. Conéctate al puerto o URL del servicio indicado en `metadata.yml`.

## 5. Metodología de resolución
Ingresar una condición lógica siempre verdadera en el campo `passphrase` (como `test' or '1'='1`) para que la cláusula `WHERE` devuelva los reportes protegidos.

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
