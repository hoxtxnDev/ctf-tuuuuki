# Guía de Solución — `moa-station` (MoA Station)

## Categoría
Seguridad Web / Extensiones de Navegador

## Procedimiento de Resolución
La extensión almacena la flag en `localStorage.setItem('secret', ...)` dentro de `background.js`. El archivo `solution/exploit.html` simula los eventos de teclado requeridos por el script de contenido para inyectar una etiqueta `<script>` que abusa de un endpoint con soporte `callback` permitido en la CSP de la extensión y exfiltra `localStorage.getItem('secret')`.

## Flag Esperada
```text
DUOC{eventos_teclado_extension_61839}
```
