from abc import ABC, abstractmethod
from tabulate import tabulate

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self):
        pass

    def get_price(self):
        return self.price

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def get_details(self):
        return ["📖 Book", self.name, f"Author: {self.author}", f"{self.price:,} บาท"]

class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def get_details(self):
        return ["💻 Electronics", self.name, f"Brand: {self.brand}", f"{self.price:,} บาท"]

class Clothing(Product):
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return ["👕 Clothing", self.name, f"Size: {self.size}, Material: {self.material}", f"{self.price:,} บาท"]

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"✅ Added to cart: {product.name}")

    def total_price(self):
        return sum(item.get_price() for item in self.items)

    def show_cart(self):
        if not self.items:
            print("🛒 ตะกร้าว่างเปล่า")
            return

        print("\n🛒 Cart Items:")
        headers = ["Type", "Name", "Details", "Price"]
        table = [item.get_details() for item in self.items]
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        print(f"\n💰 Total Price: {self.total_price():,} บาท")

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def checkout(self):
        self.cart.show_cart()
        print(f"🛍️ {self.name} has completed the purchase!")

    def search_product(self, keyword, search_all=False):
        search_list = all_products if search_all else self.cart.items
        results = [item for item in search_list if keyword.lower() in item.name.lower()]

        if results:
            print("\n🔍 Search Results:")
            headers = ["Type", "Name", "Details", "Price"]
            table = [item.get_details() for item in results]
            print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
        else:
            print("❌ No matching products found.")

all_products = [
    Electronics("Laptop", 1200, "Apple"),
    Electronics("Smartphone", 800, "Samsung"),
    Clothing("T-Shirt", 25, "L", "Cotton"),
    Clothing("Jacket", 90, "M", "Leather"),
    Book("Python Programming", 50, "John Doe"),
    Book("Machine Learning Basics", 60, "Jane Smith")
]

if __name__ == "__main__":
    user1 = User("Alice")
    user1.add_to_cart(all_products[0])
    user1.add_to_cart(all_products[2])
    user1.checkout()

    while True:
        search_mode = input("\n🔎 ค้นหาจาก (1) ตะกร้า หรือ (2) สินค้าทั้งหมด? (พิมพ์ 'exit' เพื่อออก): ").strip()
        if search_mode.lower() == "exit":
            print("👋 ออกจากระบบค้นหา")
            break

        keyword = input("🔍 พิมพ์คำที่ต้องการค้นหา: ").strip()
        if search_mode == "1":
            user1.search_product(keyword)
        elif search_mode == "2":
            user1.search_product(keyword, search_all=True)
        else:
            print("⚠️ กรุณาเลือก 1 หรือ 2 เท่านั้น")
