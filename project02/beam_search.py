from tree import *
from node_sort import *

class BeamSearch:
    def __init__(self, problemSet, memorySize):
        self.tree = problemSet
        self.root = problemSet.root
        self.k = memorySize
        self.openlist = []
        self.path = []
        
        node = self.root
        self.openlist.append(node)
        
        while node.heuristic != 0 or self.openlist == []:
            self.openlist.remove(node)
            if node.children != None:
                if (len(self.openlist) + len(node.children)) > self.k:
                    for child in node.children:
                        if child.heuristic < self.openlist[-1].heuristic:
                            for item in self.openlist:
                                if child.heuristic < item.heuristic:
                                    self.openlist.pop()
                                    if item in self.openlist:
                                        self.openlist.insert(self.openlist.index(item), child)
                                    else:
                                        self.openlist.append(child)
                                    break
                else:
                    for child in node.children:
                        self.openlist.append(child)
            if self.openlist != []:
                nodeSort(self.openlist)
                node = self.openlist[0]
        
        if node.heuristic == 0:
            return self.optPath(node)
        else:
            return self.path
    
        
        
    def optPath(self, node):
        while node != None:
            self.path.insert(0, node)
            node = node.parent
            
    
    def printPath(self):
        if self.path == []:
            print "Path not found."
        else:
            for i in self.path:
                print "(" + str(i.data) + ", " + str(i.heuristic) + ")",
        