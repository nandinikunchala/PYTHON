#*args
def student(*args):
    print(args)
student(90,80,86,85)


def marks(name,*marks):
    print(name)
    print(marks)
marks("shivani",65,85,93)

#**kwargs
def laptop(**arg):
    print(arg)
laptop(name="nandu",brand="dell",year=2025)