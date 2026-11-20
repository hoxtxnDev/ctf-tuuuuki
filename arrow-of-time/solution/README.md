Este desafío aprovecha el hecho de que un hash truncado a 64 bits presenta ciclos de longitud $O(2^{32})$. No es viable obtener por fuerza bruta la preimagen de cada MD5 por varias razones:

* Hacerlo requiere un trabajo de orden $O(2^{64})$ y hay demasiadas iteraciones que calcular.
* Existen colisiones, por lo que no se sabe qué rama hacia atrás tomar.

En su lugar, se calcula la longitud del ciclo iterado para uno de los hashes mostrados en el video y luego se utiliza la marca de tiempo de ese hash para retroceder en el tiempo avanzando hacia adelante en el ciclo. Consulta `md5_brent.c` para la detección de ciclos mediante el algoritmo de Brent y la función de solución:


    void solve() {
    
        int64_t t_known = 1999634432; /* Known, possibly future time */
        int64_t t_goal = 1742826261;  /* Current time */
        int64_t cycle_len = 3385752161;
    
        int64_t steps = (cycle_len - (t_known - t_goal)) % cycle_len;
    
        const EVP_MD *md = EVP_md5();
        EVP_MD_CTX *mdctx = EVP_MD_CTX_create();
    
        uint8_t x[EVP_MAX_MD_SIZE];
    
        memset(x, 0, EVP_MAX_MD_SIZE);
    
        x[0] = 0xef;
        x[1] = 0x2e;
        x[2] = 0x01;
        x[3] = 0x01;
        x[4] = 0xb4;
        x[5] = 0xff;
        x[6] = 0x85;
        x[7] = 0xde;
    
        fprintf(stderr, "Running %lld steps to find state at %lld from %lld\n", steps, t_goal, t_known);
        uint64_t progress = steps / 100;
        for (int64_t i = 0; i < steps; i++) {
            if (i % progress == 0) {
                fprintf(stderr, ".");
            }
            (void)md5(mdctx, md, x, TRUNCLEN, x);
        }
    
        printf("\nState found: ");
        for (int i = 0; i < TRUNCLEN; i++) {
            printf("%02x", x[i]);
        }
        printf("\n");
    
    }


Dado que esto tardará algunos minutos en ejecutarse, conviene calcular un estado correspondiente a un instante reciente y luego avanzar rápidamente desde ese instante:

    #!/usr/bin/env python
    
    import sys
    import hashlib
    
    # Use faster code like md5_brent.c to find
    # a recent state that you can
    # quickly fast-forward
    known_t = 1742837767
    known_cstate = bytes.fromhex("cc9ef28a7f481569")
    
    def md5_trunc(input_bytes: bytes) -> bytes:
        if len(input_bytes) != 8:
            raise ValueError("Input must be exactly 8 bytes (64 bits).")
    
        # Compute MD5 hash
        md5_hash = hashlib.md5(input_bytes).digest()
    
        # Return the first 8 bytes (64 bits)
        return md5_hash[:8]
    
    
    cstate = known_cstate
    for i in range(int(sys.argv[1]) - known_t):
        cstate = md5_trunc(cstate)
    
    print(cstate.hex())

Then solving:

    [...]
    The current time is 2025-03-24 21:04:32 (1742850272).
    What is the current state? You have 30 seconds.

    State = ? 983630b0180d8cc4
    983630b0180d8cc4
    DUOC{ciclo_colision_brent_59184}


Nota técnica: al aprovechar el ciclo se asume que el reloj se encuentra actualmente dentro del bucle principal del ciclo y no en una de las ramas previas que desembocan en él. El desafío fue construido específicamente de modo que el estado del reloj ya se encuentre dentro del ciclo para garantizar que sea resoluble.
