class Node:    
    def __init__(self, data=""):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        #self.height = 0


class BalBTree:
    def __init__(self):
        self.root = self.addNode()
    
    
    def addNode(self, data=""):
        return Node(data)


    def insert(self, root, data=""):
        if root.left == None:
            root.left = self.addNode(data)
            root.left.parent = root
            self.determine_height(root.left)
        elif root.right == None:
            root.right = self.addNode(data)
            root.right.parent = root
            self.determine_height(root.right)
        elif self.size(root.left) > self.size(root.right):
            size = self.size(root.left)
            maxsize = self.maxSize(root.left)
            if (size == maxsize):
                self.insert(root.right, data)
                root.right.parent = root
                self.determine_height(root.right)
            else:
                self.insert(root.left, data)
                root.left.parent = root
                self.determine_height(root.left)
        else:
            self.insert(root.left, data)
            root.left.parent = root
            self.determine_height(root.left)
        
        self.determine_height(self.root)
        self.balance()
        

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
        
        
    def maxSize(self, root):
        height = self.maxDepth(root)
        total = 0
        if root == None:
            return 0
        else:
            for i in range(0,height):
                total += 2**i
                i += 1
        return total
    
    
    def determine_height(self, node):
        count_l = (self.determine_height(node.left) + 1 if node.left != None else 0)
        count_r = (self.determine_height(node.right) + 1 if node.right != None else 0)
        
        height = (count_l if count_l > count_r else count_r)
        
        return height
    
    
    def move_left(self, node):
        _r = node.right
        _rl = _r.left
        
        node.right = _rl
        _r.left = node
        
        self.determine_height(node)
        self.determine_height(_r)
        
        return _r
  
    def move_right(self, node):
        _l = node.left
        _lr = _l.right
        
        node.left = _lr
        _l.right = node
        
        self.determine_height(node)
        self.determine_height(_l)
        
        return _l

    def rotate_left(self, node):
        _r = node.right
        
        _lH = self.determine_height(_r) if _r.left != None else 0
        _rH = self.determine_height(_r) if _r.right != None else 0
        
        if _lH > _rH: node.right = _r.move_right()
        
        return self.move_left(node)

    def rotate_right(self, node):
        _l = node.left
        
        _lH = self.determine_height(_l) if _l.left != None else 0
        _rH = self.determine_height(_l) if _l.right != None else 0
        
        if _rH > _lH: node.left = _l.move_left()
        
        return self.move_right(node)

    def balance(self):
        root = self.root
        if root.left == None and root.right == None: return root
       
        _lH = self.determine_height(root.left) if root.left != None else 0
        _rH = self.determine_height(root.right) if root.right != None else 0
       
        if _lH + 1 < _rH:
            return self.rotate_left(root)
        elif _rH + 1 < _lH:
            return self.rotate_right(root)
       
        self.determine_height(root)
        return root
          

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

            
if __name__ == "__main__":
    # create the binary tree
    BTree = BalBTree()
    # add the root node
    root = BTree.root
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
    print BTree.maxSize(root)