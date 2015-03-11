from tree import *

class BeamSearch:
    def __init__(self, problemSet, memorySize):
        self.tree = problemSet
        self.root = problemSet.root
        self.k = memorySize
        self.openlist = []
        self.path = []
        
        node = self.root
        self.openlist.append(node)
        
        while node.heuristic != 0:
            self.openlist.remove(node)
            if len(node.children) > 0:
                if (len(self.openlist) + len(node.children)) > memorySize:
                    for i in node.children:
                        if i.heuristic < self.openlist[len(self.openlist)]:
                            for j in self.openlist:
                                if i.heuristic < j.heuristic:
                                    self.openlist.pop()
                                    self.openlist.append(i)
                                    break
                else:
                    for i in node.children:
                        self.openlist.append(i)
            node = self.openlist[0]
            
        self.optPath(node)
        
        
    def optPath(self, node):
        while node != None:
            self.path.insert(0, node)
            node = node.parent    
        