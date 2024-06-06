n = int(input("Enter the no. of Numbers to onput in array :"))
print("Enter the elememts to array :")
array = [int(input("Enter a number: ")) for i in range(n)]
print(f"Before sorting {array}")
for i in range(1,n):
    j = i-1
    temp = array[i]
    while(temp<array[j] and j>=0):
        array[j+1] = array[j]
        j -= 1
    array[j+1] = temp
print(f"After sorting, {array}")