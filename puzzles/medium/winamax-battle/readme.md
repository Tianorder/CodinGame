# War
 
[![Cards_Winamax_LD ](/Cards_Winamax_LD .jpg)](Cards_Winamax_LD )

## ⚽The Goal
* **Let's go back to basics with this simple card game**: war!
Your goal is to write a program which finds out which player is the winner for a given card distribution of the "war" game.

## ✔Rules
* **War is a card game played between two players. Each player gets a variable number of cards of the beginning of the game**: that's the player's deck. Cards are placed face down on top of each deck.
* **Step 1 **: the fight
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.
 
* **Step 2 **: war
 
Special cases:
If a player runs out of cards during a "war" (when giving up the three cards or when doing the battle), then the game ends and both players are placed equally first.
The test cases provided in this puzzle are built in such a way that a game always ends (you do not have to deal with infinite games)
* **Each card is represented by its value followed by its suit**: D, H, C, S. For example**: 4H, 8C, AS.
When a player wins a battle, they put back the cards at the bottom of their deck in a precise order. First the cards from the first player, then the one from the second player (for a "war", all the cards from the first player then all the cards from the second player).

For example, if the card distribution is the following:
* **Player 1 **: 10D 9S 8D KH 7D 5H 6S
Then after one game turn, it will be:
* **Player 1 **: 5H 6S 10D 9S 8D KH 7D 10H 7H 5C QC 2C
 
Victory Conditions
A player wins when the other player no longer has cards in their deck.

## 📑Game Input

### Input
* **Line 1**: the number N of cards for player one.
* **N next lines**: the cards of player one.
* **Next line**: the number M of cards for player two.
* **M next lines**: the cards of player two.

### Output
* **If players are equally first**: PAT

### Constraints
* 0 < N, M < 1000

### Example

    Input

        3
        AD
        KC
        QC
        3
        KH
        QS
        JC

    Output

        1 3        