class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next

    def add_first(self,node):
        node.next = self.head
        self.head = node

    def add_last(self,node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Debugging repr implementation
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)



if __name__ == '__main__':

    ll = LinkedList(['a','b'])
    ll.add_first(Node("A"))
    print(ll)
    ll1 = LinkedList()
    print(ll1)
    ll1.add_last(Node("c"))
    print(ll1)