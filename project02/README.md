# project02 - "Beam Search" Search Algorithm

![beam_search](https://github.com/nbelliot/comp401/blob/master/presentation2/beam_search.jpg)

###### Explanation:
A rope is a tree-like data structure that is meant to store a large string.  When a large string is stored in a rope, the string is divided into smaller “fragment” strings and are stored at the lowest branches of the tree.  Storing a large string in this way makes storage and manipulation more efficient.

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
