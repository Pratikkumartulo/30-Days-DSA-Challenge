class Node:
    def __init__(self,data):
        self.val = data
        self.next= None
        self.prev = None
head = None

def insertBeg():
    global head
    data = int(input("Enter a value :"))
    ptr = Node(data)
    if head is None:
        head = ptr
    else:
        head.prev=ptr
        ptr.next=head
        head = ptr
def delBeg():
    global head
    if head is None:
        print("The List is empty !!")
        return
    data = head.val
    if head.next is None:
        head = None
    else:
        head = head.next
        head.prev = None
    print(f"{data} is deleted")
def insertEnd():
    global head
    data = int(input("Enter a value :"))
    ptr = Node(data)
    if head is None:
        head = ptr
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = ptr
        ptr.prev=temp
def delEnd():
    global head
    if head is None:
        print("The list is empty !")
        return
    if head.next is None:
        data = head.val
        head=None
    else:
        ptr = head
        prev = ptr
        while ptr.next is not None:
            prev = ptr
            ptr=ptr.next
        data = ptr.val
        ptr.prev= None
        prev.next=None
        print(f"{data} is deleted !")
def Traverse():
    global head
    if head is None:
        print("the Linked list is empty")
    else:
        ptr = head
        while ptr is not None:
            print(ptr.val,end=" ")
            ptr=ptr.next

while True:
    print()
    print("Press 1 for Insert at Beggning")
    print("Press 2 for Insert at the end")
    print("Press 3 for Delete the first element")
    print("Press 4 for Delete the last element")
    print("Press 5 for Traverse")
    print("Press 6 for Exit")
    ch = int(input("Enter a choice :"))
    if ch==1:
        insertBeg()
    elif ch == 2:
        insertEnd()
    elif ch==3:
        delBeg()
    elif ch==4:
        delEnd()
    elif ch==5:
        Traverse()
    elif ch==6:
        break
    else:
        print("Invalid Choice !!")
    