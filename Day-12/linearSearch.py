def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage:
arr = [3, 5, 2, 4, 9, 1]
target = 4
index = linear_search(arr, target)
print(f"Element {target} found at index {index}")
