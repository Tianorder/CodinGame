# The Travelling Salesman Problem
A contribution by Hackerman007
 Approved by Unihedron,ArglanirandJBM

## Goal
* **The travelling salesman problem (TSP) asks the following question**: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?"
In this puzzle not necessarily the shortest route is the answer but an approximation using a greedy algorithm (which in fact could be the shortest route as well).

This greedy algorithm starts at the first input given and always chooses the nearest point from the current point. This continues until no points are left and the last point is connected to the first point.

Use the euclidian distance, i.e. sqrt(deltaX^2 + deltaY^2), as the distance between two cities. If there are points with the same distance, always pick the one occurring first in the list.

In general, the greedy algorithm does not find the optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a global optimal solution in a reasonable time.

### Input
* **Line 1**: An integer N for the number of points.

### Output
* **Line 1**: The rounded distance calculated using the greedy algorithm.
5 ≤ N ≤ 14
0 ≤ x, y ≤ 100

### Example

    Input

        5
        9 12
        24 15
        12 30
        4 3
        13 27

    Output

        71        