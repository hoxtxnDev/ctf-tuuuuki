# Desafío CTF: `detector` — Dragon Detector

## 1. Introducción
Herramienta web en PHP para diagnóstico de red que bloquea caracteres especiales únicamente mediante validación JavaScript en el navegador.
- **Categoría:** Seguridad Web / Pwn

## 2. Objetivo
Demostrar por qué los controles de validación del lado del cliente no sustituyen la sanitización y parametrización en el servidor.

## 3. Requisitos
- Cliente HTTP (`curl`, navegador o Ruby con `httparty`).

## 4. Instrucciones de ejecución
1. Para construir y ejecutar el contenedor del desafío con Docker:
   ```bash
   cd detector/challenge && docker build -t ctf-detector . && docker run --rm -it -P ctf-detector
   ```
2. Archivos distribuidos al participante: `distfiles/detect-dragon.php`, `distfiles/index.php`.

## 5. Metodología de resolución
Enviar la solicitud HTTP directamente al endpoint `detect-dragon.php` omitiendo la validación JavaScript del formulario para concatenar la lectura del archivo `/app/dragon-detector-ai`.

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
