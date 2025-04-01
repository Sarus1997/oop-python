class Car:
    def __init__(self, brand, model, year=None, price=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    @staticmethod
    def search(cars, brand=None, price=None):
        return [car for car in cars if (brand is None or car.brand == brand) and (price is None or car.price == price)]

cars = [
    Car("Toyota", "Corolla", 2020, 800000),
    Car("Honda", "Civic", 2021, 900000),
    Car("Toyota", "Camry", 2019, 700000),
    Car("Honda", "Accord", 2020, 850000),
    Car("Toyota", "Corolla", 2021, 820000),
    Car("Honda", "Civic", 2022, 920000),
    Car("Toyota", "Camry", 2021, 750000),
    Car("Honda", "Accord", 2022, 880000),
]

brand = input("Select brand: ")
price_input = input("Select price: ")
price = int(price_input) if price_input.isdigit() else None

kwargs = {}
if brand:
    kwargs['brand'] = brand
if price is not None:
    kwargs['price'] = price

results = Car.search(cars, **kwargs)

if results:
    print("Results:")
    for car in results:
        print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Price: {car.price} Bath")
else:
    print("No match found.")
