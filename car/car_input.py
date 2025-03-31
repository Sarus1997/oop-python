# สร้าง class car 
# เวอรชัน ที่มีการค้นหารถยนต์

# สร้าง class car
from tabulate import tabulate

class Car:
    def __init__(self, brand, model, year=None, price=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def to_list(self):
        return [self.brand, self.model, self.year, f"{self.price:,} บาท"]

    @classmethod
    def search_cars(cls, cars, **kwargs):
        results = []
        for car in cars:
            match = True
            for key, value in kwargs.items():
                if not hasattr(car, key) or getattr(car, key) != value:
                    match = False
                    break
            if match:
                results.append(car)
        return results

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

brand = input("ค้นหาด้วย brand (หรือ เว้นว่างไว้สำหรับทั้งหมด): ")
model = input("ค้นหาด้วย model (หรือ เว้นว่างไว้สำหรับทั้งหมด): ")
year = input("ค้นหาด้วย year (หรือ เว้นว่างไว้สำหรับทั้งหมด): ")
price = input("ค้นหาด้วย price (หรือ เว้นว่างไว้สำหรับทั้งหมด): ")

kwargs = {}
if brand:
    kwargs['brand'] = brand
if model:
    kwargs['model'] = model
if year:
    kwargs['year'] = int(year)
if price:
    kwargs['price'] = int(price)

results = Car.search_cars(cars, **kwargs)

if results:
    headers = ["Brand", "Model", "Year", "Price"]
    table = [car.to_list() for car in results]
    print("\nผลลัพธ์การค้นหา:\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
else:
    print("\n\033[91mไม่มีข้อมูลไอน้อง 😫\033[0m")
