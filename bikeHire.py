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
    bikes = []
    # Get the number of records in the data
    for i in range(len(csvData.index)):
        # Create a temporal object
        temporalBikeObject = Bike(csvData[1][i], csvData[2][i], csvData[3][i])

        existingBike = checkIfExist(bikes, temporalBikeObject)

        if(not existingBike):
            bikes.append(temporalBikeObject)
        else:
            existingBike.setTimes(temporalBikeObject.getFirstArrival(),temporalBikeObject.getFirstDeparture())

    return bikes


def printObjects(bikes):
    print(" ++++ Check Objects ++++")
    for bike in bikes:
        print(bike.printObject())


def checkIfExist(bikes, bikeToCheck):
    for bike in bikes:
        if bikeToCheck.id == bike.id:
            return bike

    return False


def orderObjectsByTime(bikeObjects):
    for bike in bikeObjects:
        bike.orderTimes()


def calculateBikeAverageTimes(bikeObjects):
    for bike in bikeObjects:
        bike.calculateAverageTime()

def isNaN(num):
    return num != num

def showAverageTimeForBike(bikeObjects):
    for bike in bikeObjects:
        print("Bike: ", bike.id, " has a travel average time of: ", bike.averageTravelTime)

# Get the data from the CSV
csvData = readCSV("data/data.csv")

# Add data to bike objects
bikeObjects = createObjects(csvData)

# Order objects time => order type, ASC
orderObjectsByTime(bikeObjects)

# Run the class function to calcule the travel average time
calculateBikeAverageTimes(bikeObjects)

# Run the class function to calcule the travel average time
showAverageTimeForBike(bikeObjects)

# Print objects for debug
# printObjects(bikeObjects)
