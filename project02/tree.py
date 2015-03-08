class Node:    
    def __init__(self, data=None, heuristic=0):
        self.children = None
        self.parent = None
        self.data = data
        self.heuristic = heuristic


class Tree:
    def __init__(self, node):
        self.root = node
    
    
    def addNode(self, data=None, heuristic=0):
        return Node(data, heuristic)


    def insert(self, root, nodes):
        if root.children == None:
            root.children = nodes
            self.set_parents(root, root.children)
        else:
            node = root.children[0]
            pre_height = self.height(node)
            for child in root.children:
                cur_height = self.height(child)
                if cur_height < pre_height:
                    node = child
                    pre_height = cur_height
            self.insert(node, nodes)

    
    def set_parents(self, root, nodes):
        for node in nodes:
            node.parent = root        
    
    
    def height(self, root):
        if root == None:
            return 0
        elif root.children == None:
            return 1
        else:
            deep = 0
            for child in root.children:
                cur = self.height(child)
                deep = max(deep, cur)
            return deep + 1
        
    
    def printTree(self, root):
        thislevel = ["|", root, "|"]
        while thislevel:
            nextlevel = list()
            for node in thislevel:
                if isinstance(node, Node):
                    print "(" + str(node.data) + ", " + str(node.heuristic) + ")",
                    nextlevel.append("|")
                    if node.children != None:
                        #nextlevel.append("|")
                        for child in node.children:
                            nextlevel.append(child)
                        #nextlevel.append("|")
                    nextlevel.append("|")
                else:
                    print node,                
            print
            thislevel = nextlevel


if __name__ == "__main__":
    T = Tree(Node("S", 11))
    
    T.insert(T.root, [T.addNode("A", 10), T.addNode("B", 9), T.addNode("C", 8)])    
    T.insert(T.root, [T.addNode("D", 7), T.addNode("E", 6), T.addNode("F", 5)])
    T.insert(T.root, [T.addNode("G", 4), T.addNode("H", 3), T.addNode("I", 2)])
    T.insert(T.root, [T.addNode("J", 1), T.addNode("K", 0), T.addNode("L", 1)])
    T.insert(T.root, [T.addNode("M", 2), T.addNode("N", 3), T.addNode("0", 4)])
    T.insert(T.root, [T.addNode("P", 10), T.addNode("Q", 9), T.addNode("R", 8)])
    #T.insert(T.root, [T.addNode("S", 7), T.addNode("T", 6), T.addNode("U", 5)])
    #T.insert(T.root, [T.addNode("V", 4), T.addNode("W", 3), T.addNode("X", 2)])
    #T.insert(T.root, [T.addNode("Y", 1), T.addNode("Z", 0)]) 
    T.printTree(T.root)
    
    print T.height(T.root)
    