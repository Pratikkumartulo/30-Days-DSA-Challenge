class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

head = None

def insertEnd():
    global head
    data = int(input("Enter a value to insert :"))
    ptr = Node(data)
    if head is None:
        head = ptr
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = ptr
def delEnd():
    global head
    if head is None:
        print("The list is empty")
        return
    if head.next is None:
        data = head.val
        head = None
        print(f"{data} is deleted")
        return
    temp = head
    prev = temp
    while temp.next is not None:
        prev = temp
        temp = temp.next
    data = temp.val
    prev.next = None
    print(f"{data} is deleted")

def Traverse():
    global head
    if head is None:
        print("The list is empty !")
        return
    ptr = head
    while ptr is not None:
        print(ptr.val,end=" ")
        ptr = ptr.next

while True:
    print()
    print("Press 1 for Insert at the end")
    print("Press 2 for delete the last element")
    print("Press 3 for traverse the list")
    print("Press 4 for exit")
    ch = int(input("Enter your choice :"))
    if ch==1:
        insertEnd()
    elif ch==2:
        delEnd()
    elif ch ==3:
        Traverse()
    elif ch==4:
        break
    else:
        print("Invalid choice")


