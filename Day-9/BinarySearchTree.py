class BST():
    def __init__(self,data):
        self.value = data
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.value is None:
            self.value=data
            return
        if self.value==data:
            return
        if self.value>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)


root = BST(50)
lst = [10,82,33,2,19,5,62,17]
for i in lst:
    root.insert(i)