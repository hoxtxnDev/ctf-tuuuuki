## Cómo resolverlo
Este desafío está inspirado en el caso de las [cartas prototipo de Pokémon](https://www.elitefourum.com/t/many-of-the-pokemon-playtest-cards-were-likely-printed-in-2024/52421).

Las cartas fueron "impresas" con una impresora que añade diminutos [puntos amarillos de rastreo (Machine Identification Codes)](https://en.wikipedia.org/wiki/Printer_tracking_dots) en el [formato de cuadrícula Xerox DocuColor](https://w2.eff.org/Privacy/printers/docucolor/).

Los puntos son más visibles en el canal de color azul. A continuación se muestra una superposición sobre una carta destacando la cuadrícula:
![dot image example](annotated_solution.png)


* Hay 29 cartas: una por cada letra del alfabeto, `{`, `}` y una carta especial firmada para `f`.
* La última columna de cada carta codifica el carácter ASCII de 7 bits.
* Las cartas impresas en 1998 (96 en el código de puntos original) son auténticas. Las cartas impresas en 2024 son falsificaciones.
* Solo las cartas auténticas forman parte de la flag estandarizada `DUOC{matriz_puntos_amarillos_95173}`.
* Al ordenar las cartas auténticas cronológicamente por su minuto de impresión se obtiene la secuencia oculta.
