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
    
    def __getitem__(self, index):
        return self.head[index]
    
    def show(self):
        node = self.head
        while(node.next != None):
            print(node.data, end=" -> ")
            node = node.next
        print(node.data)

    def pushFront(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            prevHead = self.head
            self.head = newNode
            newNode.next = prevHead

    def pushBack(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    
    def remove(self, index):
        if(self.head == None):
            return None
        else:
            i, size = 1, len(self)
            if(index > size):
                index = index % size
            if(index == 1):
                self.head = self.head.next
                return 
            while(i < index-1):
                node = node.next
                i += 1
            if(node.next and node.next.next):
                temp = node.next 
                node.next = node.next.next
                del temp            
            else:
                node.next = None
    
    def pop(self):
        if(self.head == None):
            return
        else:
            node = self.head
            prevNode = None
            while(node.next != None):
                prevNode = node
                node = node.next
            prevNode.next = None
            del node
    
    def reverse(self):
        if(self.head == None):
            return 
        else:
            node = self.head
            prevNode = None
            while(node != None):
                temp = node.next 
                node.next = prevNode
                prevNode = node
                node = temp
                if(temp == None):
                    self.head = prevNode
            return self.head
    
    def create(self):
        pass