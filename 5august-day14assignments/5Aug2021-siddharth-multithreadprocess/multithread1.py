import threading,logging
logging.basicConfig(filename="multip.log",level=logging.DEBUG)
start=10
end=500
def FindPrimeBetweenNumbers():

    
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                
                print(i,end=" ")

def FindPlaindrome():
    
    for num in range(start,end+1):
        temp=num
        reverse=0
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10

        if(num == reverse):
            print("%d" %num, end =' ')

t1=threading.Thread(target=FindPrimeBetweenNumbers)
t2=threading.Thread(target=FindPlaindrome)
t1.start()
t2.start()
print("******************")
try:
        logging.info("Threading worked succesfully")

except:
        logging.error("Something went wrong")

finally:
        print("Everything executed properly")







