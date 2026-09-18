# Output-Based Python Questions
# Q1
x = [1, 2, 3]
y = x
y.append(4)
print(x)
###output:x=[1,2,3,4]
# Explain why the output occurs.
# Q2
a = 10
b = 20
a, b = b, a
print(a, b)
####output:20,10
# Q3
x = "Python"
print(x[::-1])
####output:nohtyP
# Q4
numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers if x % 2 == 0]
print(result)
####output:result=[4,8]
# Q5
data = {"a": 1, "b": 2}
for key, value in data.items():
    print(key, value)
####output:a 1 
#          b 2
# Q6
def test(x=[]):
    x.append(1)
    return x
print(test())
print(test())
####output:[1] [1,1]
# Explain the mutable-default-argument behavior.
# Q7
def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()
####output:10
# Explain the scope.
# Q8
nums = [1, 2, 3]
result = map(lambda x: x * 2, nums)
print(list(result))
####output:[2,4,6]
# Q9
def numbers():
    for i in range(3):
        yield i
x = numbers()
print(next(x))
print(next(x))
####output:0 1
# Explain generator state.
# Q10
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error")
finally:
    print("Done")
###output:Error Done
