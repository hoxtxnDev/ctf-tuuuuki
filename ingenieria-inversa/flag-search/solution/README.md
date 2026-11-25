El programa `flag-search` somete la clave de entrada de 128 bits a una serie de verificaciones aritméticas y de conteo de bits que se aplican sobre prefijos cada vez más largos de la clave, lo que hace que una búsqueda con retroceso (*backtracking*) sea el enfoque natural para podar el espacio de búsqueda.

    $ python3 search.py
    Found key [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1] feca3c730601be7fd57f1f0b668b4637
    Search found 1 for 128 bits


    $ echo 'feca3c730601be7fd57f1f0b668b4637' | netcat 127.0.0.1 11010
    feca3c730601be7fd57f1f0b668b4637
       ***
      *****
      *****
       ***
       |||
       |||\
       ||| .=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.
       ||| |                     ______                     |
       ||| |                  .-"      "-.                  |
       ||| |                 /            \                 |
       ||| |     _          |              |          _     |
       ||| |    ( \         |,  .-.  .-.  ,|         / )    |
       ||| |     > "=._     | )(__/  \__)( |     _.=" <     |
       ||| |    (_/"=._"=._ |/     /\     \| _.="_.="\_)    |
       ||| |           "=._"(_     ^^     _)"_.="           |
       ||| |               "=\__|IIIIII|__/="               |
       ||| |              _.="| \IIIIII/ |"=._              |
       ||| |    _     _.="_.="\          /"=._"=._     _    |
       ||| |   ( \_.="_.="     `--------`     "=._"=._/ )   |
       ||| |    > _.="                            "=._ <    |
       ||| |   (_/                                    \_)   |
       ||| |                                                |
       ||| '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='
       |||/
       |||
       |||                   FLAG-SEARCH
       |||
       |||                HEX MARKS THE SPOT
       |||
       |||                              .
       |||                -----          ..
       |||               /     \           \
       |||              0x      \           |
       |||                      |           /
       |||                      \          /
       |||                       \     ---
       |||                       |    /
       |||                        \  /
       |||                         --
     /:::::\
     :::::::
     =======
    
    Enter 128-bit key:
    Checking key feca3c730601be7fd57f1f0b668b4637
    
    Decrypted flag: DUOC{poda_backtracking_bits_49182}

