from balanced_binaryTree import *

class Rope:
    def __init__(self, string=""):
        self.tree = BalBTree()
        self.SIZE_FRAG = 5
        if string != "": self.feed(string)
            
        
    def feed(self, string):
        if len(string) < self.SIZE_FRAG:
            if self.tree.root.left == None or self.tree.root.right == None:
                self.tree.insert(self.tree.root, string[0:(len(string))])
            else:
                self.concat(Rope(string))
        else:
            if self.tree.root.left == None or self.tree.root.right == None:
                self.tree.insert(self.tree.root, string[0:self.SIZE_FRAG])
                self.feed(string[self.SIZE_FRAG:len(string)])
            else:
                self.concat(Rope(string))

            
    def weight(self, root):
        if root == None:
            return 0
        else:
            return self.weight(root.left) + len(root.data) +self.weight(root.right)
        
        
    def index(self, root, i):
        if self.weight(root) <= i:
            return self.index(root.right, i - self.weight(root))
        else:
            if root.left != None:
                return self.index(root.left, i)
            else:
                return root.data[i]
            
            
    def find(self, root, i):
        if self.weight(root) <= i:
            return self.find(root.right, i - self.weight(root))
        else:
            if root.left != None:
                return self.find(root.left, i)
            else:
                return root, i
    
    
    def cut(self, root, i, R):
        if self.weight(root) <= i:
            if 
            return self.cut(root.right, i - self.weight(root), R)
        else:
            if root.left != None:
                if (R.tree.root.left or R.tree.root.right) == None:
                    R.tree.root = root.right
                    #R.tree.root.left.parent = None
                    root.right = None
                    return self.cut(root.left, i, R)
                else:
                    S = Rope()
                    S.tree.root = root.right
                    #S.tree.root.parent = None
                    root.right = None
                    S.concat(R)
                    return self.cut(root.left, i, S)
            else:
                return R
    
    def concat(self, S):
        root = self.tree.addNode()
        tree1 = self.tree
        root1 = tree1.root
        tree2 = S.tree
        root2 = tree2.root
        
        root.left = root1
        root.right = root2
        root1.parent = root
        root2.parent = root
        self.tree.root = root
        
        self.tree.determine_height(root)
        self.tree.balance()

    def split(self, i):
        tree = self.tree
        node, index = self.find(tree.root, i)
        if index != 0:
            root = tree.addNode()
            root.left = tree.addNode(node.data[0:index])
            root.right = tree.addNode(node.data[index:len(node.data)+1])
            parent = node.parent
            if parent.left == node:
                parent.left = root
            else:
                parent.right = root
            self.tree.balance()
        return self.cut(tree.root, i, Rope())
    
    def insert(self, i, S):
        node, index = self.find(self.tree.root, i)
        root = tree.addNode()
        root.left = node
        node.parent = root
        root.right = S.root
        S.root.parent = root


if __name__ == "__main__":
    R1 = Rope("He12o there")
    R1.tree.printTree(R1.tree.root)
    print

    R2 = Rope("every one that is here.")
    R2.tree.printTree(R2.tree.root)
    print
    
    R1.concat(R2)
    
    print "Here: "
    R1.tree.printTree(R1.tree.root)
    print
    
    
    R3 = Rope("Hello there my friends I love you so much.")
    R3.tree.printTree(R3.tree.root)
    print
    R3.tree.printTree(R3.tree.root)
    print
    
    print R1.weight(R1.tree.root)
    print
    print R1.index(R1.tree.root, 3)
    print
    
    R4 = R1.split(3)
    
    R1.tree.printTree(R1.tree.root)
    print
    #R4.tree.printTree(R4.tree.root)