from datetime import datetime as dm
class employe:
    def __init__(self, name, year_born ,salary):
        self.name = name
        self.year_born = year_born
        self.salary = salary

    def get_age(self)-> int:
        return dm.now().year - self.year_born
    
    def do_work(self):
        print(f"{self.name} is working")

    def say_hi(self):
        print(f"Hi, I'm {self.name}")
    