## `cipher-block-corruption` -- desafío de descifrado AES-CBC sin IV

A los participantes se les entrega una imagen PNG cifrada con la flag y el script en Python que muestra cómo fue cifrada. La clave AES está incrustada en el script de Python, pero no se especificó el vector de inicialización (IV), por lo que la biblioteca criptográfica (PyCryptodome) eligió uno aleatorio.

El modo de operación CBC se recupera automáticamente tras bloques corruptos: dado que cada bloque de texto plano $P_i = D_K(C_i) \oplus C_{i-1}$ depende únicamente del bloque cifrado actual y del anterior, el desconocimiento del IV solo corrompe el primer bloque (los primeros 16 bytes), mientras que todos los bloques siguientes se descifran correctamente. Como el archivo original es una imagen PNG cuya cabecera de 16 bytes es fija y conocida, el primer bloque se restaura de forma directa:

    #!/usr/bin/env python3
    
    from Crypto.Cipher import AES # pycryptodome
    
    with open("flag.png.enc", "rb") as enc:
        enc_bytes = enc.read()
    
    K = bytes.fromhex("5f4dcc3b5aa765d61d8327deb882cf99")
    aes = AES.new(K, AES.MODE_CBC)
    
    F = aes.decrypt(enc_bytes)
    
    # We don't have the IV so the first block (16 bytes) will be
    # corrupted but since this is a PNG we can predict exactly
    # what those 16 bytes should be:
    # 00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
    HDR = b'\x89PNG\x0d\x0a\x1a\x0a\x00\x00\x00\x0dIHDR'
    
    with open("dec_flag.png", "wb") as flag:
        flag.write(HDR + F[16:])

Nota: debido al relleno (padding), habrá bytes nulos adicionales al final del archivo, los cuales son ignorados por cualquier biblioteca de visualización PNG.

La flag es: DUOC{cabecera_png_sin_iv_41827}
