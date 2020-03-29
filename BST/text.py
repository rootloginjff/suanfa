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

tree = BST([5,4,6,8,7])

