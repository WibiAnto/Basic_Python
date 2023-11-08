"""
Linear data structure with element called nodes
Head=not pointed, tail=not pointing
Singly linked list: refer to next nodes
Doubly linked list: refer to before and after nodes
"""


class node:
    """
    Object for storing single node of linked list
    Attribute: data and link to de next nodes
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """return the number of the nodes"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """Add data at the head of the list"""
        new_node = node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert(self, data, index):
        """Add data with specific place"""
        if index == 0:
            self.add(data)
        if index > 0:
            new = node(data)
            position = index
            current = self.head
            while position > 1:
                current = node.next_node
                position -= 1
            prev = current
            next = current.next_node
            new.next_node = next

    def remove(self, key):
        """Delete element on list"""
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def search(self, key):
        """linear search for the first node that match with the key"""
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    def node_at_index(self,index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current
    def __repr__(self):
        """Print the list"""
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)


