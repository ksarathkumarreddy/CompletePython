# conditional expression
# syntax
# [on_true] if [expression] else [on_false]
a, b = 10, 20
min = a if a < b else b
print(min)





# nested if else
print("Both a and b are equal" if a == b else "a is greater than b" if a>b else "b is greater than a")

if a!=b:
    if a == b:
        print("both are equal")
    elif a > b:
        print("A is greater than B")
    else:
        print("B is greater than A")