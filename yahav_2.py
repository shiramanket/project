from yahav import employe

class dev(employe):
    def __init__(self, name, year_born ,salary, programming_language):
        super().__init__(name, year_born ,salary)
        self.programming_language = programming_language

    def say_hi(self):
        print(f'Hello, my name is {self.name}. I am a developer and I know {self.programming_language}.')

dev1 = dev('John Doe', 1990, 5000, 'Python')
dev1.say_hi()

    