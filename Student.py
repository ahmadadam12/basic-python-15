class Student:
    
    def __init__(self, name, major, gpa):
        self.name=name
        self.major=major
        self.gpa=gpa
    
    def on_honor_roll(self):
        if self.gpa>=3.5:
            return True
        else:
            return False
        
class Chef:
    
    def make_chicken(self):
        print("I make chicken")
    def make_salad(self):
        print("I make salad")
    def make_special_dish(self):
        print("I make special dish")
        
