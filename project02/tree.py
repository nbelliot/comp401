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
    

    def printTree(self, nodes):
        if nodes == self.root:
            print "|(" + str(nodes.data) + ", " + str(nodes.heuristic) + ")|"
            self.printTree(nodes.children)
            
        else:
            if len(nodes) == 0:
                pass   
            else:
                print "|",
                for node in nodes:
                    print "(" + str(node.data) + ", " + str(node.heuristic) + ")",
                print "|",
                print
                for node in nodes:
                    self.printChildren(node.children)
                for node in nodes:
                    self.printTree(node.children)
                    
    
    def printChildren(self, nodes):
        print "|",
        for node in nodes:
            print "(" + str(node.data) + ", " + str(node.heuristic) + ")",
        print "|",        



if __name__ == "__main__":
    T = Tree("S", 11)
    T.insert(T.root, [T.addNode("A", 8), T.addNode("B", 9), T.addNode("C", 10)])
    T.insert(T.root, [T.addNode("D", 7), T.addNode("E", 6), T.addNode("F", 5)])
    T.insert(T.root, [T.addNode("G", 4), T.addNode("H", 3), T.addNode("I", 2)])
    T.insert(T.root, [T.addNode("J", 4), T.addNode("K", 3), T.addNode("L", 2)])
    T.insert(T.root, [T.addNode("M", 4), T.addNode("N", 3), T.addNode("0", 2)])
    T.printTree(T.root)