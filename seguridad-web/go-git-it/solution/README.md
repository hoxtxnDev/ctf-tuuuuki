# Solución

1. Al visualizar la página web principal no se observa información sensible a simple vista, pero al inspeccionar el código fuente HTML se encuentra una nota de desarrollo (`<!-- dev note: don't forget to unlist the git directory! -->`) que advierte sobre el directorio git listado.
2. Al navegar a la ruta `/git/` se observa el directorio `.git` expuesto con listado de directorios habilitado.
3. Puedes utilizar `curl` o `wget` para descargar recursivamente este directorio e inspeccionarlo localmente.
4. Dentro del directorio git descargado, ejecuta el siguiente comando para verificar qué archivos fueron eliminados en commits anteriores:

    ```bash
    git log --name-status
    ```

5. Una vez identificado el hash del commit donde se eliminó `flag.html`, ejecuta el siguiente comando para recuperar la flag (`DUOC{historial_commits_expuesto_26491}`):

    ```bash
    git show <commit ID> -- <file path>
    ```
