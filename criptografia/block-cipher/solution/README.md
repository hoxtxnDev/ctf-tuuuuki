## `block-cipher` es un esquema de codificación de texto a imagen.

Los usuarios ingresan una "clave" y algunas palabras separadas por espacios. Las palabras se codifican de 3 letras a la vez en bloques grandes. Los bloques grandes se dividen en tres sub-bloques: un rectángulo de 1x2 y dos cuadrados de 1x1. La clave acepta los números del 1 al 4 y, según el valor, intercambia la posición de los sub-bloques dentro de un bloque grande. El efecto de la clave es menor y puede leerse directamente desde la imagen.

La idea es comenzar probando mensajes cortos como "a", luego "b", "c", y así sucesivamente. Debería hacerse evidente un patrón de cambios en los sub-bloques. Usando una clave de "1", el sub-bloque cuadrado superior izquierdo cambiará en esta secuencia repetitiva:

![a0](imgs/a_0.png) ![a1](imgs/a_1.png) ![a2](imgs/a_2.png) ![a3](imgs/a_3.png) ![a4](imgs/a_4.png)

Cuando este bloque completa su ciclo, cambia el siguiente sub-bloque cuadrado siguiendo esta secuencia:

![b0](imgs/b_0.png) ![b1](imgs/b_1.png) ![b2](imgs/b_2.png) ![b3](imgs/b_3.png) ![b4](imgs/b_4.png)

Cuando el segundo sub-bloque cuadrado completa su ciclo, el sub-bloque mayor de 1x2 sigue esta secuencia:

![c0](imgs/c_0.png) ![c1](imgs/c_1.png) ![c2](imgs/c_2.png) ![c3](imgs/c_3.png) ![c4](imgs/c_4.png) ![c5](imgs/c_5.png) ![c6](imgs/c_6.png)

Los símbolos de los tres sub-bloques actúan como dígitos en base 5, 5 y 7. Una vez que han completado su ciclo, se agregan rotaciones de 90 grados al primer sub-bloque, luego rotaciones de 90 grados al segundo y de 180 grados al tercero. Finalmente, cuando todas esas rotaciones completan su ciclo, el bloque completo rota en incrementos de 90 grados.

En total, un bloque grande codifica un número de base mixta (5, 5, 7, 4, 4, 2, 4), donde la parte (5, 5, 7) corresponde a los símbolos de los tres sub-bloques, la parte (4, 4, 2) a las rotaciones de los sub-bloques, y el 4 final a la rotación del bloque completo. Esto permite que cada bloque grande codifique $\log(5 \times 5 \times 7 \times 4 \times 4 \times 2 \times 4) / \log(27) = 3.039$ dígitos en base 27. Así cada bloque grande codifica 3 letras simultáneamente ($a = 1, b = 2, \dots, z = 26$; el dígito cero se usa únicamente como relleno cuando hay menos de 3 letras).

Existe una marca semicircular en el borde del bloque grande que muestra tanto la rotación del bloque grande como si el dígito de la clave ha intercambiado el sub-bloque 1x2 con los dos sub-bloques cuadrados 1x1. La rotación del bloque grande debe deshacerse antes de leer las rotaciones de los sub-bloques.

## Lectura de la clave

Al experimentar con las claves del 1 al 4 se puede determinar que:

- 1: sin efecto
- 2: intercambia la posición de los sub-bloques cuadrados
- 3: intercambia el sub-bloque 1x2 con los sub-bloques cuadrados
- 4: mismo efecto que 2 y 3 combinados (doble intercambio)

Aquí se muestra la imagen de la flag anotada con el dígito de clave para cada bloque grande:

![key](imgs/key.png)

Como se observa, la clave es "121314".


## Lectura de la rotación del bloque grande

La muesca semicircular en el borde permite identificar cómo se ha rotado el bloque completo. Comienza en la parte superior y rota en sentido horario hacia la derecha, abajo y finalmente a la izquierda.

Aquí se muestra la flag anotada con la rotación de los bloques grandes:
![large rotations](imgs/large_rotations.png)

Por casualidad, el valor de rotación final "3" no se utiliza porque ninguno de los bloques de 3 letras termina con una letra suficientemente alta en el alfabeto.


## Lectura de los sub-bloques

Cada sub-bloque aporta dos dígitos: el número de símbolo del bloque y su rotación. Es sencillo identificar a simple vista qué símbolo corresponde a cada sub-bloque; para determinar su rotación, primero debe deshacerse mentalmente la rotación del bloque grande.

A continuación se muestran todos los sub-bloques anotados con su número de símbolo en fuente grande y su rotación en fuente pequeña:

![sub block details](imgs/sub_block_notation.png)

    #!/usr/bin/env python3
    
    
    def block_to_n(bl):
    
        radix = (5, 5, 7, 4, 4, 2, 4)
    
        n = 0
    
        for i in range(len(radix) - 1, -1, -1):
            n *= radix[i]
            n += bl[i]
    
        return n

    
    def num_to_let(num):
    
        if num == 0:
            return ''
    
        return chr(ord('a') + (num - 1))
    
    
    def n_to_trip(n):
    
        if n >= 19683:
            n -= 19683
            d1 = n % 11
            n //= 11
            d2 = n % 11
            n //= 11
            d3 = n
            return (chr(ord('0') + d1 - 1) if d1 else '') + (chr(ord('0') + d2 - 1) if d2 else '') + (chr(ord('0') + d3 - 1) if d3 else '')

        l1num = n % 27
        n //= 27
        l2num = n % 27
        n //= 27
        l3num = n
    
        return num_to_let(l1num) + num_to_let(l2num) + num_to_let(l3num)
    
    
    def decode_word(bll):
    
        word = ''
        for bl in bll:
            n = block_to_n(bl)
            #print(f"Got {n} for {bl}")
            word += n_to_trip(n)
    
        return word
    
    
    w1_bll = [(4, 4, 6, 2, 0, 1, 0),
              (2, 1, 3, 2, 1, 0, 1),
              (2, 3, 4, 0, 3, 0, 0),
              (0, 4, 4, 0, 3, 1, 1)]
    w1 = decode_word(w1_bll)
    
    w2_bll = [(1, 2, 6, 0, 0, 1, 0),
              (2, 1, 5, 3, 0, 0, 0)]
    w2 = decode_word(w2_bll)
    
    w3_bll = [(2, 0, 3, 1, 1, 0, 3),
              (2, 4, 1, 0, 0, 0, 0)]
    w3 = decode_word(w3_bll)
    
    w4_bll = [(4, 3, 4, 1, 1, 1, 3),
              (0, 4, 0, 1, 0, 1, 3)]
    w4 = decode_word(w4_bll)
    
    
    print(f"DUOC{{{w1}_{w2}_{w3}_{w4}}}")


Al ejecutarse, produce la flag configurada:

    $ ./decode_blocks.py
    DUOC{codificacion_radix_mixta_84619}


## Método de solución alternativo

En lugar de modelar matemáticamente cada detalle de la codificación, los participantes pueden observar que cada bloque corresponde a 3 letras y buscar o probar manualmente cada bloque de 3 letras utilizando el servicio web del desafío. Una vez que se conoce parte de una palabra, resulta más sencillo deducir los bloques restantes.

