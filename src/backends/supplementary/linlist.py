class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

class LinkedList:
    def __init__(self, head = None):
        self.head = None
    
    def __len__(self):
        if(self.head == None):
            return 0
        else:
            count = 0
            node = self.head
            while(node != None):
                node = node.next
                count += 1
            return count