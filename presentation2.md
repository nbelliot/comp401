# Presentation 2 - Beam Search (algorithm)
![beam_search](https://github.com/nbelliot/comp401/blob/master/presentation2/beam_search.jpg)

###### Explanation:
**Beam search** is a search algorithm based off of heuristic where, in a graph, the most promising nodes (with the best heuristic) are expanded.  Beam search is an optimization of best-first search, reducing memory requirements.  Best-first orders all partial solutions (states) by heuristic.  In beam search, the number of best partial solutions is limited by a predetermined quantity (k).  Limiting the number of explored solutions increases memory efficiency but sacrifices completeness (guarantee of solution) and optimality (guarantee of best solution).

Watch this cool video for good explenation on general concept of beam search: https://www.youtube.com/watch?v=G_teUutyC3Y

###### Algorithm:
![algorithm](https://github.com/nbelliot/comp401/blob/master/presentation2/algorithm.jpg)
This is the algorithm in pseudocode for beam search.

###### Pathfinding:
![pathfinding](https://github.com/nbelliot/comp401/blob/master/presentation2/pathfinding.jpg)<br /> 
This a graph.  **S** is the starting point; **G** is the goal.  The numbers between the edges represent *cost* (actual distance between nodes); the numbers inside the nodes represent *heuristic* (straightline distance from node to goal).

![openlist](https://github.com/nbelliot/comp401/blob/master/presentation2/openlist.jpg)
Walk through the grap using the beamsearch algorithm.  Assume memory size is 2 (k=2).  The first two steps have been done for you as example (notice how node C was pruned for you).

Is the path found using beam search the *optimal path* (least amout of total cost)?  What is the optimal path?

Additional Reading:
- http://en.wikipedia.org/wiki/Beam_search
- http://en.wikibooks.org/wiki/Artificial_Intelligence/Search/Heuristic_search/Beam_search
- http://en.wikipedia.org/wiki/Breadth-first_search
