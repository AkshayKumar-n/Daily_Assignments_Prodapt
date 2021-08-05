import re,datetime,time,csv
from datetime import date
productdetails=[]
header=['pname','pdes','price','manufacturer','mfg_date','exp_date']
class product:

    def addproduct(self,pname,pdes,price,manufacturer,mfg_date,exp_date):
        pdict={"pname":pname,"pdes":pdes,"price":price,"manufacturer":manufacturer,"mfg_date":mfg_date,"exp_date":exp_date}
        productdetails.append(pdict)  
obj=product()
while(True):
    print("1.Add product")
    print("2.view all products")
    print("3.search a product")
    print("4.list all products that expire today")
    print("5.save to file")
    choice=int(input("enter your choice"))
    if choice==1:
        pname=input("enter product name:")
        pdes=input("enter product description:")
        price=int(input("enter price of product:"))
        manufacturer=input("enter manufacturer:")
        mfg_date=input("enter manufacturing date:")
        exp_date=input("enter expiry date:")
        obj.addproduct(pname,pdes,price,manufacturer,mfg_date,exp_date) 
    if choice==2:
        print(productdetails)   
    if choice==3:
        prname=input("please enter required product:")
        print(list(filter(lambda i:i["pname"]==prname,productdetails)))  
    if choice==4:
        current_time=time.localtime()
        today=time.strftime("%Y-%m-%d",current_time)
        print(list(filter(lambda i:i["exp_date"]==today,productdetails)))
    if choice==5:
        with open('productdetails.csv','w+',encoding='UTF8',newline='') as s:
            writer = csv.DictWriter(s,fieldnames=header)
            writer.writeheader()
            writer.writerows(productdetails)
