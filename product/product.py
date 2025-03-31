from abc import ABC, abstractmethod

# สร้างคลาส Product
class Product(ABC):
    def __init__(self, name, price):  # แก้ชื่อเมธอด __init__
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self):
        pass  # เป็น abstract method

    def get_price(self):
        return self.price
    
# สร้างคลาส Book ที่สืบทอดมาจาก Product
class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def get_details(self):
        return f"Book: {self.name}, Author: {self.author}, Price: {self.price} บาท"
    
# สร้างคลาส Electronics ที่สืบทอดมาจาก Product
class Electronics(Product):
    def __init__(self, name, price, brand):  # ลบอาร์กิวเมนต์ที่เกินมา
        super().__init__(name, price)
        self.brand = brand

    def get_details(self):
        return f"Electronics: {self.name}, Brand: {self.brand}, Price: {self.price} บาท"

# สร้างคลาส Clothing ที่สืบทอดมาจาก Product 
class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"👕 {self.name} - Size: {self.size}, Material: {self.material}, Price: ${self.price}"
    
# สร้างคลาส Cart
class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"✅ Added to cart: {product.get_details()}")

    def total_price(self):
        return sum(item.get_price() for item in self.items)

    def show_cart(self):
        print("\n🛒 Cart Items:")
        for item in self.items:
            print(f"- {item.get_details()}")
        print(f"💰 Total Price: ${self.total_price()}")

# สร้างคลาส User
class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def checkout(self):
        self.cart.show_cart()
        print(f"🛍️ {self.name} has completed the purchase!")

# 🔥 ทดลองใช้งานระบบ
if __name__ == "__main__":
    # สร้างสินค้า
    laptop = Electronics("Laptop", 1200, "Apple")  # แก้ไขจำนวนอาร์กิวเมนต์
    t_shirt = Clothing("T-Shirt", 25, "L", "Cotton")
    book = Book("Python Programming", 50, "John Doe")

    # สร้างผู้ใช้
    user1 = User("Alice")

    # ผู้ใช้เพิ่มสินค้าในตะกร้า
    user1.add_to_cart(laptop)
    user1.add_to_cart(t_shirt)

    # แสดงตะกร้าและ Checkout
    user1.checkout()
