import datetime

class Golem:

    def __init__(self, name=None):   #__init__为class中的一个method
        self.name = name
        self.built_year = datetime.date.today().year
            
    def say_i(self):
        print("Say Hi!")

class Running_Golem(Golem):

    def run(self):
        print("Can't you see ? I'm here waiting for you...")

    def say_i(self):
        print("Hey ! Nice day, Huh ?")

rg = Running_Golem('Galiy')

rg.run()
rg.run
rg.built_year
rg.name
rg.say_i()
hasattr(rg, 'built_year')