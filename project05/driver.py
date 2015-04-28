from tree import *
from a_star import *
from music_generator import *
from music_notator import *

C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B = 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71
majScale = [0, 2, 4, 5, 7, 9, 11]
minScale = [0, 2, 3, 5, 7, 8, 10]
hminScale = [0, 2, 3, 5, 7, 8, 11]
beats = [16, 8, 4, 2]
octave = [0]

tonic = Bb - 12
key = 'G'
mode = hminScale
meter = (4, 4)
tempo = 150
nNotes = 6

if __name__ == "__main__":
    melody = []
    for i in range(20):
        T = Tree(tonic, beats, mode, octave)
        T.generate(nNotes, 3)
        ASearch = AStar(T)
        for j in ASearch.path:
            melody.append(j)
    print
    music_generator(melody, tempo)
    print
    music_notator(melody, key, meter)