#!/usr/bin/python3
# coding=utf-8
import os
import pandas as pd
from bike import Bike

def readCSV(name):
    """
    Function name: readCVS
    Description: Using pandas reads the CSV, with no headers, indicated by param and returns it

    Arguments: 
        IN -- route to CSV file
        OUT -- data object
    """
    
    CSVdata = pd.read_csv(name, header=None, encoding='utf-8-sig')

    # print(CSVdata)

    return CSVdata


def createObjects(csvData):
    """
    Function name: createObjects
    Description: Using the CSV file data, creates all bike objects with no duplicates.

    Arguments: 
        IN -- CSV data
        OUT -- Bike Objects
    """

    bikes = []

    # Get the number of records in the data
    for i in range(len(csvData.index)):
        # Create a temporal object
        temporalBikeObject = Bike(csvData[1][i], csvData[2][i], csvData[3][i])

        existingBike = checkIfExist(bikes, temporalBikeObject)

        if(not existingBike):
            # Add new bike to list
            bikes.append(temporalBikeObject)
        else:
            # If the bike exists add times to existing bike
            existingBike.setTimes(temporalBikeObject.getFirstArrival(),temporalBikeObject.getFirstDeparture())

    return bikes

def checkIfExist(bikes, bikeToCheck):
    """
    Function name: checkIfExist
    Description: Checks if the ID of the bike already exist in the object list.

    Arguments: 
        IN -- Bike list, bike object to check
        OUT -- Bike object if exists, False if does not exist
    """

    for bike in bikes:
        if bikeToCheck.id == bike.id:
            return bike

    return False


def orderObjectsByTime(bikeObjects):
    """
    Function name: orderObjectsByTime
    Description: Calls the order function of each object.

    Arguments: 
        IN -- Bike list
    """

    for bike in bikeObjects:
        bike.orderTimes()


def calculateBikeAverageTimes(bikeObjects):
    """
    Function name: calculateBikeAverageTimes
    Description: Calls the calculate average trip time.

    Arguments: 
        IN -- Bike list
    """

    for bike in bikeObjects:
        bike.calculateAverageTime()

def showAverageTimeForBike(bikeObjects):
    """
    Function name: showAverageTimeForBike
    Description: Shows the average trip time of each bike.

    Arguments: 
        IN -- Bike list
    """

    for bike in bikeObjects:
        print("Bike: ", bike.id, " has a travel average time of: ", bike.averageTravelTime)


def main():
    # Get the data from the CSV
    csvData = readCSV("Bike-Hire-Analysis/data/data.csv")

    # Add data to bike objects
    bikeObjects = createObjects(csvData)

    # Order objects time => order type, ASC and fix missing times
    orderObjectsByTime(bikeObjects)

    # Run the class function to calcule the travel average time
    calculateBikeAverageTimes(bikeObjects)

    # Run the class function to calcule the travel average time
    showAverageTimeForBike(bikeObjects)


if __name__ == "__main__":
    main()

    print("Program ended.")