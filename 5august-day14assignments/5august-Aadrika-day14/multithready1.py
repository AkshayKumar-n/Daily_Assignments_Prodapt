import threading,time
import logging
start=2
stop=500

logging.basicConfig(filename='error2.log',level=logging.INFO)
###############  FINDING PRIME NUMBER BETWEEN 2 TO 500 ######################
def findPrime():
    logging.info("User had run findPrime function")
    for i in range(start,stop+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
        
                #time.sleep(2)
                print(i+" ")
############### FINDING PALINDROME BETWEEN 2 TO 500 ###############
print("palindromes")
def findPalindrome():
    logging.info("User had run FIND PALINDROME function")
    for k in range(start,stop+1):
        temp=k
        rev=0
        try:
            while(temp > 0):
                Reminder = temp % 10
                rev = (rev * 10) + Reminder
                temp = temp //10
            if(k == rev):
                #time.sleep(2)
                print("%d" %k+ " ")
        except:
            print("something went wrong")

t1=threading.Thread(target=findPrime)
t2=threading.Thread(target=findPalindrome)
t1.start()
t1.join()
print("******")
t2.start()
t2.join()
print("******")