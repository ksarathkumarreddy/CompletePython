class Emp:
    def __init__(self,id, name,sal, office):
        self.id = id
        self.name = name
        self.sal = sal
        self.office = office
    def get_emp_details(self):
        print("Emp details are:",self.id, self.name, self.sal, self.office)
vis = Emp(101,'sarath',233333,'blr')
vis.get_emp_details()