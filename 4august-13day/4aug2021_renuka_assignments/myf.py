headercontent=["name","rollno"]



with open('file1.txt','w+') as f:
    f.write("hii")
    f.seek(0)
    print(f.read())