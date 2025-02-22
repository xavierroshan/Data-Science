import threading

# def add():
#     a,b=4,5
#     sum = a+b
#     print(sum)

# t=threading.Thread(target = add)
# t.start()
# t.join()

# import threading
# import time

# #task1
# def add(a,b):
#     sum =a+b
#     time.sleep(4)
#     print(sum)

# #task1
# def product(a,b):
#     prod=a*b
#     time.sleep(2)
#     print(prod)

# #code to show threading
# #add(100,200)
# #product(100,200)

# t1 = threading.Thread(target = add, args=(100,200))
# t2 = threading.Thread(target = product, args=(100,200))
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# import threading

# lock = threading.Lock()

# def add(a,b):
#     with lock:
#         print (f"the numbers are {a} and {b}")
#         sum = a+b
#         print (f"the sum is {sum}")


# t1 = threading.Thread(target = add, args = (100,200))
# t2 = threading.Thread(target = add, args =(1000,2000))

# t1.start()
# t2.start()

# t1.join()

# t2.join()












