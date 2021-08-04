import timeit
#x=print("hello")
#print(timeit.timeit(stmt="a=10000;b=512345678;c=a*b"))
mycode='''
a=10
if(a<15):
    pass'''
print(timeit.timeit(stmt=mycode))