'''
There may be a lot of data, a class contain and the user does not need the entire data.
The user needs only some part of the available data.
In thi case, we can hide the unnecessary data from the user and expose only that data that is of interest to the user.
Best example for abstraction is a car..

'''
class Bank:
    def __init__(self):
        self.accno = 12
        self.name = 'vis'
        self.__loan= 132445555
    def dis(self):
        print(self.accno)
        print(self.name)
sarath = Bank()
sarath.dis()
