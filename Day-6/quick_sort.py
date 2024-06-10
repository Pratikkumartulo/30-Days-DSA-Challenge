n = int(input("Enter the no. of Numbers to onput in array :"))
print("Enter the elememts to array :")
array = [int(input("Enter a number: ")) for i in range(n)]
print(f"Before sorting {array}")

def pivot(array,low,high):
    pivot = array[low]
    i = low+1
    j = high
    while True:
        while(i<=j and array[i]<=pivot):
            i+=1
        while(i<=j and array[j]>=pivot):
            j-=1
        if(i<=j):
            array[i],array[j] = array[j],array[i]
        else:
            break
    array[low],array[j] = array[j],array[low]
    return j

def quick_sort(array,low,high):
    if(low<high):
        piv = pivot(array,low,high)
        quick_sort(array,low,piv-1)
        quick_sort(array,piv+1,high)
    return array

sorted_Arr = quick_sort(array,0,len(array)-1)
print("After sorting",sorted_Arr)

