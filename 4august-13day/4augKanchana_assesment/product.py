import datetime,time,logging
from datetime import date
import csv
import json
product_list=[]
headerContent=["pname","description","price","manufacturer","mfd","efd"]
class ProductDetails:
    def init(self,pname,des,price,manufacturer,mfd,efd):
        self.pname=pname
        self.des=des
        self.price=price
        self.manufacturer=manufacturer
        self.mfd=mfd
        self.efd=efd
        def validate(dict1):
            vpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["pname"])
            valdes=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dict1["desc"])
            vprice=re.search("[1-9]{1}[1-9]{2,7}$",dict1["price"])
            
        if valname and valdes and valprice:
            return True
        else:
            return False       

    def AddProductDetails(self,pname,desc,price,manufacturer,mfd,efd):

        dict1={"pname":pname,"description":desc,"price":price,"manufacturer":manufacturer,"mfd":mfd,"efd":efd} 
        product_list.append(dict1)

   
obj1=ProductDetails()    
today=datetime.date.today()
while True:

    print("1.Add Product")
    print("2.View products")
    print("3.Search a product")
    print("4.List products that expire today")
    print("5.move data to csv file")
    print("6.exit") 
    choice=int(input("Enter your choice : "))
    
        
    if choice==1:
        pname=input("Enter the  name of the product : ")
        desc=input("Enter the Description of a product:")
        price=int(input("Enter the Price of product in rupees : "))
        manufacturer=input("Enter the manufacturer name : ")
        mfd=input("Enter the manufacturing date : ")
        efd=input("Enter the expiry date   YYYY-MM-DD : ")
                # a=validate(pname,desc,price)
                # if a:
        obj1.AddProductDetails(pname,desc,price,manufacturer,mfd,efd)
                # else:
                    # logging.error("Invalid data Enter it again")


              
    if choice==2:
        print(json.dumps(product_list))

    if choice==3:
        sname=input("Enter the product name to search : ")
        print(list(filter(lambda i:i["pname"]==sname,product_list)))
                
    if choice==4:
        current_time=time.localtime()
        tday=time.strftime("%Y-%m-%d",current_time)
        expirylist=(list(filter(lambda i:i["efd"]==str(tday),product_list)))    
        if len(expirylist)>0:
            print(expirylist)
                
        else:
            print("No records found") 
                
    if choice==5:
        with open("product.csv","w+",encoding="UTF8",newline='')as p:
            writer=csv.DictWriter(p,fieldnames=headerContent) 
            writer.writeheader()
            writer.writerows(product_list)
                
    if choice==6:
            break
        
        
    
# except:
#     logging.error("unable to connect")
# finally:
#     logging.info("successfully added student details")

                
     