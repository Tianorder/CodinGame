# Clash of Code - Fastest mode
 Approved by Emixamexc,Unnamed CodinGamerandbasiliclebogoss

## Goal
Suppose Zeno wishes to walk to the end of a path. Before she can get there, she must get halfway there. Before she can get halfway there, she must get a quarter of the way there. Before traveling a quarter, she must travel one-eighth; before an eighth, one-sixteenth; and so on.
Zenos every time she makes a step she travels the distance mentioned earlier
What will be the distance that she travelled after s steps

example:
start = 0
end = 100
steps = 5
in step 1 she will travel the distance 50.0
in step 2 she will travel the distance 75.0
in step 3 she will travel the distance 87.5
in step 4 she will travel the distance 93.75
in step 5 she will travel the distance 96.875
96.875 round up will be 97
so the output should be 97

### Input
* **line 1 **: start **: integer the position where Zeno will start
* **line 3 :steps **: integer how many steps will she take
output the distance that zeno travelled after s steps rounded

### Constraints
* 0 <= start <= 10**4
* 0 <= end <= 10**8
* 0 <= steps <= 100
* start < end

### Example

    Input

        0
        100
        5

    Output

        97        