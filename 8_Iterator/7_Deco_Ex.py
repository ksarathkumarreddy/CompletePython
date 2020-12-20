'''
First class func
nested function
returning function

If we can satisfy the three things then only decorator concept will be executed..

'''
import math, time
def cal_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(* args, **kwargs)
        end = time.time()

        print("Total time taken in:",end - begin)
    return inner1

# cal_time is a decorator
@cal_time
def fact(num):
    time.sleep(2)
    print(math.factorial(num))
fact(10)



@cal_time
def fact(num):
    time.sleep(5)
    print(math.factorial(num))
fact(7)









