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
        
        while node.h != 0:
            self.openlist.remove(node)
            if len(node.children) > 0:
                if (len(self.openlist) + len(node.children)) > memorySize:
                    for i in node.children:
                        if i.h < openlist[len(openlist)]:
                            for j in self.openlist:
                                if i.h < j.h:
                                    self.openlist.pop()
                                    self.openlist.append(i)
                                    break
                else:
                    for i in children:
                        self.openlist.append(i)
            node = openlist[0]
            
        self.optPath(node)
        
        
    def optPath(self, node):
        while node != None:
            self.path.insert(0, node)
            node = node.parent    
        