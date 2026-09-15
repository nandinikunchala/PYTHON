#Pattern
# * * * * *
for i in range(5):
     print("*",end=" ")
# #in 5 columns
for i in range(5):
   print("* ")
#print a square 5 rows and 5 columns
for i in range(5):
    print("* "*5)
#
for i in range(1,6):
    print("* "*i)

#####25 Patterns
#1.SQUARE PATTERN
# *****
# *****
# *****
# *****
# *****
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
#2.INCREASING RIGHT TRIANGLE
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
#3.DECREASING RIGHT TRIANGLE
# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
#4.RIGHT-ALIGNED INCREASING TRIANGLE
#     *
#    **
#   ***
#  ****
# *****
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
#5.Right-Aligned Decreasing Triangle
# *****
#  ****
#   ***
#    **
#     *
for i in range(1,6):
    for j in range(i-1):
        print(" ",end="")
    for j in range(6-i):
        print("*",end="")
    print()
##6.Pyramid.
#     *
#    ***
#   *****
#  *******
# *********
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
#7.Inverted Pyramid:
# *********
#  *******
#   *****
#    ***
#     *
for i in range(1,6):
    for j in range(i-1):
        print(" ",end="")
    for j in range(11-2*i):
        print("*",end="")
    print()
#8.Hollow Square
# *****
# *   *
# *   *
# *   *
# *****
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#9.Hollow Right Triangle.
# *
# **
# * *
# *  *
# *****
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#10.Hollow Pyramid
#     *
#    * *
#   *   *
#  *     *
# *********
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()
#11.Number Square
# 12345
# 12345
# 12345
# 12345
# 12345
for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()
#12.Repeated Number Triangle
# 1
# 22
# 333
# 4444
# 55555
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()
#13.Continuous Number Triangle:
# 1
# 23
# 456
# 78910
n=1
for i in range(1,5):
    for j in range(i):
        print(n,end="")
        n+=1
    print()
#14.Inverted Number Triangle
# 12345
# 1234
# 123
# 12
# 1
for i in range(5, 0, -1):
    for j in range(1,i+1):
        print(j, end="")
    print()
#15.Number Pyramid
#     1
#    123
#   12345
#  1234567
# 123456789
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
