class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

head = None

def insertBeg():
    global head
    data = int(input("Enter a value :"))
    ptr = Node(data)
    ptr.next = head
    head = ptr
def delBeg():
    global head
    if head is None:
        print("List is empty !")
        return
    else:
        data = head.val
        head = head.next
        print(f"{data} is deleted")
def Traverse():
    global head
    if head is None:
        print("List is empty !")
        return
    ptr = head
    while ptr is not None:
        print(ptr.val,end=" ")
        ptr = ptr.next

while True:
    print("\n")
    print("Press 1 for Insert at beggining")
    print("Press 2 for Delete the First node")
    print("Press 3 for Traverse the linked List")
    print("4 for Exit")
    ch = int(input("Enter your choice :"))
    if ch==1:
        insertBeg()
    elif ch==2:
        delBeg()
    elif ch==3:
        Traverse()
    elif ch==4:
        break
    else:
        print("Invalid Choice")



