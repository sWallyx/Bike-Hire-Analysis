from datetime import datetime, timedelta
from defaultParams import *
from miscFunctions import checkNaNValue

class Bike:
    
    def __init__(self, id, arrival, departure):
        self.id = id
        self.arrivalTime = []
        self.departureTime = []
        self.averageTravelTime = 0

        arrival = checkNaNValue(arrival)
        self.arrivalTime.append(arrival)

        departure = checkNaNValue(departure)
        self.departureTime.append(departure)

    def setTimes(self, arrival, departure):
        """
        Adds arrival and departure times to the object

        Arguments:
            IN -- arrival {String}, departure {String}
        """

        self.arrivalTime.append(arrival)
        self.departureTime.append(departure)

    def getFirstArrival(self):
        """
        Returns the first arrival time. It is used to reutilize temporal object, and not duplicate bikes.

        Arguments:
            OUT -- arrival {String}
        """

        return self.arrivalTime[0]

    def getFirstDeparture(self):
        """
        Returns the first arrival time. It is used to reutilize temporal object, and not duplicate bikes.

        Arguments:
            OUT -- arrival {String}
        """

        return self.departureTime[0]

    def printObject(self):
        """
        Prints the object for debug purpose, not used in the application
        """

        print(self.id, self.arrivalTime, self.departureTime, self.averageTravelTime)

    def orderTimes(self):
        """
        Orders all times, arrival and departures as ASC. Then check for missing times.
        """

        self.arrivalTime.sort()
        self.departureTime.sort()

        self.checkTimeList()

    def checkTimeList(self):
        """
        Checks if there are missing datetimes. If there are, it adds the default time value.
        """

        # Condition of a travel: Arrival > Departure; if false, fix the missing datetime record.
        if (self.arrivalTime[0] < self.departureTime[0]):
            self.departureTime.insert(0, DEFAULT_TIME_VALUE)

    def calculateAverageTime(self):
        """
        Call the update format function. And fill an array of travelTimes with the times of each trip.
        """
        travelTimes = []

        self.updateTimeFormat()

        for i in range(len(self.arrivalTime)):
            # If departure time maches with the default time. We dont need to calculate that trip, we dont know the real departure time
            if(self.departureTime[i] != datetime.strptime(DEFAULT_TIME_VALUE, TIME_FORMAT)):
                travelTimes.append(self.arrivalTime[i] - self.departureTime[i])

        self.averageTravelTime = sum(travelTimes, timedelta()) / len(travelTimes)

        # Make the DateTime variable more user friendly
        self.averageTravelTime = str(self.averageTravelTime)

    def updateTimeFormat(self):
        """
        Update the format of the all time variables to Datetime from String
        """
        for i in range(len(self.arrivalTime)):
            self.arrivalTime[i] = datetime.strptime(self.arrivalTime[i], TIME_FORMAT)

        for i in range(len(self.departureTime)):
            self.departureTime[i] = datetime.strptime(self.departureTime[i], TIME_FORMAT)
