# project01 - "Rope" Data Structure

![Rope](https://github.com/nbelliot/comp401/blob/master/presentation1/Rope.jpg)

###### Explanation:
A rope is a tree-like data structure that is meant to store a large string.  When a large string is stored in a rope, the string is divided into smaller “fragment” strings and are stored at the lowest branches of the tree.  Storing a large string in this way makes storage and manipulation more efficient.

###### References:
- http://en.wikipedia.org/wiki/Rope_%28data_structure%29
- http://www.ibm.com/developerworks/library/j-ropes/
- https://www.sgi.com/tech/stl/ropeimpl.html
- http://bitsavers.trailing-edge.com/pdf/xerox/parc/techReports/CSL-94-10_Ropes_Are_Better_Than_Strings.pdf

###### Documentation:
- Edit and run `driver.py` to load a rope with text.
- `rope.py` contains rope class - see for methods and comments.
- `balanced_binaryTree.py` contains tree helper class for `rope.py` - no need to see or manipulate.

###### Complexity Analysis:
Operation | Rope | String
--------- | ---- | ------
Build | O(n) | O(n)
Iterate over e/ character | O(n) | O(n)
Index | O(log n) | O(1)
Concatenate | O(log n) | O(n)
Split | O(log n) | O(1)
Insert | O(log n) | O(n)
Delete | O(log n) | O(n)

