arr = [ 170, 45, 75, 90, 802, 24, 2, 66]

def countSort(arr,n):
    ln = len(arr)
    outpt = [0]*ln
    cnt = [0]*10
    for i in arr:
        index = (i//n)%10
        cnt[index]+=1
    for j in range(1,10):
        cnt[j]+=cnt[j-1]
    i = ln-1
    while(i>=0):
        index = (arr[i]//n)%10
        outpt[cnt[index]-1]=arr[i]
        cnt[index]-=1
        i-=1
    for i in range(ln):
        arr[i] = outpt[i]

def radixSort(arr):
    maximum = max(arr)
    n = 1
    while maximum//n> 0:
        countSort(arr,n)
        n*=10
radixSort(arr)
print("Sorted array is:", arr)