class Treenode:
    def __init__(self, right, left, value):
        self.right = right
        self.left = left
        self.value = value
    
    def insert(self, value):
        if self.value == value:
            return 
        
        if value < self.value:
            if self.left:
                self.left.insert(value)
            self.left = Treenode(value)

    
    
