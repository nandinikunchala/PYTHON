#1.Write a Python program to count how many even numbers are present in a list.
list=[10,11,12,13,14]
count=0
for number in list:
    if number%2==0:
        count+=1
print(count)

#2.Write a Python program to find the largest number in a list.
max=[10,5,7,20,45,4]
largest=0
for number in max:
    if number>largest:
        largest=number
print(largest)

#3.Write a Python program to find the smallest number in a list.
min=[9,6,5,12,90]
smallest=min[0]
for number in min:
    if number<smallest:
        smallest=number
print(smallest)

#4.Write a Python program to find the second largest number in a list.
numbers=[50,80,90,66,54,85]
largest_number=0
secong_largest=0
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number

    elif number > second_largest:
        second_largest = number

print(second_largest)

#5.Write a Python program to remove duplicate elements from a list while keeping the original order.
num=[1,2,2,3,3,4,3]
unique=[]
for number in num:
    if number  not in unique:
        unique.append(number)
print(unique)

#6.Write a Python program to check whether a list is in ascending order or not.


