import multiprocessing
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
if(__name__=="__main__"):

    p1=multiprocessing.Process(target=FindPrimeBetweenNumbers)
    p2=multiprocessing.Process(target=FindPlaindrome)
    p1.start()
    p2.start()
    print("******************")


