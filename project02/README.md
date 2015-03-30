# project02 - "Beam Search" Search Algorithm

![beam_search](https://github.com/nbelliot/comp401/blob/master/presentation2/beam_search.jpg)

###### Explanation:
**Beam search** is a search algorithm based off of heuristic where, in a graph, the most promising nodes (with the best heuristic) are expanded.  Beam search is an optimization of best-first search, reducing memory requirements.  Best-first orders all partial solutions (states) by heuristic.  In beam search, the number of best partial solutions is limited by a predetermined quantity (k).  Limiting the number of explored solutions increases memory efficiency but sacrifices completeness (guarantee of solution) and optimality (guarantee of best solution).

###### References:
- http://en.wikipedia.org/wiki/Beam_search
- http://en.wikibooks.org/wiki/Artificial_Intelligence/Search/Heuristic_search/Beam_search
- http://en.wikipedia.org/wiki/Breadth-first_search
- http://en.wikipedia.org/wiki/Quicksort

###### Documentation:
- Run `driver.py` edit and run to generate a tree with depth (d) and bredth (b) and search generated tree using Beam Search algorithm to find "shortest" path.
- `beam_search.py` contains Beam Search class - see for methods and comments.
- `node_sort.py` conains helper function for `beam_search.py`; implementation of quicksort on array of nodes, sorting by heuristics of nodes - no need to see or manipulate.
- `tree.py` contains tree helper class for `beam_search.py`; implementation of tree with depth d and bredth b - no need to see or manipulate.

###### Complexity Analysis:
Performance | Space
--------- | ----
O(k^d) | O(k)
k - memory size, d - depth
