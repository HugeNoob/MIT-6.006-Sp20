class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    def insert_last(self, x):
        new = Doubly_Linked_List_Node(x)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def delete_first(self):
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if self.head == None:
            return None
        else:
            self.head.prev = None
        return x

    def delete_last(self):
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail == None:
            return None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        L2.head = x1
        L2.tail = x2
        if x1 == self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next
        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        x1.prev, x2.next = None, None
        return L2

    def splice(self, x, L2):
        xn = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.tail.next = xn
        xn.prev = L2.tail
        if xn == None:
            self.tail = L2.tail
        L2.head, L2.tail = None, None


