from tree import *
from node_sort import *

class AStar:
    def __init__(self, problemSet, goal=None):
        self.tree = problemSet
        self.root = self.tree.root
        self.goal = goal
        self.openlist = []
        self.closedlist = []
        self.path = []
        
        current = self.root
        self.openlist.append(current)
        
        while self.openlist != [] :
            self.openlist.remove(current)
            self.closedlist.append(current)
            if current.children == self.goal:
                return self.optPath(current)
            for child in current.children:
                self.fN(child, current)
                if child in self.closedlist and child.g_accum < self.closedlist[self.closedlist.index(child)].g_accum:
                    self.closedlist.remove(self.closedlist[self.closedlist.index(child)])
                    self.closedlist.append(child)
                elif child in self.openlist and child.g_accum < self.openlist[self.openlist.index(child)].g_accum:
                    self.openlist.remove(self.openlist[self.openlist.index(child)])
                    self.openlist.append(child)
                else:
                    self.openlist.append(child)
            if self.openlist != []:
                nodeSort(self.openlist)
                current = self.openlist[0]
        return False
    
    
    def gN(self, new, old):
        new.g_accum = new.g + old.g_accum
        return new.g_accum
    
    
    def fN(self, new, old):
        g = abs(new.g - old.g)
        h = abs(new.h - old.h)
        new.f = g + h
        return new.f
    
    
    def optPath(self, current):
        while current != None:
            self.path.insert(0, current)
            current = current.parent
    
    
    def printPath(self):
            if self.path == []:
                print "Path not found."
            else:
                for i in self.path:
                    print "(" + str(i.g) + ", " + str(i.h) + ")",    