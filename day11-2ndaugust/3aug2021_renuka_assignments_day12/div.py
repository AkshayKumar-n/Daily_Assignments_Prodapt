import logging

try:
    x=int(input("enter a number"))
    y=int(input("enter a number"))
    z=x/y
    #logging.basicConfig(filename='demo.log',level=logging.DEBUG)
    #logging.info(z)
except Exception as e:
    #print("ArithmeticException")
    logging.basicConfig(filename='demo.log',level=logging.DEBUG)
    logging.exception("exception occured")
    
