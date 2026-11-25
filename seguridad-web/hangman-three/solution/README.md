Juega al ahorcado para adivinar la palabra aleatoria y obtener la flag (`DUOC{secreto_jwt_diccionario_91463}`); la restricción es que solo dispones de *4 vidas*.

El contador de vidas perdidas (`life_lost`) se almacena dentro del token JWT en la cookie `access_token_cookie`:
``
 "fresh": false,
  "iat": 1745122377,
  "jti": "4b6e355a-9604-4a87-951a-296a77b148ba",
  "type": "access",
  "sub": "1",
  "nbf": 1745122377,
  "exp": 1745123277,
  "life_lost": "1"
}
``

El token JWT está firmado con una clave secreta débil (`tobemodified`), que puede descubrirse mediante ataque de diccionario utilizando la lista pública de [Wallarm](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list):
`hashcat -a 0 -m 16500 <jwt> secrets.list`

Al forjar un token JWT válido con `"life_lost": "0"`, se obtienen vidas ilimitadas. Para validar el nivel ejecuta `python solution.py <CHALLENGE-URL>`