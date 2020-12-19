'''
Exception is an event, that distrupts the normal flow of the program..

'''

try:
    fh = open('testfile','w')
    fh.write("This is a file for handling exception")
except IOError:
    print("cannot find file or read data")
else:
    print("written content in the file successfully")
    fh.close()