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

