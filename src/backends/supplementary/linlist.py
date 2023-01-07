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