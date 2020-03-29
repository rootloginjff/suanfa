class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self,li,method='head'):
        self.head = None
        self.tail = None
        if method == 'head':
            self.create_LinkList_head(li)
        elif method == 'tail':
            self.create_linkList_tail(li)

    def create_linkList_head(self,li):
        self.head = Node(0)
        for i in li:
            n = Node(i)
            n.next = self.head.next
            self.head.next = n
            self.head.data += 1

    def create_linkList_tail(self,li):
        self.head = Node(0)
        self.tail = self.head
        print(id(self.tail))
        print(id(self.tail))
        for i in li:
            p = Node(i)
            self.tail.next =  p
            self.tail = p
            self.head.data += 1

    def traverse(self):
        p = self.head.next
        while p:
            print(p.data)
            p = p.next


a = LinkList([1,2,3,4,5],method='tail')
a.traverse()