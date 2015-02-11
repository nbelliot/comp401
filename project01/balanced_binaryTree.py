class Node:    
    def __init__(self, data=""):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data


class BalBTree:
    def __init__(self):
        self.root = self.addNode()
    
    
    def addNode(self, data=""):
        return Node(data)


    def insert(self, node, data=""):
        if node.left == None:
            node.left = self.addNode(data)
            node.left.parent = node
        elif node.right == None:
            node.right = self.addNode(data)
            node.right.parent = node
        elif self.size(node.left) > self.size(node.right):
            size = self.size(node.left)
            maxsize = self.maxSize(node.left)
            if (size == maxsize):
                self.insert(node.right, data)
                node.right.parent = node
            else:
                self.insert(node.left, data)
                node.left.parent = node
        else:
            self.insert(node.left, data)
            node.left.parent = node
        
        self.balance()
        

    def maxDepth(self, node):
        if node == None:
            return 0
        else:
            ldepth = self.maxDepth(node.left)
            rdepth = self.maxDepth(node.right)
            return max(ldepth, rdepth) + 1
            
            
    def size(self, node):
        if node == None:
            return 0
        else:
            return self.size(node.left) + 1 + self.size(node.right)
        
        
    def maxSize(self, node):
        height = self.maxDepth(node)
        total = 0
        if node == None:
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
        
        _r.left = node
        node.right = _rl
        if node == self.root:
            self.root = _r        
                
        return _r
  
    def move_right(self, node):
        _l = node.left
        _lr = _l.right
        
        _l.right = node
        node.left = _lr
        if node == self.root:
            self.root = _l
                
        return _l

    def rotate_left(self, node):
        _r = node.right
        
        _lH = self.determine_height(_r) if _r.left != None else 0
        _rH = self.determine_height(_r) if _r.right != None else 0
        
        if _lH > _rH: node.right = self.move_right(_r)
        
        return self.move_left(node)

    def rotate_right(self, node):
        _l = node.left
        
        _lH = self.determine_height(_l) if _l.left != None else 0
        _rH = self.determine_height(_l) if _l.right != None else 0
        
        if _rH > _lH: node.left = self.move_left(_l)
        
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
       
        return root    
          

    def printTree(self, node):
        if node == None:
            pass   
        else:
            self.printTree(node.left)
            if node.data != "":
                print node.data,
            self.printTree(node.right)


    def printRevTree(self, node):
        if node == None:
            pass
        else:
            self.printRevTree(node.right)
            if node.data != "":
                print node.data,
            self.printRevTree(node.left)

            
if __name__ == "__main__":
    B = BalBTree()
    B.insert(B.root, 1)
    B.insert(B.root, 2)
    B.insert(B.root, 3)
    B.insert(B.root, 4)
    B.root.left.left.right = B.addNode(5)
    B.printTree(B.root)
    B.balance()
    print
    B.printTree(B.root)