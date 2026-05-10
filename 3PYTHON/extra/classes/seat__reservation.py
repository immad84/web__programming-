class Flight:
     def __init__(self, capacity):
          self.capacity = capacity;
          self.passengers = []

     def add_passenger(self, person):
          if not self.available_seats():
               return False;
          self.passengers.append(person)
          return True
     
     def available_seats(self):
          return self.capacity - len(self.passengers);


flight = Flight(3)
people = ["Harry", "Hermoine", "Ron", "Draco"]
for person in people:
     if flight.add_passenger(person):
          print(f"{person} Booked For Flight.")
     else:
          print("No Seats Available. ")