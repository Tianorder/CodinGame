# Clash of Code - Shortest mode
 Approved by __yel__p,asasas1111andGuillaumeLEFEBVRE

## Goal
Sum each set of 3 consecutive numbers in the first N natural numbers (natural numbers are positive integers).
* **Ex**: N = 5, you will have to calculate 1 + 2 + 3, 2 + 3 + 4, 3 + 4 + 5
What you do with the sums depends on how many sums there are.

If there are an even number of sums, add and subtract the sums alternatingly, starting with addition. If a, b, c, d, e, and f were the sums, you would calculate a + b - c + d - e + f

If there are an odd number of sums, add and subtract the sums alternatingly, starting with subtraction. If a, b, c, d, and e were the sums, you would calculate a - b + c - d + e

Print the result.

### Input
One integer N, which is the amount of natural numbers you have to deal with

### Output
The result of the operations on the first N natural numbers as described above

### Constraints
* 3 <= N <= 1000

### Example

    Input

        5

    Output

        9        