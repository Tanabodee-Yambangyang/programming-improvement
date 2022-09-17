"""Python Object-Oriented Programming (OOP) Exercise: Classes and Objects Exercises."""


class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity, color="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self._color = color
        self.capacity = capacity

    def __repr__(self):
        return f"Color: {self._color}, Vehicle Name: {self.name}, " \
               f"Speed: {self.max_speed}, Mileage: {self.mileage}"

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50, color="white"):
        super().__init__(name, max_speed, mileage, color)
        self.capacity = capacity

    def fare(self):
        total_fare = super().fare()
        total_fare += total_fare * 0.1
        return f"Total Bus fare is: {total_fare}"


class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=4, color="white"):
        super().__init__(name, max_speed, mileage, color)
        self.capacity = capacity
