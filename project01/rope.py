from balanced_binaryTree import *

class Rope:
    def __init__(self, string=""):
        self.tree = BalBTree()
        self.SIZE_FRAG = 5
        i = 0
        while i < len(string):
            if len(string) - i < self.SIZE_FRAG:
                if self.tree.root.left == None or self.tree.root.right == None:
                    self.tree.insert(self.tree.root, string[i:i+(len(string))])
                else:
                    self.concat(Rope(string[i:i+(len(string))]))
            else:
                if self.tree.root.left == None or self.tree.root.right == None:
                    self.tree.insert(self.tree.root, string[i:i+self.SIZE_FRAG])
                else:
                    self.concat(Rope(string[i:i+(len(string)-1)]))
            i += self.SIZE_FRAG
        
    #def feed(self, string):

            
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
            
    def find(self, root, i):
        if self.weight(root) < i:
            return self.find(root.right, i - self.weight(root))
        else:
            if root.left != None:
                return self.find(root.left, i)
            else:
                return root, i
    
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

    #def split(self, i):
        #
        #if i < weight 
        """
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
                
                """
        def insert(self, i, S):
            node, index = self.find(self.tree.root, i)
            root = tree.addNode()
            root.left = node
            node.parent = root
            root.right = S.root
            S.root.parent = root        


if __name__ == "__main__":
    R1 = Rope("Hello there")
    R1.tree.printTree(R1.tree.root)
    print

    R2 = Rope("every one.")
    R2.tree.printTree(R2.tree.root)
    print
    
    R1.concat(R2)
    
    print "Here: "
    R1.tree.printTree(R1.tree.root)
    print
    
    #print R1.split(3)
    
    R3 = Rope("123456789098")
    R3.tree.printTree(R3.tree.root)
    
    print R1.weight(R1.tree.root)
    print
    print R1.index(R1.tree.root, 3)
    