class LinkedList:
    def __init__(self):
        self.node = None

    def listPrint(self):
        l = []
        node = self.node
        while node is not None:
            l.append(node.data)
            node = node.next
        return l

    def insertAtBeginning(self, data):
        # create a newnode with data
        newnode = Node(data)
        # insert the first node of current Linkedlist in the node.next
        newnode.next = self.node
        # make the new node as the first node
        self.node = newnode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.node is None:
            self.node = newNode
