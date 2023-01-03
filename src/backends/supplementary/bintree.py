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

        print(self.value)

        if self.right:
            self.right.print_nodes()

        return False
    
    def printLevel(self, X):
        if self is None:
            return 0
        q = []
        currLevel = 1
        q.append(self)
        
        while(len(q) > 0):
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if(node.value == X):
                    return currLevel
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            currLevel += 1
        return 0
    

def buildbintree(values):
    root = Treenode(values[0])
    for i in range(1, len(values)):
        root.insert(values[i])
    return root


if __name__ == "__main__":
    nodes = [30, 10, 40, 22, 15, 18]
    tree = buildbintree(nodes)
    tree.insert(18)
    tree.insert(20)
    print("15 found in binary tree", tree.search(15))
    print("100 found in binary tree", tree.search(100))
    print("10 is on level: ",tree.printLevel(10))
    tree.print_nodes()
    
    
