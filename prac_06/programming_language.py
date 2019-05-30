class ProgrammingLanguage:

    def __int__(self, typing, reflection, year, name):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing,
                                                                           self.reflection, self.year)


