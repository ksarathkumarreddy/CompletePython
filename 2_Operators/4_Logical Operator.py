# AND OPERATOR
''''
T T T
T F F
F T F
F F F

'''
a = 22
b = 33
c = -44
if a > 0 and b > 0:
    print("numbers are greater than zero")
if a > 0 and b > 0 and c >0:
    print("greater than zero")
else:
    print("atleast one number is not greater than zero")

# OR OPERATOR
''''
T T T
T F T
F T T
F F F
'''

x = 22
y = -10
z = 0
if x > 0 or y > 0:
    print("either of the number is greater than zero")
else:
    print("no number is greater than zero")
if y > 0 or z > 0:
    print("either of the number is greater than zero")
else:
    print("no number is greater than zero")


# NOT OPERATOR
''''
T F 
F T

'''

p = 10
if not p:
    print("boolea value of a is ture")
if not(p%3 == 0 or a%5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")




a = True
b = False
print(a and b)
print(a or b)
print(not a)


