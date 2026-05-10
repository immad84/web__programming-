class Person:
    def __init__(self, name):
        self.name = name
 
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.__name = name
