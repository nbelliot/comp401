from a_star import *
from midiutil.MidiGenerator import MidiGenerator
from midiutil.TrackGen import LoopingArray
import itertools

class music_generator:
    def __init__(self, melody, tempo):
        self.melody = melody
        midiGenerator = MidiGenerator(tempo=tempo)
        length = 0
        n = []
        b = []
        
        for note in self.melody:
            n.append([note.g])
            b.append(((4.0/note.h), 2))
            length += 4.0/note.h
    
        notes = LoopingArray(n)
        beats = LoopingArray(b)
        velocities = LoopingArray([100])
    
        midiGenerator.add_track(0, 0, beat=beats, notes=notes, velocities=velocities, length=length)
        midiGenerator.write()