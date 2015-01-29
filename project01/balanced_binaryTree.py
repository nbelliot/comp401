"""
"Binary Tree" - balanced_binaryTree.py (5/14/14)
Nicholas Elliot

Associated Files:
balanced_binaryTree.py
a_star.py
DFS.py
music_generator.py
"""


class Node:    
    def __init__(self, data=""):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data


class BalBTree:
    def __init__(self):
        self.root = None
    
    
    def addNode(self, data=""):
        return Node(data)


    def insert(self, root, data=""):    
        if root.left == None:
            root.left = self.addNode(data)
            root.left.parent = root
        elif root.right == None:
            root.right = self.addNode(data)
            root.right.parent = root
        elif self.size(root.left) > self.size(root.right):
            size = self.size(root.left)
            maxsize = self.maxSize(root.left)
            if (size == maxsize):
                self.insert(root.right, data)
                root.right.parent = root
            else:
                self.insert(root.left, data)
                root.left.parent = root
        else:
            self.insert(root.left, data)
            root.left.parent = root


    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1
            
            
    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)
        
        
    def maxSize(self,root):
        height = self.maxDepth(root)
        total = 0
        if root == None:
            return 0
        else:
            for i in range(0,height):
                total += 2**i
                i += 1
        return total


    def printTree(self, root):
        if root == None:
            pass   
        else:
            self.printTree(root.left)
            if root.data != "":
                print root.data,
            self.printTree(root.right)


    def printRevTree(self, root):
        if root == None:
            pass
        else:
            self.printRevTree(root.right)
            if root.data != "":
                print root.data,
            self.printRevTree(root.left)

"""            
if __name__ == "__main__":
    # create the binary tree
    BTree = BalBTree()
    # add the root node
    root = BTree.addNode(10)
    # ask the user to insert values
    for i in range(0, 5):
        data = int(raw_input("insert the node value nr %d: " % i))
        # insert values
        BTree.insert(root, data)
    print
    
    BTree.printTree(root)
    print
    BTree.printRevTree(root)
    print
        
    print BTree.maxDepth(root)
    print BTree.mazSize(root)
"""