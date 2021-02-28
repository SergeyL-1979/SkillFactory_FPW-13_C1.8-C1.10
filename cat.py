class Cat():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_say(self):
        return "{0}: mau!".format(self.name)


cats = Cat('Mate', 'boy', 3)
print(cats.gender)
print(cats.name)
print(cats.get_say())