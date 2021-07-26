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
            return
        node = self.node
        while node.next:
            node = node.next
        node.next = newNode

    def insertInBeetween(self, nextval, data):
        start = self.node
        while start.next:
            if start.data == nextval:
                print("Match Found")
                newNode = Node(data)
                newNode.next = start.next
                start.next = newNode
                return
            else:
                start = start.next

    def removeNode(self, Removekey):
        start = self.node

        if (start is not None):
            if (start.data == Removekey):
                self.node = start.next
                start = None
                return

        while (start is not None):
            if start.data == Removekey:
                break
            prev = start
            start = start.next

        prev.next = start.next
        start = None


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next


llist = LinkedList()
