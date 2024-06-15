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
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.value,end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def preorder(self):
        print(self.value,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.value,end=" ")

    def search(self,data):
        if self.value==data:
            print(f"{data} is present")
        elif data>self.value:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(f"{data} is not present")
        else:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(f"{data} is not present")

root = BST(50)
lst = [10,82,33,2,19,5,62,17]
for i in lst:
    root.insert(i)

root.inorder()
print()
root.preorder()
print()
root.postorder()
print()
root.search(30)