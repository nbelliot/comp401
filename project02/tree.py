class Node:    
    def __init__(self, data=None, heuristic=0):
        self.children = []
        self.parent = None
        self.data = data
        self.heuristic = heuristic


class Tree:
    def __init__(self, data=None, heuristic=0):
        self.root = self.addNode(data, heuristic)
    
    
    def addNode(self, data=None, heuristic=0):
        return Node(data, heuristic)


    def insert(self, root, nodes):
        if len(root.children) == 0:
            root.children = nodes
            self.set_parents(root, root.children)
        else:
            inserted = False
            for node in root.children:
                if len(node.children) == 0:
                    self.insert(node, nodes)
                    inserted = True
                    break
            if inserted == False:
                self.insert(root.children[0], nodes)

    
    def set_parents(self, root, nodes):
        for node in nodes:
            node.parent = root        
    
        
    def printTree(self, root):
        thislevel = [root]
        while thislevel:
            nextlevel = list()
            #rint "|",
            for node in thislevel:
                print "(" + str(node.data) + ", " + str(node.heuristic) + ")",
                
                for child in node.children:
                    if child: nextlevel.append(child)
                #print "|",
            print
            thislevel = nextlevel


if __name__ == "__main__":
    T = Tree("S", 11)
    T.insert(T.root, [T.addNode("A", 10), T.addNode("B", 9), T.addNode("C", 8)])
    T.insert(T.root, [T.addNode("D", 7), T.addNode("E", 6), T.addNode("F", 5)])
    T.insert(T.root, [T.addNode("G", 4), T.addNode("H", 3), T.addNode("I", 2)])
    T.insert(T.root, [T.addNode("J", 1), T.addNode("K", 0), T.addNode("L", 1)])
    T.insert(T.root, [T.addNode("M", 2), T.addNode("N", 3), T.addNode("0", 4)])
    T.insert(T.root, [T.addNode("P", 10), T.addNode("Q", 9), T.addNode("R", 8)])
    T.insert(T.root, [T.addNode("S", 7), T.addNode("T", 6), T.addNode("U", 5)])
    T.insert(T.root, [T.addNode("V", 4), T.addNode("W", 3), T.addNode("X", 2)])
    T.insert(T.root, [T.addNode("Y", 1), T.addNode("Z", 0)]) 
    T.printTree(T.root)
    