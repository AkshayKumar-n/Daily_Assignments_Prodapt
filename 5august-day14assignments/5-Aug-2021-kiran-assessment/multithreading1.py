import threading,time
def Primenumbers():
    for num in range(2,500):
        time.sleep(2)
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num,end=' ')

def Palindromenumbers():
    for num in range(10,500):
        time.sleep(2)
        temp=num
        reverse=0
        while(temp>0):
            rem=temp%10
            reverse=(reverse*10)+rem
            temp=temp//10
        if(num==reverse):
            print(num,end=' ')

t1=threading.Thread(target=Primenumbers)
t2=threading.Thread(target=Palindromenumbers)
t1.start()
t1.join()
print("......")
t2.start()
t2.join()
print(".........")