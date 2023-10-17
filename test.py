"""This module is designed to test the Customer Masker script. It contains one
function which passes a file through the functions used in the main module.
Numerous files are fed into this function which predetermined errors. The
function catches these errors and reports a pass if they're expected. If an
error occurs unexpectedly it will print a fail to the console along with a log
detailing which file failed the tests. If this module is run directly, it will
pass each file in the Tests folder into the function and generate a report
stating pass or fail for each file passed through it. Displaying an overall
pass if all files passed or fail is one or more failed.
"""

import os
from classcreator import Customers
from errorlogger import errorhandler
from csvreader import importreader
from csvwriter import rowmaker, outputwriter
import re

def tester(filename, file):
    """The tester function takes two arguments, the absolute path of the file
    it is testing and the file name of the tested file. First the function
    passes the file through the import reader function, looking at the result
    length and type in order to detect an error. The expected result is a
    tuple containing two items. A tuple with three items is expected in the case
    of a value error. All other error types will result in a list with one item.
    Next the function tests feeding the test data into the Customer object. it
    will check the outputs of the two masking functions within this class
    against the desired result, generated using list comprehension and regular
    expressions for the strings and calculate the average for each of the
    numbers. The function then tests the outputwriter function before testing
    the reportwriter function. For the report writer the function will generate
    the ideal report using the class attributes and then check the functions
    report against this. Files containing known errors are named the error they
    contain and passed through. If one of these errors is passed into the
    function but the file name matches the error type, this will still be a
    pass. At each stage, the function will either return the string "FAIL" if
    the test is failed, "PASS" if an expected error is caught, or "PASS" if a
    file makes it to the end of the function without encountering an error.
    """
    try:
        csvtest = importreader(filename)
        if isinstance(csvtest, tuple) and len(csvtest) == 2:
            tabledata = csvtest[0]
            tableheaders = csvtest[1]
        elif isinstance(csvtest, tuple) and len(csvtest) == 3:
            if csvtest[2].split(":")[0] == file.split(".")[0]:
                return "PASS"
        elif csvtest[0].split(":")[0] == file.split(".")[0]:
            return "PASS"
    except:
        return "FAIL at importreader function"
    try:
        database = Customers(**tabledata)
        maskednums = database.masknum()
        maskedtext = database.masktext()
        if ([re.sub(r'[^@.,]', r"X", name) for name in database.names] !=       #Regular expessions and list comprehension to simulate masking the strings
        [name for name in maskedtext[0]]):
            return "FAIL at maskedtext function in masknames"
        elif ([re.sub(r'[^@.,]', r"X", email) for email in database.emails] !=
         [email for email in maskedtext[1]]):
            return "FAIL at maskedtext function in maskemails"
        elif (
        [re.sub(r'[^@,.]', r"X", location) for location in database.locations]
         != [location for location in maskedtext[2]]):
            return "FAIL at maskedtext function in masklocations"
        elif maskednums[0] != sum(database.ids)/len(database.ids):
            return "FAIL at maskednums function in maskids"
        elif maskednums[1] != sum(database.billings)/len(database.billings):
            return "FAIL at maskednums function in maskbillings"
    except:
        return "FAIL at Customers class"
    try:
        outputwriter(rowmaker(maskedtext,maskednums), tableheaders)
    except:
        return "FAIL at outputwriter function"
    try:
        report = database.reportwriter()
        reportdata = f"""
Name:    Avg. {sum(map(len, database.names))/len(database.names):.2f}, Min. {len(min(database.names, key=len))}, Max. {len(max(database.names, key=len))}
Billing: Avg. {sum(database.billings)/len(database.billings):.2f}, Min. {min(database.billings)}, Max. {max(database.billings)}
"""
        if reportdata != report:
            return "FAIL"
    except:
        return "FAIL at reportwriter function"
    return "PASS"

if __name__ == "__main__":
    testdir = os.path.join(os.getcwd(), "Tests")
    results = []
    fail = False
    for file in os.listdir(testdir):
        outcome = [file, tester(os.path.join(testdir, file), file)]
        print(outcome)
        if "FAIL" in outcome[1]:
            fail = True
        results.append(outcome)
    if fail:
        print("FAIL - a test failed. Please check the log above")
    else:
        print("PASS - All tests passed!")
