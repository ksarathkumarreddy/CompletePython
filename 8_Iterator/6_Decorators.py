'''
1.First class function
2.Nested function
3.Returning function

'''
print("----------1. FIRST CLASS FUNCTIONS------------")
def foo2(bar):
    return bar + 1
foo2(2)
print(foo2(3))
print(type(foo2))
print(foo2)



# 2. Nested Function
print("---------------2. NESTED FUNCTIONS------------------")

# main()
def parent1():
    print("Printing from the parent() function.")
    # inner function
    def first_child():
        return "Printing from the first_child() function."

    print(first_child())
    print("---------=======")
    print(first_child)
    print("returning first_child function")
    return first_child

# print(parent1.first_child())
ch_addr = parent1()
print("Calling second child nested func ==> " ,ch_addr)
# parent1.first_child() #We can't call nested function directly
print(ch_addr())
print("---Exception Handling-----")
try:
    parent1.first_child() # AtrributeError('fdsfadsf')
except AttributeError as err:
    print(err)
    print("--You cannot call nested function directly------")



# Returning Functions

print("---------------3. RETURNING NESTED FUNCTION NAME------------------")

def parent(num):

    def first_child():
        return "Printing from the first_child() function."
    def second_child():
        return "Printing from the second_child() function."

    if num == 10:
        return first_child
    else:
        return second_child
sara = parent(10)
print("Returning funct",sara)
print("Executing func",sara())

