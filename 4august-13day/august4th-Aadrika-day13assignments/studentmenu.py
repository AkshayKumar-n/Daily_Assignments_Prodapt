import time
import re ,csv
studentlist=[]
studentheadercontent=["name","rollnum","adminnum","eng","hindi","maths","science","cs","total","added"]


class Student:
    def studentdetails():
         name=" "
         rollnum=0
         adminnum=0
         eng=0
         hindi=0
         maths=0
         science=0
         cs=0
    
   
class studentdetails(Student):
    def addstudentdetails(self,name,rollnum,adminnum,eng,hindi,maths,science,cs):
        total=eng+hindi+maths+science+cs
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"name":name,"rollnum":rollnum,"adminnum":adminnum,"eng":eng,"hindi":hindi,"maths":maths,"science":science,"cs":cs,"total":total,"added":current_local_time}
        studentlist.append(dict1)
s1=studentdetails()


def validation_student_details(name,roll):
    val=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",name)
    val2=re.match("[0-9]{0,7}$",roll)
    if val and val2:
        return True
    else:
        return False


while(True):
    print("1. Add Students:")
    print("2. Display student details: ")
    print("3. Search student using roll number")
    print("4. Ranking")
    print("5. Generate csv file")
    print("6. Exit")
    choice=int(input("enter your choice: "))
    
    if choice==1:
        while(True):
            name=input("Enter your name: ")
            rollnum=(input("enter your roll number: "))
            if validation_student_details(name,rollnum):
                admisnum=int(input("enter your admin num: "))
                englis=int(input("enter english marks: "))
                hindi=int(input("enter hindi marks: "))
                maths=int(input("enter maths marks: "))
                science=int(input("enter science marks: "))
                cs=int(input("enter cs marks: "))
                s1.addstudentdetails(name,rollnum,admisnum,englis,hindi,maths,science,cs)
            else:
                print("PLease Try again by entering valid name and roll number")
                continue
            break
        
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=input("Enter roll number to search: ")
        print(list(filter(lambda i:i["rollnum"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
    if choice==5:
        with open("student.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=studentheadercontent)
            writer.writeheader()
            writer.writerows(studentlist)
    if choice==6:
        break