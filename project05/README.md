# project05 - "Music Notator" Visual Algorithm

###### Explanation:
**Music Notator** notates a melodic line that is calculated by searching through a randomly generated tree with the A* algorithm.<br /> 
First, a tree is generated with a predetermined breadth (*b*) and depth (*d*).  Each node of the tree represents a musical note and holds two randomly generated values: *g* and *h*.  The value *g* represents the pitch of the note and the value *h* represents the rhythmic value of the note.<br />
Then, the search algorithm A* (*f(n) = g(n) + h(n)*) is applied to the completely generated tree.  *f(n)* is the total path cost to node *n*, *g(n)* is the total cost of the difference between *g* values of all consecutive nodes up to node *n*, and *h(n)* is the total cost of the difference between *h* values of all consecutive nodes up to node *n*.  Therefore, *f(n)* is the balanced consideration between melodic and rhythmic coherence.  A* stops at depth of *d*. This is the optimal path, of the lowest *f(n)* cost.<br />
After A* finds the optimal path, it returns the string of nodes of the optimal path, length *d*.  Using the 3rd party “Python Music Generator” library, a MIDI file is initialized. The g and h values are extracted from the nodes and converted from numeric values to MIDI notes with *g* pitch and *h* rhythmic value for each node, saving each musical note to the MIDI file.  Once the musical notes are saved to the MIDI file, it is exported and saved to the local folder, available to play.<br />
Similarly, using a 3rd party music package, “mingus,” built in sheet music notator, “LilyPond,” a pdf file is exported.

###### Documentation:
- Run `driver.py` edit and run to generate a tree with depth (*d*) and bredth (*b*), search generated tree using A* algorithm to find optimal path (melody), generate melody as a MIDI file, and generate medlody as pdf file.
- `music_notator.py` contains music_notator class - extracts *g* and *h* values from nodes and notates corresponding notes on staff paper, exported as pdf.
- `music_generator.py` contains music_generator class - extracts *g* and *h* values from nodes and exports MIDI file with corresponding notes.
- `a_star.py` contains AStar class - searches problem set (tree) for optimal path using function *f(n) = g(n) + h(n)*.
- `node_sort.py` conains helper function for `a_star.py` - implementation of quicksort on array of nodes, sorting by heuristics of nodes - no need to see or manipulate.
- `tree.py` contains tree class - implementation of tree with depth (*d*) and bredth (*b*) - no need to see or manipulate.

###### References:
Must have the following packages installed to run:
- https://code.google.com/p/mingus/
- https://code.google.com/r/earsbender-python-music-gen/source/browse/
