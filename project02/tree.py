K = 3

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
            pre_child = root.children[0]
            pre_size = self.size(pre_child)
            for child in root.children:
                cur_size = self.size(child)
                max_size = self.maxSize(child)
                if cur_size != max_size:
                    return self.insert(child, nodes)
            return self.insert(root.children[0], nodes)

    
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
    
    
    def size(self, root):
        if root == None:
            return 0
        elif root.children == None:
            return self.size(root.children) + 1
        else:
            total = 0
            for child in root.children:
                total += self.size(child) + 1
            return total - 2
            
        
    def maxSize(self,root):
        height = self.height(root)
        total = 1
        if root == None:
            return total
        elif root.children == None:
            return self.maxSize(root.children)
        else:
            for i in range(0, height):
                total += K**i
                i += 1
        return total - 1
        
    
    def printTree(self, root):
        thislevel = ["|", root, "|"]
        while thislevel:
            string = ""
            nextlevel = list()
            for node in thislevel:
                if isinstance(node, Node):
                    string += "(" + str(node.data) + ", " + str(node.heuristic) + ")"
                    nextlevel.append("|")
                    if node.children != None:
                        #nextlevel.append("|")
                        for child in node.children:
                            nextlevel.append(child)
                        #nextlevel.append("| ")
                    nextlevel.append("| ")
                else:
                    string += node
            print string
            thislevel = nextlevel


if __name__ == "__main__":
    T = Tree(Node("S", 11))
    
    print T.height(T.root)
    print T.size(T.root)
    print T.maxSize(T.root)
    print
    
    T.insert(T.root, [T.addNode("A", 10), T.addNode("B", 9), T.addNode("C", 8)])
    
    print T.height(T.root)
    print T.size(T.root)
    print T.maxSize(T.root)        
    
    
    T.insert(T.root, [T.addNode("D", 7), T.addNode("E", 6), T.addNode("F", 5)])
    T.printTree(T.root)
    T.insert(T.root, [T.addNode("G", 4), T.addNode("H", 3), T.addNode("I", 2)])
    #T.insert(T.root, [T.addNode("J", 1), T.addNode("K", 0), T.addNode("L", 1)])
    #T.insert(T.root, [T.addNode("M", 2), T.addNode("N", 3), T.addNode("0", 4)])
    #T. printTree(T.root)
    
    
    #T.insert(T.root, [T.addNode("P", 10), T.addNode("Q", 9), T.addNode("R", 8)])
    #T.insert(T.root, [T.addNode("S", 7), T.addNode("T", 6), T.addNode("U", 5)])
    #T.insert(T.root, [T.addNode("V", 4), T.addNode("W", 3), T.addNode("X", 2)])
    #T.insert(T.root, [T.addNode("Y", 1), T.addNode("Z", 0)]) 
    T.printTree(T.root)
    
    print T.height(T.root)
    print T.size(T.root)
    print T.maxSize(T.root)
    