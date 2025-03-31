# สร้าง class car 
# เวอรชัน ง่ายๆ
class car :
    def __init__(self, brand, model, year=None, price=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def make_car(self):
        return f"{self.brand} รุ่น {self.model} ปี {self.year} ราคา {self.price} บาท 🚗"
    
# สร้าง Object ของ class car
car1 = car("Toyota", "Corolla", 2020, 800000)
car2 = car("Honda", "Civic", 2021, 900000)

print(car1.make_car())
print(car2.make_car())