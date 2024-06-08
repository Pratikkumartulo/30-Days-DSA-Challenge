n = int(input("Enter the no. of Numbers to onput in array :"))
print("Enter the elememts to array :")
array = [int(input("Enter a number: ")) for i in range(n)]
print(f"Before sorting {array}")

def minim(curr_pos,curr_min,array):
    pos = curr_pos
    for curr_pos in range(curr_pos,len(array)):
        if(curr_min>array[curr_pos]):
            curr_min = array[curr_pos]
            pos = curr_pos
    return pos


for i in range(n):
    mini = array[i]
    pos = minim(i,mini,array)
    array[i], array[pos] = array[pos], array[i]

print("After sorting",array)


