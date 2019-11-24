from datetime import datetime, timedelta
from defaultParams import *

class Bike:
    # Object init
    def __init__(self, id, arrival, departure):
        self.id = id
        self.arrivalTime = []
        self.departureTime = []
        self.averageTravelTime = 0
        if(arrival != arrival): arrival = DEFAULT_TIME_VALUE
        self.arrivalTime.append(arrival)

        if(departure != departure): departure = DEFAULT_TIME_VALUE
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
        print(self.id, self.arrivalTime, self.departureTime, self.averageTravelTime)

    # Order both arrays by time
    def orderTimes(self):
        self.arrivalTime.sort()
        self.departureTime.sort()

        self.checkTimeList()

    def checkTimeList(self):
        if (self.arrivalTime[0] < self.departureTime[0]):
            self.departureTime.insert(0, DEFAULT_TIME_VALUE)

    def calculateAverageTime(self):
        travelTimes = []

        self.updateTimeFormat()

        for i in range(len(self.arrivalTime)):
            if(self.departureTime[i] != datetime.strptime(DEFAULT_TIME_VALUE, '%Y%m%dT%H:%M:%S')):
                travelTimes.append(self.arrivalTime[i] - self.departureTime[i])

        # print(travelTimes)

        self.averageTravelTime = sum(travelTimes, timedelta()) / len(travelTimes)

        self.averageTravelTime = str(self.averageTravelTime)

    def updateTimeFormat(self):
        for i in range(len(self.arrivalTime)):
            self.arrivalTime[i] = datetime.strptime(self.arrivalTime[i], '%Y%m%dT%H:%M:%S')

        for i in range(len(self.departureTime)):
            self.departureTime[i] = datetime.strptime(self.departureTime[i], '%Y%m%dT%H:%M:%S')
    

    