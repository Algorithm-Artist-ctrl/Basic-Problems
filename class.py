class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print("Brand:", self.brand, "| Model:", self.model)

c = Car("Toyota", "Corolla")
c.info()
