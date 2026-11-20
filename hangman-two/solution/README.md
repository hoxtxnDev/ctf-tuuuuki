Juega al ahorcado para adivinar una cadena alfanumérica aleatoria de 25 caracteres y obtener la flag (`DUOC{persistencia_cookie_estado_58271}`).

* Cada usuario inicia con una palabra aleatoria que se mantiene hasta que el usuario gana, pierde o reinicia la partida.
* Las vidas están asociadas a la cuenta del usuario, pero existe una cookie llamada `state` que identifica la palabra en la base de datos.
* Si registras un nuevo usuario pero reutilizas el valor de la cookie `state` del primer usuario tras cada grupo de 3 intentos, puedes probar todo el alfabeto sin agotar las vidas de una misma cuenta ni reiniciar la palabra objetivo.
* Después de cada intento, consulta la página `/home` para verificar si se ha completado la palabra y obtener la flag antes de que la partida se reinicie.

Para probar el desafío, ejecuta `python3 solution.py http://127.0.0.1:8000`.