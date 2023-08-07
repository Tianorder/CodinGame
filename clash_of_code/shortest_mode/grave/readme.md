# Clash of Code - Shortest mode
 Approved by jk_java,ChaudropandNowan

## Goal
You find yourself exploring a place, looking for your grandfather's grave.
Given a particular layout, output your chance to find it with only one try.

The place you're exploring is delimited by symbols -, +, and | as follows:
+--+
| +|
| ||
+--+
As you can see, each grave you'll be able to find inside this area is represented by a + with a | below.
You have to count the graves and give the chance (percentage, rounded) that, if you pick any of them, it will be the one you're looking for.

### Input
* **Line 1 **: An integer n, for the graveyard's size.

### Output
* **Line 1 **: Chance (%) to find grandpa's grave directly, rounded.
3 < n < 50

### Example

    Input

        5
        +---+
        |+  |
        ||  |
        |   |
        +---+

    Output

        100%        