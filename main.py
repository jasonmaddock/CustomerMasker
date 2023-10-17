"""
The main file of the customer masking script. If this file is run directly it
will use the functions and classes outlined in its accompanying modules to
read data from a .csv file, create the Customers() object to contain this data,
use the maskednums and maskedtext functions to anonymise the data before writing
it to an export file. The script will also handle any errors that result from
the user input by skipping the data entries containing the error, while making
the user aware of the location of the error, or if that is not possible, cease
the execution of the script but notify the user of the error type and provide
them with assistance on how to fix the error. Finally the script will print a
report showing stats for the Name and Billing attributs of the Customers object.

This script depends on the following modules in order to function:
classcreator
errorlogger
csvreader
csvwriter

"""

from classcreator import Customers
from errorlogger import errorhandler
from csvreader import importreader
from csvwriter import rowmaker, outputwriter

if __name__ == "__main__":
    filename = "customers.csv"
    csvoutput = importreader(filename)
    if len(csvoutput) == 1:
        print(csvoutput[0])
        exit()
    elif len(csvoutput) == 3:
        print(str(csvoutput[2]))
    tabledata = csvoutput[0]
    tableheaders = csvoutput[1]
    database = Customers(**tabledata)
    maskednums = database.masknum()
    maskedtext = database.masktext()
    outputwriter(rowmaker(maskedtext,maskednums), tableheaders)  #### CHECK perm error
    print(database.reportwriter())
