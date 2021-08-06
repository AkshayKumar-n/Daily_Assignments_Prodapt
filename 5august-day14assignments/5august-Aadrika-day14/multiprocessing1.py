import multiprocessing , logging
start=10
stop=500
logging.basicConfig(filename='error1.log',level=logging.INFO)
###############  FINDING PRIME NUMBER BETWEEN 2 TO 500 ######################

def findPrime():
    logging.info("User had run findPrime function using multiprocessing")
    for i in range(start,stop+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i," ")

 ############### FINDING PALINDROME BETWEEN 2 TO 500 ###############          

def findPalindrome():
    logging.info("User had run FIND PALINDROME function using multiprocessing")
    for k in range(start,stop+1):
        
        temp=k
        rev=0
        try:
            while(temp > 0):
                remainder = temp % 10
                rev = (rev * 10) + remainder
                temp = temp //10

            if(k == rev):
                print("%d" %k,' ')

        except:
            print("something went wrong ")

            
if(__name__=='__main__'):
    p1=multiprocessing.Process(target=findPrime)
    p2=multiprocessing.Process(target=findPalindrome)
    p1.start()
    # p1.join()
    # print("******")
    p2.start()
    # p2.join()
    print("******")
