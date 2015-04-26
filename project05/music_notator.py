import mingus.core.notes as notes
from mingus.containers.Bar import Bar
from mingus.containers.Track import Track
from mingus.containers.Composition import Composition
from mingus.extra.LilyPond import *

class Node:    
    def __init__(self, g=0, h=0):
        self.left = None
        self.right = None
        self.parent = None
        self.g = g
        self.h = h
        self.f = 0

melody = [Node(60,4), Node(61,4), Node(62,4), Node(63,4), Node(67,4)]

c = Composition()
c.set_author('Nicholas Elliot', 'elliot_nicholas@wheatoncollege.edu')
c.set_title('A* Generated Melodic Line')

b = Bar()
t = Track()

for i in melody:
    n = Note()
    n.from_int(i.g)
    b.place_notes(n, i.h)
    print b.current_beat * b.length
    if (b.current_beat * b.length) < ((1 / i.h) * b.length):
        t.add_bar(b)
        b = Bar()
        b.place_notes(n, i.h)
    else:
        b.place_notes(n, i.h)

t.add_bar(b)
c.add_track(t)

to_png(from_Composition(c), "out.png")