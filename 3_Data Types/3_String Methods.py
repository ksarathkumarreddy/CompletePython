''''
string is used to store text data.
'''



# 1 Capitalize          first letter must be capital and remaining must be small
str = 'python is Awesome'
capitalzed_str = str.capitalize()
print(capitalzed_str)

# 2 Center              it gives space
name = 'sarath'
print(name.center(22))

# 3 Count               how many times sub str will present in str
str = 'python is awesome and python high level programming language'
substr = 'p'
print(str.count(substr))

# 4 Casefold            All the letters must be small
str = "Sarath Kumar Reddy"
print(str.casefold())

# 5 Encode              returns utf-8 encoded version
string = 'python'
print(string.encode())

# 6 Endswith            return true if endswith specified index and otherwise return false
txt = 'easy to learn.'
print(txt.endswith(txt))

# 7 Expandtabs          default size is 8
str = 'sarath\t9505\tkumar'
print(str.expandtabs())

# 8 Find                substring exists in string it returns the specified path nd it doesnt exist it returns -1
text = 'sarath is a good boy'
print(text.find('a'))

#9 Format
print("hello %s you have %d RS left"%('sarath',25))
print("Hi {},this is {}".format('sarath','bharath'))
print("many more happy returns of the day{name} and this is your {age} birthday".format(name='sarath',age=23))

# 10 isalnum            here albhabets and number both can contain
name = 'sarath11'
print(name.isalnum())

# 11 isalpha            here alphabets contain only
name = 'bharath'
print(name.isalpha())

# 12 isdecimal          here decimal only
num = '950586'
print(num.isdecimal())

# 13 isidentifier
str = 'python'
print(str.isidentifier())

# 14 isprintable          starting letter should be capital and remaining must be small
sha = 'This is sarath'
print(sha.isprintable())

# 15 istitle            is starting letter for every letter must be capital
letter= 'Python Is Good'
print(letter.istitle())

# 16 join
list = ['1','2','3']
sep = ','
print(sep.join(list))

s1 = 'abc'
s2 = '123'
print(s1.join(s2))

# 17 split              we can separated by comma
txt = "hello everyone this is sarath"
print(txt.split())
print(txt.split(','))

# 18 strip              we can remove space from both sides
name = '    sarath   '
print(name.strip())

str = 'android is awesome'
print(str.strip('an'))

# 19 swapcase           we can convert upper case to lower case
name = 'SARATH KUMAR REDDY'
print(name.swapcase())

