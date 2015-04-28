import random

class Node:    
    def __init__(self, g=0, h=0):
        self.children = None
        self.parent = None
        self.g = g
        self.h = h
        self.g_accum = 0
        self.f = 0


class Tree:
    def __init__(self, tonic, beats, scale, octave):
        self.root = None
        self.tonic = tonic
        self.beats = beats
        self.scale = scale
        self.octave = octave
    
    def addNode(self, g=0, h=0):
        return Node(g, h)

    
    def generate (self, depth, bredth):
        self.root = self.addNode(self.tonic + random.choice(self.scale) + random.choice(self.octave), random.choice(self.beats))
        thislevel = [self.root]
        level = 1
        while level <= depth:
            nextlevel = list()
            num = 0
            for node in thislevel:
                nodes = list()
                for i in range(0, bredth):
                    temp = self.addNode(self.tonic + random.choice(self.scale) + random.choice(self.octave), random.choice(self.beats))
                    nextlevel.append(temp)
                    nodes.append(temp)
                    num += 1
                self.set_relatives(node, nodes)
            level += 1
            thislevel = nextlevel     
    
    
    def set_relatives(self, parent, children):
        self.set_children(parent, children)
        self.set_parents(parent, children)        
    
    
    def set_children(self, parent, children):
        parent.children = children
    
    
    def set_parents(self, parent, children):
        for node in children:
            node.parent = parent        
            
    
    def printTree(self):
        thislevel = ["|", self.root, "|"]
        while thislevel:
            string = ""
            nextlevel = list()
            for node in thislevel:
                if isinstance(node, Node):
                    string += "(" + str(node.g) + ", " + str(node.h) + ")"
                    #nextlevel.append("|")
                    if node.children != None:
                        nextlevel.append("|")
                        for child in node.children:
                            nextlevel.append(child)
                        nextlevel.append("| ")
                    #nextlevel.append("| ")
                else:
                    string += node
            print string
            thislevel = nextlevel    