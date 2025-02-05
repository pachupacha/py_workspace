import random
import string

class Station:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

class TrainNetwork:
    def __init__(self):
        self.stations = {
            "Tokyo": Station("Tokyo", 320),
            "Sasuke": Station("Sasuke", 180),
            "Tekaido": Station("Tekaido", 260),
            "Meishi": Station("Meishi", 150),
            "Kyoto": Station("Kyoto", 410),
            "Osaka": Station("Osaka", 230),
            "Hiroshima": Station("Hiroshima", 500),
            "Nagasaki": Station("Nagasaki", 340),
            "Fukuoka": Station("Fukuoka", 290)
        }
    
    def generate_ticket_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    def calculate_fare(self, start, destination):
        if start not in self.stations or destination not in self.stations:
            return "Invalid station."
        
        station_keys = list(self.stations.keys())
        start_index = station_keys.index(start)
        destination_index = station_keys.index(destination)
        
        if start_index == destination_index:
            return "You are already at your destination."
        
        step = 1 if start_index < destination_index else -1
        total_cost = sum(
            self.stations[station_keys[i]].fare for i in range(start_index + step, destination_index + step, step)
        )
        
        ticket_id = self.generate_ticket_id()
        
        return f"The ticket cost from {start} to {destination} is {total_cost} yen. Ticket ID: {ticket_id}"

network = TrainNetwork()
start_station = input("Enter your departure station: ")
destination_station = input("Enter your destination: ")
print(network.calculate_fare(start_station, destination_station))