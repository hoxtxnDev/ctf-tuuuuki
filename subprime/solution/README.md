# subprime

Este desafío se centra en las debilidades criptográficas de RSA cuando los números primos iniciales elegidos son demasiado pequeños.

## Solución

1. Los participantes reciben un texto cifrado compuesto por un arreglo de enteros junto con una clave pública formada por el exponente público ($e$) y el módulo ($n$).
2. Si los números primos iniciales $p$ y $q$ son lo suficientemente pequeños, una computadora puede derivarlos fácilmente a partir del módulo ($n$) mediante factorización prima.
3. A continuación, basta con calcular $\phi(n) = (p-1)(q-1)$ y el exponente privado $d \equiv e^{-1} \pmod{\phi(n)}$ para descifrar cada entero del arreglo.
4. Al observar el rango de los números descifrados, se comprueba que corresponden a códigos ASCII.

Received n = 98563159, e = 1009

Attempting to find prime factors p and q from n...

Found primes: p = 9883, q = 9973

Calculated phi(n) = 98543304

Verified: gcd(e, phi) = gcd(1009, 98543304) = 1

Calculating private exponent d...

--- RSA Key Information ---

Smaller prime p: 9883

Larger prime q:  9973

Modulus n:       98563159

Phi(n):          98543304

Public Key (e, n):  (1009, 98563159)

Private Key (d, n): (31545577, 98563159)

Received ciphertext to decode: [23637004, 83925846, 2209113, 27583995, 30323096, 31771886, 30323096, 75901128, 31771886, 53482472, 97809030, 69683388, 68450410, 39905961, 75846723, 75901128, 53482472, 56293282, 69683388, 68450410, 63432789, 9450820, 81966837]

Decoding using Private Key (d=31545577, n=98563159)...

--- Decryption Result ---

Decoded message (numeric): [67, 84, 70, 123, 110, 48, 110, 95, 48, 112, 116, 33, 109, 64, 108, 95, 112, 82, 33, 109, 51, 36, 125]

Plaintext: DUOC{exponente_privado_factorizado_51739}

## Recursos

Existen diversas herramientas de apoyo para comprender esta operación cuando los factores primos son pequeños, por ejemplo [BabyRSA](https://github.com/mrdebator/BabyRSA).
