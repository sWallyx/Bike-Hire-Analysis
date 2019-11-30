# Bike Hire Analysis

A bike hire scheme consists of a number of bike hire stations from which bikes can be rented.

Python console application to analyze a CSV containing bike hire station records. The goal is to calculate the average travel time for each bike for the reporting period, in format hh:mm:ss. The file to analyze is data.csv which is included in the data folder.

## The Records

The CSV records have the following structure, and it has no headers.

| Station ID | Bike ID | Arrival Datetime  | Departure Datetime |
|------------|---------|-------------------|--------------------|
| 22         | 102     | 20150304T13:04:00 | 20150304T13:25:32  |
| 4          | 34      |                   | 20150301T05:15:08  |

* **Station ID**: Integer, representing the bike hire station. Valid values: 1-1,000.
* **Bike ID**: Integer, representing the bike itself. Valid values: 1-10,000.
* **Arrival Datetime**: Datetime in format YYYYMMDDThh:mm:ss. Representing the date/time the bike arrived at the station. It is empty if the bike was at this station at the start of the reporting period.
* **Departure Datetime**: Datetime in format YYYYMMDDThh:mm:ss. Representing the date/time the bike departed from the station. It is empty if the bike was at this station at the end of the reporting period.


## Requirements

The application needs [panda module](https://pandas.pydata.org). It can be installed using:

````
pip3 install pandas
````

## What the application does

### Read the CSV

First, the application reads the data.csv file and stores it in a variable.

### Create Bike Objects

The next step is to create bike objects, because of having multiple records of each bike, we need to check if the bike object already exists. If that is the case. We add the arrival and departure times to the existing object instead of creating a new one (although we already created a temporal object). If the datetime does not exist, because is not in the document. Set it to the default time (00010101T00:00:00).

### Order

Order the datetimes inside each bike ascendent. The objective of this is to have in the same position, of the list the details of all the travels. So we can join each position to have the initial and end time of the travel.

### Check for datetimes

Now we need to check that all the travel datetime sorted are in the correct position. For that, we need to have in mind that a journey must have the datetimes as follows: Arrival > Departure;

Because you can not reach your destination, earlier than departing. If this condition is not met. We modify the datetimes adding a missing Departure. So the bike was not in a station on the report starting period.

### Parse times

Next is to update the format of the datetimes, until now, they were string. So, convert it to Datetime.


### Get travel duration

Get the duration of each travel. 
````
Arrival time - Departure time = Travel time
````

### Get the average travel time

Using sum and timedelta(). Get the average time of all travels stored. And print it on the console.


## Optimizations

The list of optimizations the application could have:

* Remove the need of creating a temporal object, and check if the object exist with the table of the data, insted of a temporal object.

## License

[MIT - License](LICENSE.md)