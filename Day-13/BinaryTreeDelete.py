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

    def delete(self,node):
        if self.value is None:
            print("Tree is empty !")
            return
        if node > self.value:
            if self.rchild:
                self.rchild = self.rchild.delete(node)
            else:
                print("Node is not available")
        elif node < self.value:
            if self.lchild:
                self.lchild = self.lchild.delete(node)
            else:
                print("Node is not available")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            elif self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            temp_node = self.lchild
            while temp_node.rchild:
                temp_node = temp_node.rchild
            self.value = temp_node.value
            self.lchild = self.lchild.delete(temp_node.value)
        return self

root = BST(50)
lst = [10,82,33,2,19,5,62,17]
for i in lst:
    root.insert(i)

root.inorder()
print()
root.preorder()
root.delete(50)
print()
root.inorder()
print()
root.preorder()
