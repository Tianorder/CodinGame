# Clash of Code - Fastest mode
 Approved by presidentaz,RyzeonandThisIs5am

## Goal
Definition 1.
n!!…! = n(n−k)(n−2k)…(n mod k), if k doesn’t divide n;
n!!…! = n(n−k)(n−2k)…k, if k divides n
(There are k ! marks in the both cases).

* **For example**: 3! = 3·2·1; 10!!! = 10·7·4·1.
Definition 2. X mod Y — a remainder after division of X by Y.

* **For example**: 10 mod 3 = 1;
Given numbers n and k you have to calculate a value of the expression in the first definition.

### Input
* **Line 1**: An integer n.

### Output
* **Line 1**: An integer n!!…! (there are k marks ! here).
1 ≤ n ≤ 10
1 ≤ k ≤ 20

### Example

    Input

        9
        !!

    Output

        945        