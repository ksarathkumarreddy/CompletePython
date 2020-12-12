'''
1.Class variables can access Class methods.
2.Class variables can access Instance methods.
3.Instance variables can't access Class methods.

CV CM   YES
IV IM   YES
CV IM   YES
IV CM   NO


'''
# Class variables and methods
class Emp:
    office = 'CGI'
    @classmethod
    def get_info(cls):
       print("Class Emp data:",cls.office)
Emp.get_info()


class Stu:
    clg_address = 'mpl'
    clg_name = 'Ganambica'
    @classmethod
    def get_add(cls):
        print("Student college address:",cls.clg_address,cls.clg_name)
Stu.get_add()

