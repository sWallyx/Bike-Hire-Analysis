

class Bike:
    # Object init
    def __init__(self, id, arrival, departure):
        self.id = id
        self.arrivalTime = []
        self.departureTime = []

        self.arrivalTime.append(arrival)
        self.departureTime.append(departure)

    # Add new times to the object from the records
    def setTimes(self, arrival, departure):
        self.arrivalTime.append(arrival)
        self.departureTime.append(departure)

    # Get first time only, for temporal objects
    def getFirstArrival(self):
        return self.arrivalTime[0]

    # Get first time only, for temporal objects
    def getFirstDeparture(self):
        return self.departureTime[0]

    # Function to print the object and check if everything is OK
    def printObject(self):
        print(self.id, self.arrivalTime, self.departureTime)

    # Order both arrays by time
    def orderTimes(self):
        self.arrivalTime.sort()
        self.departureTime.sort()
        

    