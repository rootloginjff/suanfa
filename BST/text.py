class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self,li):
        self.root = None
        self.li = li
        if self.li:
            for val in self.li:
                self.insert(val)

    def insert(self,key):
        if not self.root:
            self.root = BiTreeNode(key)
        else:
            p = self.root
            while p:
                if key < p.data:
                    if p.lchild:
                        p = p.lchild
                    else:
                        p.lchild = BiTreeNode(key)
                        break
                elif key > p.data:
                    if p.rchild:
                        p = p.rchild
                    else:
                        p.rchild = BiTreeNode(key)
                        break
                else:
                    break
    #前序遍历
    def pre_traverse(self):
        def pre_order(root):
            if root:
                print(root.data)
                pre_order(root.lchild)
                pre_order(root.rchild)
        pre_order(self.root)

    #中序遍历
    def mid_traverse(self):
        def mid_order(root):
            if root:
                mid_order(root.lchild)
                print(root.data)
                mid_order(root.rchild)
        mid_order(self.root)

    #后序遍历
    def last_traverse(self):
        def last_order(root):
            if root:
                last_order(root.lchild)
                last_order(root.rchild)
                print(root.data)
        last_order(self.root)
tree = BST([5,4,6,8,7])
tree.pre_traverse()
print('----')
tree.mid_traverse()
print('----')
tree.last_traverse()

