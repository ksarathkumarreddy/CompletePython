# Membership Operator
# in
# not in
list1 = [1,2,3,4]
list2 = [4,5,6,7]
for item in list1:
    if item in list2:
        print("over lapping")
else:
    print("not overlapping")


x = 24
y = 330
list = [10,20,30,33]
if(x not in list):
    print("x not in given list")
else:
    print("x is present in given list")
if(y in list):
    print("y is given list")
else:
    print("y is not given list")

print("----------------")

p =99
tup = (19,99,9)
if(p in tup):
    print("true")
else:
    print("false")

str = "sarath"
print('s' in str)

dict = {3:"k",4:"s"}
print(3 in dict)    # here true means 3 is a key for any time in dict type only comparing the key only
print('k' in dict)  # here false means k is a value

list = ["sarath",2,3,4]
print(list[0])
if(2 in list):
    print("true")
else:
    print("false")

print("-------------------------------")
if('sarath' in list):
    print("true")
else:
    print("false")

