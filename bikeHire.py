#!/usr/bin/python3
# coding=utf-8
import os
import pandas as pd
from bike import Bike


def readCSV(name):
    # Get the data from the CSV
    data = pd.read_csv(name, header=None, encoding='utf-8-sig')

    print(data)

    return data

    # Get Data Lenght
    # for i in range(len(data.index)):
    #     # All except Id need to have a space in front
    #     tmp = Product(data['Id'][i], checkAndReplace(data[' Name'][i]), checkAndReplace(data[' Brand'][i]), checkAndReplace(
    #         data[' Retailer'][i]), checkAndReplace(data[' Price'][i]), checkAndReplace(data[' InStock'][i]))

    #     products.append(tmp)


def createObjects(csvData):
    bikes = []
    # Get the number of records in the data
    for i in range(len(csvData.index)):
        # Create a temporal object
        temp = Bike(csvData[1][i], csvData[2][i], csvData[3][i])

        existingBike = checkIfExist(bikes, temp)

        if(not existingBike):
            bikes.append(temp)
        else:
            existingBike.setTimes(temp.getFirstArrival(), temp.getFirstDeparture())

    return bikes


def printObjects(bikes):
    print(" ++++ Check Objects ++++")
    for bike in bikes:
        print(bike.printObject())


def checkIfExist(bikes, checkBike):
    for bike in bikes:
        if checkBike.id == bike.id:
            return bike

    return False


def orderObjectsByTime(bikeObjects):
    for bike in bikeObjects:
        bike.orderTimes()

# Get the data from the CSV
csvData = readCSV("data/data.csv")

# Add data to bike objects
bikeObjects = createObjects(csvData)

orderObjectsByTime(bikeObjects)

printObjects(bikeObjects)