class Car:
    def __init__(self, brand, name):
        self.name = name
        self.brand = brand

    def start_engine(self):
        print("Start the engine of ", self.name, "Whose brand is ", self.brand)