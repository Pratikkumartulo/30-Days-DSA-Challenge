n = int(input("Enter the no. of Numbers to onput in array :"))
array = []
print("Enter the numbers in ascending order :")
for i in range(n):
    num = int(input(f"Enter the {i+1} number :"))
    array.append(num)
item = int(input("Enter the item to search :"))
start = 0
end = len(array)-1
pos = -1
while(start<=end):
    mid = int((start+end)/2)
    if array[mid]==item:
        pos = mid
        print(f"Item found on index {pos}")
        break
    elif array[mid]>item:
        end = mid - 1
    else:
        start = mid + 1
if(pos==-1):
    print("Item not found !!")