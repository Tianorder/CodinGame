# Clash of Code - Shortest mode
A contribution by PolentaEater
 Approved by C26_1,BartholomewIIIandJbagher

## Goal
The 1-dimensional Ising model is an idealized physical system made of a chain of "spins". Each spin is a discrete variable that takes either the value +1 or -1. Each pair of neighboring spins contribute an amount +J to the energy of the system if the two spins have opposite values, or -J if they have the same value. For example, in the four-spin chain

++--

the two pairs '++' and '--' contribute -J while the pair '+-' contribute +J, adding up to a total energy of -J.

Given a chain of N spins, compute its total energy in units of J.

### Input
* **Line 1**: an integer N, the number of spins.

### Output
An integer E, the total energy in units of J.

### Constraints
* 0 < N < 10000

### Example

    Input

        4
        ++--

    Output

        -1        