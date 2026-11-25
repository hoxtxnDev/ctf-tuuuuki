# Desafío CTF: `extinction` — Dragon Extinction

## 1. Introducción
Panel de autenticación en PHP que recibe credenciales en Base64 (`encoded_creds`), bloquea la cadena exacta `YWRtaW46YWRtaW4=` antes de decodificar y luego verifica si el resultado decodificado es `admin:admin`.
- **Categoría:** Seguridad Web / Criptografía

## 2. Objetivo
Comprender la maleabilidad de los bits de relleno (*padding bits*) en la codificación Base64 cuando se compara la cadena codificada en lugar del valor decodificado canónico.

## 3. Requisitos
- Cliente HTTP (`curl` o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd extinction/challenge && docker build -t ctf-extinction . && docker run --rm -it -P ctf-extinction
   ```
2. Archivos distribuidos al participante: `distfiles/index.php`.

## 5. Metodología de resolución
Modificar el último carácter antes del signo `=` en `YWRtaW46YWRtaW4=` alterando únicamente los 2 bits inferiores de relleno (por ejemplo, `YWRtaW46YWRtaW5=`), de modo que la cadena Base64 sea distinta pero decodifique exactamente a `admin:admin`.

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
