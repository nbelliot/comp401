import random

class Node:    
    def __init__(self, data=None, heuristic=0):
        self.children = None
        self.parent = None
        self.data = data
        self.heuristic = heuristic


class Tree:
    def __init__(self):
        self.root = None
    
    
    def addNode(self, data=None, heuristic=0):
        return Node(data, heuristic)

    
    def generate (self, total, branches):
        count = 0
        self.root = self.addNode("S", random.randint(0,9))
        thislevel = [self.root]
        count += 1
        while count < total:
            nextlevel = list()
            for node in thislevel:
                nodes = list()
                for i in range(0, branches):
                    temp = self.addNode(chr(ord("A") + (count -1)) + ver, random.randint(0,9))
                    nextlevel.append(temp)
                    nodes.append(temp)
                    count += 1
                self.set_relatives(node, nodes)
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
                    string += "(" + str(node.data) + ", " + str(node.heuristic) + ")"
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


if __name__ == "__main__":
    T = Tree()
    T.generate(26,3)
    T.printTree()
    