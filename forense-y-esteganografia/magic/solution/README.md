# Magic

El nombre y la descripción del desafío sugieren que hay un problema con los "magic bytes" (firma de cabecera) de la imagen, razón por la cual no se puede abrir.

Puedes utilizar una herramienta hexadecimal como `xxd` o `hexedit` para examinar y editar los primeros bytes del archivo.

Los primeros bytes de un archivo determinan su formato. Para imágenes PNG, la firma de cabecera debe comenzar con `8950 4e47` (`\x89PNG`), pero `magic.png` comienza con `616e 7368`.

Restaurar la cabecera con los magic bytes correctos de PNG permite abrir la imagen y obtener la flag (`DUOC{reparacion_firma_cabecera_76392}`).
