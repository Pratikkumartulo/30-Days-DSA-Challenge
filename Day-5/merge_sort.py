n = int(input("Enter the no. of Numbers to onput in array :"))
print("Enter the elememts to array :")
array = [int(input("Enter a number: ")) for i in range(n)]
print(f"Before sorting {array}")


def merge_sort(array):
    if(len(array)<=1):
        return array
    else:
        mid = len(array)//2
        left = array[:mid]
        right =array[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merger(left,right)
def merger(left,right):
    new = []
    i,j = 0,0
    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

sortedarr = merge_sort(array)
print("After sorted ",sortedarr)