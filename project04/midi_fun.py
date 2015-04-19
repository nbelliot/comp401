import pygame
import time
import pygame.midi

pygame.midi.init()
player= pygame.midi.Output(0)
player.set_instrument(48,1)
inp = pygame.midi.Input(1)

duration = 0.5
major=[0,4,7,12]

def get(data):
    return data[0][0][1]

def go(note):
    player.note_on(note, 127,1)
    time.sleep(duration)
    player.note_off(note,127,1)

def arp(base,ints):
    for n in ints:
        go(base+n)

def chord(base, ints):
    player.note_on(base,127,1)
    player.note_on(base+ints[1],127,1)
    player.note_on(base+ints[2],127,1)
    player.note_on(base+ints[3],127,1)
    time.sleep(duration)
    player.note_off(base,127,1)
    player.note_off(base+ints[1],127,1)
    player.note_off(base+ints[2],127,1)
    player.note_off(base+ints[3],127,1)
    
def end():
    pygame.quit()

if __name__ == "__main__":
    x = 1
    while True:
        if inp.poll():
                 # no way to find number of messages in queue
                 # so we just specify a high max value
            note = get(inp.read(1))
            print note
            x += 1
            
        if x % 2 == 0:
            go(note)
