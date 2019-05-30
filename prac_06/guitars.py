class Guitar:

    def __int__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        current_year = 2018
        origin =int(input("When was the guitar made?: "))
        age = current_year - origin
        return age

    def is_vintage(self):
        age = 0
        age.get_age()
        if age >= 50:
            return True


    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)
