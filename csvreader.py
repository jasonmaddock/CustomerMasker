"""
Contains one function: importreader. Opens the input .csv file and reads the
data in the table. The function transforms the data into a more usable format
and adds the data from each column to a list attached to a dictionary key.
The function will also designate the first row as the table headers. Four
Errors are watched for in this function: FileNotFound, Empty, NoData and
value. The function returns the dictionary and the headers.

"""
from errorlogger import errorhandler, errorcatagory

def importreader(filename):
    """
    Opens the input .csv file and reads the data in the table. The function
    transforms the data into a more usable format by stripping the new line
    character at the end of each row and splitting the remaining data based
    on the delimiter (,). If a value in the .csv contains the delimiter, it will
    originally be split but afterwards the function looks for two adjactent
    strings in the list, the first begginging with " and the second ending with
    " where the line length is also longer than expected. It joins them back
    together with the comma while removing the old split values. Then it adds
    the data from each column to a list attached to a dictionary key. The
    function will also designate the first row as the table headers. Two
    exceptions are watched for in this function: FileNotFound and Value along
    with detecting two possible errors: Empty and NoData. FileNotFound occurs
    when no file matching the file name is found in the scripts folder. Value
    occurs when either of the columns designated for numerical data contains
    something which cannot be formatted as an integer in one case and a float
    in the other. Empty occurs when the .csv file is blank. NoData occures
    when the .csv contains only headers. If any error is detected in this
    function, the function will send the error to the errorhandler function
    in the errorlogger module. Only the value error will allow the script to
    continue (although it will remove the offending row from it's output),
    all other errors are considered catastrophic. The function returns the
    dictionary and the headers.
    """
    errors = []
    fileinput = {"ids":[], "names":[], "emails":[], "billings":[],
    "locations":[]}
    try:
        with open(filename) as filereader:
            read = [line[:-1].split(',') for line in filereader]
            filereader.close()
    except FileNotFoundError:
        return errorcatagory(["FileNotFound", 0])
    if read == [[""]]:
        return errorcatagory(["Empty", 0])
    for line in read:  #Finds values that contained a comma and were split before re-joining them.
        for item in line:
            try:
                if item[0] == '"' and line[line.index(item)+1][-1] == '"' \
                and len(line)>5:
                    newitem = (item + ',' + line[line.index(item)+1]).strip('"')
                    line.insert(line.index(item), newitem)
                    line.pop(line.index(item)+1)
                    line.pop(line.index(item))
            except IndexError:      #If of the examined items is blank an index error is thrown.
                pass
    data = read[1:]
    headers = read[0]
    if not data:
        return errorcatagory(["NoData", 0])
    for line in data:
        try:
            fileinput['ids'].append(int(line[0]))
            fileinput['billings'].append(float(line[3]))
        except ValueError:
            errors.append(["Value", read.index(line)+1])
            continue
        fileinput['names'].append(str(line[1]))
        fileinput['emails'].append(str(line[2]))
        fileinput['locations'].append(str(line[4]))
    if errors:
        valerror = errorhandler(errors) #Only called when value errors have occured.
        return fileinput, headers, valerror
    return fileinput, headers
