from person import Person
class Employee(Person):
    """derived class"""
    def __init__(self, emp_id, first_name, last_name):
        self.emp_id = emp_id
        # invoking over-ridden methods
        super().__init__(first_name, last_name)

    def get_info(self):
        print ('employee_id:', self.emp_id)
        # invokde base class version of get_info
        super().get_info()

if __name__ == '__main__':
    e = Employee('123123', 'Bhagyesh', 'Dudhediya')
    e.get_info()