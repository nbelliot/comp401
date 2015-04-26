import pygame
import time
import pygame.midi

class MidiEmulator:
    def __init__(self, midiInput, midiOutput, midiInstrument):
        pygame.midi.init()
        self.inp = pygame.midi.Input(midiInput)
        self.player = pygame.midi.Output(midiOutput)
        self.player.set_instrument(midiInstrument,midiOutput)
        self.keys = {}

        self.duration = 0.5
        self.major=[0,4,7,12]

    def get(self, data):
        return data[0][0]
    
    def check(self, note):
        if note in self.keys:
            return self.keys[note]
        else:
            return False
    
    def play(self, data):
        note = data[1]
        velocity = data[2]
        channel = data[3]
        if self.check(note):
            self.player.note_off(note,velocity,channel)
            self.keys[note] = False
        else:
            self.player.note_on(note,velocity,channel)
            self.keys[note] = True
    
    def harm(self, data, interval):
        note = data[1]
        velocity = data[2]
        channel = data[3]
        if self.check(note):
            self.player.note_off(note,velocity,channel)
            self.player.note_off(note+interval,velocity,channel)
            self.keys[note] = False
        else:
            self.player.note_on(note,velocity,channel)
            self.player.note_on(note+interval,velocity,channel)
            self.keys[note] = True        

    def arp(self,data,mode,duration):
        note = data[1]
        velocity = data[2]
        channel = data[3]
        if self.check(note):
            self.keys[note] = False
        else:
            for n in mode:
                self.player.note_on(note+n,velocity,channel)
                time.sleep(duration)
                self.player.note_off(note+n,velocity,channel)
            self.keys[note] = True
    
    def chord(self, data, mode):
        note = data[1]
        velocity = data[2]
        channel = data[3]
        if self.check(note):
            for n in mode:
                self.player.note_off(note+n,velocity,channel)
            self.keys[note] = False
        else:
            for n in mode:
                self.player.note_on(note+n,velocity,channel)
            self.keys[note] = True
        
    def end(self):
        pygame.quit()

if __name__ == "__main__":
    VI = MidiEmulator(1,0,1)
    while True:
        if VI.inp.poll():
            data = VI.get(VI.inp.read(50))
            print data
            VI.play(data)
            #VI.harm(data,7)
            #VI.arp(data,VI.major,VI.duration)
            #VI.chord(data,VI.major)
            
