from balanced_binaryTree import *

class Rope:
    def __init__(self, string=""):
        self.tree = BalBTree()
        self.SIZE_FRAG = 5
        #for i in len(string):
        #    self.concat(, s2)
    
    def weight(self, root):
        if root == None:
            return 0
        else:
            return self.weight(root.left) + len(root.data) +self.weight(root.right)
        
    def index(self, root, i):
        if self.weight(root) < i:
            return self.index(root.right, i - self.weight(root))
        else:
            if root.left != None:
                return self.index(root.left, i)
            else:
                return root.data[i]
    
    def concat(self, s1, s2):
        rope = Rope()
        tree = rope.tree
        root = tree.root
        tree1 = s1.tree
        root1 = tree1.root
        tree2 = s2.tree
        root2 = tree2.root
        
        root.left = root1
        root.right = root2
        root1.parent = root
        root2.parent = root
        return rope


if __name__ == "__main__":
    R1 = Rope()
    tree1 = R1.tree   
    root1 = tree1.root
    tree1.insert(root1, "hello")
    tree1.insert(root1, "there")
    tree1.printTree(root1)
    print

    R2 = Rope()
    tree2 = R2.tree
    root2 = tree2.addNode()
    tree2.insert(root2, "every")
    tree2.insert(root2, "one")
    tree2.printTree(root2)
    print
    
    new = R1.concat(R1, R2)
    ntree = new.tree
    nroot = ntree.root
    
    print "Here: "
    ntree.printTree(nroot)
    print
    
    """
    print new.weight(root1)
    print
    print new.index(root1, 3)
    """