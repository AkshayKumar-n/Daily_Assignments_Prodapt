myfile=open('demo.txt',"a")
myfile.write(" renuka hello dharani")
myfile=open('demo.txt','r')
x=myfile.read()
print(str(x))
myfile.close()

