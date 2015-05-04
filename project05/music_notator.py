from a_star import *
import mingus.core.value as value
from mingus.containers.Note import Note
from mingus.containers.Bar import Bar
from mingus.containers.Track import Track
from mingus.containers.Composition import Composition
from mingus.extra.LilyPond import *

class music_notator:
    def __init__(self, melody, key='C', meter=(4,4)):
        self.melody = melody

        c = Composition()
        c.set_author('Nicholas Elliot', 'elliot_nicholas@wheatoncollege.edu')
        c.set_title('A* Generated Melodic Line')
        
        b = Bar(key, meter)
        t = Track()
        
        for note in self.melody:
            n = Note()
            n.from_int(note.g)
            print n
            if b.current_beat + 1.0/note.h < b.length:
                b.place_notes(n, note.h)
            elif b.current_beat == b.length:
                t.add_bar(b)
                b = Bar(key, meter)
                b.place_notes(n, note.h)
            else:
                remain = b.length - b.current_beat
                if float(remain**-1).is_integer():
                    b.place_notes(n, remain**-1, "~")
                else:
                    left = remain
                    for v in value.base_values:
                        if left >= 1.0/v:
                                left -= 1.0/v
                                b.place_notes(n, v, "~")
                t.add_bar(b)
                b = Bar(key, meter)
                remain = note.h - remain                    
                if float(remain**-1).is_integer():
                    b.place_notes(n, remain**-1)
                else:
                    left = remain
                    for v in value.base_values:
                        if left >= 1.0/v:
                            left -= 1.0/v
                            if left > 0:
                                b.place_notes(n, v, "~")
                            else:
                                b.place_notes(n, v)

        t.add_bar(b)
        c.add_track(t)
        
        to_pdf(from_Composition(c), "out.pdf")