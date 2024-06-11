a = [8, 2, 4, 6, 5, 1, 3, 9, 7, 1, 2, 6]
rnge = 10  #Define the range of the elements in array
dic = {}
print("Before sorting",a);
# Initialize the counting array with zeros
for i in range(rnge + 1):
    dic[i] = 0

# Count occurrences of each element in the array
for j in a:
    dic[j] += 1

# Generate the sorted array
sortd = []
for keys in dic:
    for i in range(dic[keys]):
        sortd.append(keys)

# Print the sorted array
print("After sorting",sortd)
