from balanced_binaryTree import *

class Rope:
    def __init__(self):
        self.tree = BalBTree()
    
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
    
    def


if __name__ == "__main__":
    Lasso = Rope()
    tree = Lasso.tree   
    root = tree.addNode()
    tree.insert(root) #1
    tree.insert(root) #2
    tree.insert(root) #3
    tree.insert(root) #4
    tree.insert(root, "hello")
    tree.insert(root, "there")
    tree.insert(root, "friend")
    tree.printTree(root)
    print
    print Lasso.weight(root)
    print
    print Lasso.index(root, 3)