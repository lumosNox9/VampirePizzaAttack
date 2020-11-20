class Monster(object):
    eats = 'food'

    #methods
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name + ' speaks')

    def eat(self, meal):
        if meal == self.eats:
            print('yum')
        else:
                print('blech')
