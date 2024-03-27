from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import datetime

class Golem:
    population = 0
    __life_span = 10

    def __init__(self, name=None):   #__init__为class中的一个method
        self.name = name
        self.built_year = datetime.date.today().year
        self.__active = True
        Golem.population += 1
            
    def say_i(self):
        print("Say Hi!")

    def cease(self):
        self.__active = False
        Golem.population -= 1

    def is_active(self):
        if datetime.date.today().year - self.built_year >= Golem.__life_span:
            self.cease()
        return self.__active

class Running_Golem(Golem):

    def run(self):
        print("Can't you see ? I'm here waiting for you...")

    def say_i(self):
        print("Hey ! Nice day, Huh ?")

g = Golem()
rg = Running_Golem('Galiy')

hasattr(Golem, 'population')
hasattr(g, 'population')
hasattr(Golem, '__life_span')
hasattr(g, '__active')
hasattr(Golem, 'is_active')

rg.run()
rg.run
rg.built_year
rg.name
rg.say_i()
hasattr(rg, 'built_year')