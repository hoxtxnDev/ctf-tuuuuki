Ejecuta `solution.py <challenge-url>` para verificar el funcionamiento de Firebase y del servidor, y obtener la flag (`DUOC{prediccion_semilla_aleatoria_39846}`).

Ejecuta `solution.py` sin argumentos para calcular las predicciones de cada ronda a partir de la semilla de Mersenne Twister e ingresarlas en la aplicación Android.

Si deseas utilizar el hook de Frida para resolver el desafío dinámicamente:
* Configura un dispositivo virtual Android (AVD) con la imagen `Android 13.0 ('Tiramisu') | arm64 with Google APIs`
* Instala `soothsayer.apk` en el emulador
* `adb root` 
* `adb push frida-server /data/local/tmp/frida-server`
* `adb shell chmod 755 /data/local/tmp/frida-server`
* `adb shell /data/local/tmp/frida-server &`
* `frida -U -f com.bsidessf.soothsayer -l solver.js`
* En la aplicación, pulsa el botón "Reset" y luego el botón "Get Flag"
* La flag se imprimirá en la consola de Frida (`DUOC{prediccion_semilla_aleatoria_39846}`).
