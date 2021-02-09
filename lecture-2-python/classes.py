#template for a type of object
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(3, 8)

print(p)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        #list of passengers
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight1 = Flight(3)

people = ["harry", "ron", "hern", "pepe"]

for person in people:
    success = flight1.add_passenger(person)
    if success:
        print(f"Added {person} to flight")
    else:
        print(f"No seat for {person}")

