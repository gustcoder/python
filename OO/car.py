class Car:

    title = 'Cars are cool'
    
    def __init__(self, name, brand, year, color):
        self.name = name
        self.brand = brand
        self.year = year
        self.color = color

    
    def start(self):
        print(self.name + ' started.')


    @staticmethod
    def showDescription(): #nao tem acesso a nada, nem ao self
        print('This is a class about cars.')


    @classmethod
    def showTitle(carClass):
        print(carClass.title)
