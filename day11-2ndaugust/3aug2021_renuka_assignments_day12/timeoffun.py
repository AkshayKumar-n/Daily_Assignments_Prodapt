import timeit
mylist=[12,12,3,4,1,5,7,9,6,4,5]
#def printnumbers():
#    for i in range(100000):
#        pass
def f1():
    filter(6,mylist)
def f2():
    for i in mylist:
        if(i==6):
            pass
#def printwhile():
#    n=0
#    while(n<=100000):
#        n=n+1
#       pass
#print(timeit.timeit(printnumbers,number=100000))
#print(timeit.timeit(printwhile,number=100000))
print(timeit.timeit(f1,number=100))
print(timeit.timeit(f2,number=100))