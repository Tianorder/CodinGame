# Logic gates
A contribution by b0n5a1
 Approved by Zorg1,Remi.andWesticles

## Goal
A logic gate is an electronic device implementing a boolean function, performing a logical operation on one or more binary inputs and producing a single binary output.

Given n input signal names and their respective data, and m output signal names with their respective type of gate and two input signal names, provide m output signal names and their respective data, in the same order as provided in input description.

All type of gates will always have two inputs and one output.
All input signal data always have the same length.

The type of gates are :
* **AND **: performs a logical AND operation.
* **XOR **: performs a logical exclusive OR operation.
* **NOR **: performs a logical inverted OR operation.

Signals are represented with underscore and minus characters, an undescore matching a low level (0, or false) and a minus matching a high level (1, or true).

### Input
* **Line 1 **: n number of input signals.
* **n next lines **: two space separated strings **: name of input signal, then signal form.

### Output
* **m lines **: two space separated strings **: name of output signal, then signal form.
1 ≤ n ≤ 4
1 ≤ m ≤ 16

### Example

    Input

        2
        3
        A __---___---___---___---___
        B ____---___---___---___---_
        C AND A B
        D OR A B
        E XOR A B

    Output

        C ____-_____-_____-_____-___
        D __-----_-----_-----_-----_
        E __--_--_--_--_--_--_--_--_        