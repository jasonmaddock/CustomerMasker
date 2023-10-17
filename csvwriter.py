"""
Contains two functions which are used in tandem write to the csv file. rowmaker
takes the output of the maskedtext and maskednums functions from within the
Customer object and adds them to a dictionary before adding that dictionary to
a list which it returns. outputwriter takes a list of dictioanries and the
tableheaders identified in the importreader function. It will write the
tableheaders to the first row of the .csv and then for each dictionary in the
list write the values of the dictionary to a new line.
"""
from errorlogger import errorhandler

def rowmaker(maskedtext,maskednums):
    """Takes a list containing three lists of strings and a list containing
    two numbers. If a comma is present in any of the strings, the function will
    wrap the string in double quotes to preseve the data when it's written to
    the .csv. The three lists of strings are then aggregated into tuples,
    each tuple containing one value from each list. Using these tuples and the
    list containing the numbers a dictionary is constructed and appended to a
    list. Once the tuples have been iterated through and a dict created for each
    of them, the list of dictionaries is returned.
    """
    output = []
    for row in maskedtext:  #If a comma is in one of the substrings, the string is wrapped in double quotes to avoid a misformat whe writing to the .csv
        for item in row:
            if "," in item:
                newitem = '"' + item + '"'
                row.insert(row.index(item), newitem)
                row.pop(row.index(item))
    for name,email,location in zip(maskedtext[0],maskedtext[1],maskedtext[2]):
        line = {"id" : maskednums[0], "name": name, "email" : email,
         "billing": maskednums[1], "location": location}
        output.append(line)
    return output

def outputwriter(output,headers):
    """Takes a list of dicts and a list of strings. Opens a .csv file or creates
    one if it doesn't exist. Writes the list of strings to the first row of the
    csv file and then for each dictionary in the list, writes the values of the
    dictionary to a new line. An exception is provided for a permission error.
    Caused by the file the function is attempting to write to already being
    open. In this case the error code "PermissionError" is returned with a
    position of 0
    """
    try:
        with open("masked_clients.csv", "w") as filewriter:
            filewriter.write(f"{headers[0]},{headers[1]},{headers[2]},{headers[3]},{headers[4]}\n")
            for line in output:
                filewriter.write(f"{line['id']},{line['name']},{line['email']},{line['billing']},{line['location']}\n")
            filewriter.close()
    except PermissionError:
        return errorcatagory(["PermissionError", 0]) #Error if the user has left the target file open
