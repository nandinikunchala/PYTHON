#Find the Second Largest Element (without using sort())
numbers = [10, 45, 32, 67, 89, 54]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest:", second)
#Remove Duplicate Elements Without Using set()
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
result = []
for num in numbers:
    if num not in result:
        result.append(num)
print(result)
#Find the Missing Number from 1 to n
numbers = [1, 2, 4, 5]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
print("Missing number:", expected_sum - actual_sum)