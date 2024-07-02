arr =  [1,3,5,7,23,10,15,45]

def arrSum(arr,start,end):
    sums = 0
    for i in range(start,end+1):
        sums+=arr[i]
    print(sums)

def buildPrefix(arr):
    prefix = []
    sums=0
    for i in arr:
        sums+=i
        prefix.append(sums)
    return prefix

def prefixSum(prefix,start,end):
    if start==0:
        print(prefix[end])
    else:
        print(prefix[end]-prefix[start-1])

prefix = buildPrefix(arr)
arrSum(arr,0,5)
prefixSum(prefix,0,5)

