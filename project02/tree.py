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

    
    def generate (self, depth, bredth):
        self.root = self.addNode("S", random.randint(depth-1,depth+1))
        thislevel = [self.root]
        level = 1
        while level <= depth:
            nextlevel = list()
            num = 0
            for node in thislevel:
                nodes = list()
                char = chr(ord("A") + (level -1))
                for i in range(0, bredth):
                    temp = self.addNode(char + str(num), abs(random.randint(depth-level-1,depth-level+1)))
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
    T.generate(5,3)
    T.printTree()
    