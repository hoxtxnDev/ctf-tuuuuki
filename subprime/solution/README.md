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

Received ciphertext to decode: [68615770, 58616983, 50194529, 23637004, 27583995, 35504906, 97616453, 53482472, 58166381, 30323096, 35504906, 30323096, 97809030, 35504906, 75901128, 53482472, 63746616, 93000364, 41806842, 86660678, 27951473, 58166381, 75901128, 74647548, 86660678, 65487275, 97809030, 58166381, 63746616, 93000364, 80381793, 86660678, 27951473, 58166381, 75901128, 93205851, 93397721, 53786144, 63432789, 70367105, 81966837]

Decoding using Private Key (d=31545577, n=98563159)...

--- Decryption Result ---

Decoded message (numeric): [68, 85, 79, 67, 123, 101, 120, 112, 111, 110, 101, 110, 116, 101, 95, 112, 114, 105, 118, 97, 100, 111, 95, 102, 97, 99, 116, 111, 114, 105, 122, 97, 100, 111, 95, 53, 49, 55, 51, 57, 125]

Plaintext: DUOC{exponente_privado_factorizado_51739}

## Recursos

Existen diversas herramientas de apoyo para comprender esta operación cuando los factores primos son pequeños, por ejemplo [BabyRSA](https://github.com/mrdebator/BabyRSA).
