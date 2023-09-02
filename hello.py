<<<<<<< HEAD
print("Hello World!!!")
=======
print("Hello world!,connection")
>>>>>>> bd72189bee10dcac3065f1d97b003a583dfa56a4
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
