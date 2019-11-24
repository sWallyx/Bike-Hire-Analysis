# Bike Hire Analysis

A bike hire scheme consists of a number of bike hire stations from which bikes can be rented.

Python console application to analyze a CSV containing bike hire station records. The goal is to calculate the average travel time for each bike for the reporting period, in format hh:mm:ss. The file to analyze is data.csv which is included in the data folder.

## The Records

The CSV records have the following structure, and it has no headers.

| Station ID | Bike ID | Arrival Datetime  | Departure Datetime |
|------------|---------|-------------------|--------------------|
| 22         | 102     | 20150304T13:04:00 | 20150304T13:25:32  |
| 4          | 34      |                   | 20150301T05:15:08  |

* Station ID: Integer, representing the bike hire station. Valid values: 1-1,000.
* Bike ID: Integer, representing the bike itself. Valid values: 1-10,000.
* Arrival Datetime: Datetime in format YYYYMMDDThh:mm:ss. Representing the date/time the bike arrived at the station. It is empty if the bike was at this station at the start of the reporting period.
* Departure Datetime: Datetime in format YYYYMMDDThh:mm:ss. Representing the date/time the bike departed from the station. It is empty if the bike was at this station at the end of the reporting period.


## Requirements

The application needs [panda module](https://pandas.pydata.org). It can be installed using:

````
pip3 install pandas
````


## License

MIT - License