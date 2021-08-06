import time,multiprocessing,sys
prime = []
def findPrime(a,b):
    for num in range(a,b):
        time.sleep(0.1)  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                print("%d"%num, end ='  ')
    print("\n")
                

def findPalindrome(c,d):
    for num in range(c,d):
        time.sleep(0.1)
        temp = num
        reverse = 0

        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10

        if(num == reverse):
            print("%d " %num, end = '  ')
    sys.exit(0)        
        
a=2
b=500
c=10
d=500
findPrime(a,b)
findPalindrome(c,d)       




if (__name__ =="__main__"):
    

    p1 = multiprocessing.Process(target=findPrime,args=(a,b,))  #Creating a thread
    p2 = multiprocessing.Process(target=findPalindrome,args=(c,d,))
    p1.start()
    p2.start()


    p1.join()
    p2.join() 
    print("******")
    

    
