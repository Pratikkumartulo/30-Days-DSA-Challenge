n = int(input("Enter the no. of Numbers to onput in array :"))
print("Enter the elememts to array :")
array = [int(input("Enter a number: ")) for i in range(n)]
print(f"Before sorting {array}")

for i in range(n):
    changed = False
    print(array)
    for j in range(n-1-i):
        if(array[j]>array[j+1]):
            array[j], array[j + 1] = array[j + 1], array[j]
            changed = True
    if(not(changed)):
       break
        
print("After sorting",array)