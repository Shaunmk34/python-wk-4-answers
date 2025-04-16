# Activity 1

class Animal:
    def __init__(self, name, age):
        self.name = name  
        self.age = age 

    def eat(self):     
        print(f"{self.name} is eating.")

    def sleep(self):    
        print(f"{self.name} is sleeping.")

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age) 
        self.breed = breed          

    def bark(self):        
        print("Woof! Woof!")

    # Overriding the eat method from parent
    def eat(self):
        print(f"{self.name} the {self.breed} is eating dog food.")

# Cat class inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print("Meow!")

    # Now to override the sleep method
    def sleep(self):
        print(f"The {self.color} cat is purring while sleeping.")

# Create objects
my_dog = Dog("Danger", 3, "African breed dog")
my_cat = Cat("kitty", 2, "gray")


# Activity 2
class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying!")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming!")

class pig(Animal):
    def move(self):
        print(f"{self.name} is running!")

# Create different animals
animals = [
    Bird("Ndevu", 1),
    Fish("Mzimba", 2),
    pig("Peppa", 5)
]

# They all have move() but behave differently
for animal in animals:
    animal.move()