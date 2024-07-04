def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left, right]  # Indices are 1-based
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Example usage:
numbers = [2, 7, 11, 15]
target = 9
print("Indices of two numbers that add up to target:", two_sum(numbers, target))
