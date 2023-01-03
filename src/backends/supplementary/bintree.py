class Treenode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
    
    def insert(self, value):
        if self.value == value:
            return 
        
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Treenode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Treenode(value)
    
    def search(self, value):
        if self.value == value:
            return True
        
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def print_nodes(self):
        

        if self.left:
            self.left.print_nodes()

        print(self.node)

        if self.right:
            self.right.print_nodes()

        return False
    

def buildbintree(values):
    root = Treenode(values[0])
    for i in range(1, len(values)):
        root.insert(values[i])
    return root



    
    
