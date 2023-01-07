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