#Scope
#scope has 4 sub topics
#L-local scope
#E-enclosing scope
#G-global scope
#B-built in scope

#local problems
def num():
    x=10
    x=20
    print(x)
num()

#global
x=10
def num():
   global x
   x+=3
num()
print(x)

#enclosing problem
x=10
def outer():     #enclosing variable
    x=20
    def inner():
        print(x) #finds x in enclosing scope
    inner()
outer()

#built-in scope
x="nandu"
print(len(x))

