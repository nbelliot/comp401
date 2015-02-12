from balanced_binaryTree import *

class Rope:
    """A rope data structure.
    
    Creates a rope object and stores a string (if given) within.
    
    Args:
      string: A string.
    """
    def __init__(self, string=""):
        self.tree = BalBTree()  #tree
        self.SIZE_FRAG = 10  #max number of characters per string fragments
        if string != "": self.feed(string)  #stores string (arg) in rope
            
        
    def feed(self, string):
        """'Feeds' and stores a string (arg) into rope.
        
        Args:
          self: A rope.
          string: A string.
        """
        if len(string) < self.SIZE_FRAG:  #if string fits in fragment...
            if self.tree.root.left == None or self.tree.root.right == None:
                #if it is the 1st or 2nd element in rope, insert
                self.tree.insert(self.tree.root, string[0:(len(string))])
            else:
                self.concat(Rope(string))  #otherwise, concatenate
        else:  #string does not fit in fragment
            if self.tree.root.left == None or self.tree.root.right == None:
                #if it is the 1st or 2nd element in rope...
                self.tree.insert(self.tree.root, string[0:self.SIZE_FRAG])
                #insert what does fit
                self.feed(string[self.SIZE_FRAG:len(string)])
                #feed what is left
            else:
                self.concat(Rope(string))  #concatenate


    def weight(self, node):
        """Determines the left weight of node.
        
        Args:
          node: A node.
          
        Returns:
          Weight of node.
          """
        if node == None:
            return 0
        else:
            return self.way(node.left) + len(node.data)
    
    
    def way(self, node):
        """Determines the total weight of node. - "weight" helper func
        
        Args:
          node: A node.
          
        Returns weight of node.
        """
        if node == None:
            return 0
        else:
            return self.way(node.left) + len(node.data) + self.way(node.right)
        
        
    def index(self, root, i):
        """Retrieves character at index i.
                
        Args:
          roor: A root node.
          i: An index.
          
        Returns:
          Character at index i.
        """        
        if self.weight(root) <= i:  #if weight is < index, go right
            return self.index(root.right, i - self.weight(root))
        else:  #otherwise, go left
            if root.left != None:
                return self.index(root.left, i)
            else:
                return root.data[i]
            
            
    def find(self, root, i):
        """Retrieves node at index i and index of character in fragment.
                        
        Args:
          root: A root node.
          i: An index.
          
        Returns:
          Node at index i, index of character in fragment.
        """                
        if self.weight(root) <= i:  #if weight is < index, go right
            return self.find(root.right, i - self.weight(root))
        else:  #otherwise, go left
            if root.left != None:
                return self.find(root.left, i)
            else:
                return root, i

    
    def concat(self, S):
        """Concatenates two Ropes into a single Rope.
                                
        Args:
          self: A rope.
          S: A rope.
        """             
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
        
        self.tree.balance()

    def split(self, i):
        """Splits a Rope at index i, removing all elements from i and the right.
                        
        Args:
          self: A rope.
          i: An index.
          
        Returns:
          Leftover Rope of removed right elements.
        """             
        tree = self.tree
        node, index = self.find(tree.root, i)  #node at index i
        if index != 0:  #if character at i is not at begining of fragment...
            root = tree.addNode()  #split the point to create two new leaf nodes
            root.left = tree.addNode(node.data[0:index])
            root.left.parent = root
            root.right = tree.addNode(node.data[index:len(node.data)])
            root.right.parent = root
            parent = node.parent
            if parent.left == node:
                parent.left = root
            else:
                parent.right = root
            root.parent = parent
            self.tree.balance()
        R = Rope()
        R.tree.root = None
        S = self.cut(tree.root, i, R)
        self.tree.balance()
        return S


    def cut(self, root, i, R):
        """Trims all elements off of Rope from i and the right. - 'split' helper
        func.
                        
        Args:
          self: A rope.
          root: A root node.
          i: An index.
          R: Rope composed of trimmed leaves off of original Rope.
          
        Returns:
          Leftover Rope of composed trimmed elements.
        """ 
        if self.weight(root) <= i:  #if weight is < index, go right
            return self.cut(root.right, i - self.weight(root), R)
        else:  #otherwise, go left
            if root.left != None:
                if R.tree.root == None:
                    if root.right != None:
                        R.tree.root = root.right
                        R.tree.root.left.parent = None
                        root.right = None
                    return self.cut(root.left, i, R)
                else:
                    if root.right != None:
                        S = Rope()
                        S.tree.root = root.right
                        S.tree.root.parent = None
                        root.right = None
                        S.concat(R)
                    return self.cut(root.left, i, S)
            else:
                S = Rope()
                S.tree.root = root
                root.parent.right = None
                S.tree.root.parent = None
                S.concat(R)                
                return S
    
    
    def insert(self, i, S):
        """Inserts Rope S into the Rope at index i.
        
        Args:
          i: An integer for the index.
          S: A Rope to be inserted.
        """        
        tree = self.tree
        node, index = self.find(tree.root, i)  #node at index i
        if index != 0:  #if character at i is not at begining of fragment...
            root = tree.addNode()  #split the point to create two new leaf nodes
            root.left = tree.addNode(node.data[0:index])
            root.left.parent = root
            root.right = tree.addNode(node.data[index:len(node.data)])
            root.right.parent = root
            parent = node.parent
            if parent.left == node:
                parent.left = root
            else:
                parent.right = root
            root.parent = parent
            self.tree.balance()
            node, index = self.find(tree.root, i)
        root = self.tree.addNode()
        parent = node.parent
        root.right = node
        node.parent = root
        root.left = S.tree.root
        root.left.parent = root
        if parent.left == node:
            parent.left = root
        else:
            parent.right = root
        root.parent = parent
        self.tree.balance()
        
        
    def delete(self, i, j):
        """Deletes substring i to j from Rope.
                        
        Args:
          self: A rope.
          i: Begining of index.
          j: End of index.
        """         
        R = self.split(i)
        S = R.split(j-i)
        self.concat(S)
        
    
    def report(self):
        """Prints string fragments in order from Rope."""
        self.tree.printTree(self.tree.root)
        print


if __name__ == "__main__":
    R1 = Rope("He12o there")
    print "R1: "
    R1.report()
    print
    
    print "R2: "
    R2 = Rope("everyone that is here.")
    R2.report()
    print
    
    print "R1 = R1 + R2: "
    R1.concat(R2)
    R1.report()
    print
    
    print "R3: "
    R3 = Rope("The cow jumped over the moon.")
    R3.report()
    print
    
    print "R3.split(8): "
    R4 = R3.split(8)
    R3.report()
    print
    
    print "R4: "
    R4.report()
    print
    
    print "R5: "
    R5 = Rope("I like you.")
    R5.report()
    print
    
    print "R6: "
    R6 = Rope("really don't ")
    R6.report()
    print
    
    print "R5.insert(5, R6): "
    R5.insert(2, R6)
    R5.report()
    print   
    
    print "R7: "
    R7 = Rope("Hi there pal.")
    R7.report()
    print
    
    print "R7.delete(3,9): "
    R7.delete(3,9)
    R7.report()
    print