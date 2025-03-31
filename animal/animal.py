# สร้าง class Animal

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}"

# สรhาง Object ของ class Animal
dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

print(dog.make_sound())
print(cat.make_sound())


# สร้าง class Dog ที่สืบทอดมาจาก class Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed} dog"

dog = Dog("Buddy", "Golden Retriever")
print(dog.make_sound())
print(dog.info())

# สร้าง class Cat ที่สืบทอดมาจาก class Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Meow")
        self.color = color

    def info(self):
        return f"{self.name} is a {self.sound} cat"
    
cat = Cat("Whiskers", "Black")
print(cat.make_sound())
print(cat.info())
