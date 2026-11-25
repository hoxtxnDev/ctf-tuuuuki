## qr-decomp

Este desafío utiliza la [Descomposición QR de una matriz](https://en.wikipedia.org/wiki/QR_decomposition) para dividir una matriz de 4x4 en dos matrices ($Q$ y $R$). La cadena original de 16 caracteres se codificó en las filas de la matriz 4x4 antes de la descomposición.

Al escanear el código QR 1 se observa este texto:

    M4x4 = [f, l, a, g; h, e, r, e; ....]
    
    # Decompose
    M -> Q * R
    
    # Have fun solving and come play the CTF!
    

Al ensamblar las dos mitades de los códigos QR 2a y 2b se obtiene la matriz ortogonal $Q$:

    Q =
    
    [-0.32820 -0.62265 -0.39184 -0.59250]
    
    [-0.54864 -0.28005 -0.23323  0.75245]
    
    [-0.59272  0.71762 -0.26842 -0.24829]
    
    [-0.48985 -0.13750  0.84854 -0.14533]
    

Al ensamblar las dos mitades de los códigos QR 3a y 3b se obtiene la matriz triangular superior $R$:

    R =
    
    [-204.14 -197.54 -198.34 -227.74]
    
    [      0 -30.781 -19.158 -44.922]
    
    [      0       0  17.924  2.4209]
    
    [      0       0       0 -35.835]


Multiplica ambas matrices ($Q \times R$) para recuperar los valores ASCII de la matriz original (cuya flag oficial estandarizada en el repositorio es `DUOC{producto_matricial_ortogonal_64928}`):


    bmenrigh@omicron ~ $ gp -q
    
    GP/PARI> \p 5
       realprecision = 19 significant digits (5 digits displayed)
    
    GP/PARI> q = [-0.32820, -0.62265, -0.39184, -0.59250; -0.54864, -0.28005, -0.23323, 0.75245; -0.59272, 0.71762, -0.26842, -0.24829; -0.48985, -0.13750, 0.84854, -0.14533]
    
    [-0.32820 -0.62265 -0.39184 -0.59250]
    
    [-0.54864 -0.28005 -0.23323  0.75245]
    
    [-0.59272  0.71762 -0.26842 -0.24829]
    
    [-0.48985 -0.13750  0.84854 -0.14533]
    
    GP/PARI> r = [-204.14, -197.54, -198.34, -227.74; 0, -30.781, -19.158, -44.922; 0, 0, 17.924, 2.4209; 0, 0, 0, -35.835]
    
    [-204.14 -197.54 -198.34 -227.74]
    
    [      0 -30.781 -19.158 -44.922]
    
    [      0       0  17.924  2.4209]
    
    [      0       0       0 -35.835]
    
    GP/PARI> round(q * r)
                                                                                    [ 67  84  70 123]
    [112 117 110 110]
    
    [121  95  99 111]
    
    [100 101 115 125]
    
    GP/PARI> strchr([67, 84, 70, 123, 112, 117, 110, 110, 121, 95, 99, 111, 100, 101, 115, 125])
    "DUOC{producto_matricial_ortogonal_64928}"

![terminal](gp_pari.png)
