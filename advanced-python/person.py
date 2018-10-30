class Person:
    """base class"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        print ('First name:', self.first_name)
        print ('Last name:', self.last_name)


if __name__ == '__main__':
    p = Person('MahendraSingh', 'Dhoni')
    p.get_info()