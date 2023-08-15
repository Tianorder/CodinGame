# Rugby score
A contribution by Bob
 Approved by TwoSteps,MadKnightandUljahn

## Goal
Given a rugby score, your program must compute the different scoring combinations that lead to that particular score.
As a reminder:
  - a try is worth 5 points
  - after a try, a transformation kick is played and is worth 2 extra points if successful
  - penalty kicks and drops are worth 3 points

### Input
* **Line 1**: the score
* **N lines**: number of tries, number of transformations, number of penalties / drops, separated by spaces

### Constraints
* No impossible scores are given, there is always at least one valid combination.

### Example

    Input

        12

    Output

        0 0 4
        2 1 0        