class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f





#前序遍历
def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.lchild)
        pre_order(root.rchild)

#中序遍历
def mid_order(root):
    if root:
        mid_order(root.lchild)
        print(root.data)
        mid_order(root.rchild)

#后序遍历
def last_order(root):
    if root:
        last_order(root.lchild)
        last_order(root.rchild)
        print(root.data)
root = e
pre_order(root)
print('-------')
mid_order(root)
print('-------')
last_order(root)