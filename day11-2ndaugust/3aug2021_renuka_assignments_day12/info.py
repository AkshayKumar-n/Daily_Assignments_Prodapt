import logging
x=10
y=12
z=x+y
logging.basicConfig(filename='demo.log',level=logging.DEBUG)
# logging.critical("critical error happened")
# logging.error("unknown error happened")

# logging.warning("expected value is an integer")

logging.info(z)
# logging.debug("for developers")
#create a menu driven program 1.add books ,book title,author,descr,price,distributor,publisher
                            # 2.view all books
                            # 3.view all books title in alphabetical order
                            # 4.search a book by using title
#for product sum 1.add products product name,des,price,manufacturer,manfa date,exp date,
                #  2.view all products
                #  3.search a product
                #  4.list all the products that expire today
#find out the execution time of sorting a list by using a sorted function add any other sorting funtion
