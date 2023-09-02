print("Hello World!")
def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
print(mydoubler(11))

#localscope
def scope():
    x=300
    print(x)
scope()

#globalscope
x=300
def func():
    print(x)
func()
print(x)
