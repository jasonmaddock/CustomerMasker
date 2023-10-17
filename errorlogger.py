"""
Contains three functions each used in the construction of error messages aswell
as a dictionary used to store the error message that will be sent to the user.
Errorhandler takes a list of lists, each of these nested lists will contain
the error type and the error position. Each of the errors in the list are passed
individually to the error catagory function. The error catagory function takes
an individual error and assesses it based on it's type. It will pull the
relevant error text for the error type and if the error is considered
catastrophic ("Empty", "NoData", "FileNotFound", "PermissionError"), it will
return an error message. If the error is recoverable (Value),the function will
return the error type, error position and error text to the errorhandler
function. The errorhandler will then append the returned information as a list
into the errorlist variable. Once all of the errors have been iterated through,
provided a catastrophic error hasn't exited the script, the error handler
function will pass the errorlist into the valerrormessage function. This
function will take the list of errors and create an error message. returning the
error message in the first error item and the positions of each error in the
list.

"""
import sys


errortext = {
"Value":"""ValueError: One or more value errors were detected while masking your
 data. While the script has run successfully, the rows containing these errors
 have been excluded from the results! These errors were caused by an unexpected
 entry in either the ID or Billing columns of the input file. These columns can
 only contain numbers, they cannot contain text or be blank. If you have left
 the billing blank for a record because the billing is zero, please enter 0
 instead. Please find below which rows in the input file need to be
 addressed.""",
"Empty":"""EmptyError: An empty error was detected while masking your data. This
is caused when the source .csv file doesn't contain any data. Please check your
source file and re-run the script.""",
"NoData":"""NoDataError: A no data error was detected while masking your data.
This is cause by the source file containing headings but no data underneath
them. Please check your source file and re-run the script.""",
"FileNotFound":"""FileNotFoundError: A file not found error was detected while
masking your data. This is caused when the source file cannot be located.
Please ensure that the source file is in the same directory as this script and
is named "customer.csv.""",
"PermissionError":"""PermissionError: A permission error was detected while
masking your data. This is caused when you have the output file
"masked_clients.csv" open while attempting to run the script. Please close the
file and re-run the script again. """
}

def errorhandler(errors):
    """Takes a list of lists, each of these nested lists will contain
    the error type and the error position. These errors are iterated through and
    passed to the error catagory function. The result of the errorcatagory
    function is then appended to the errorlist variable. Once all errors have
    been iterated through, the error list is passed to the valerrormessage
    function.
    """
    errorlist = []
    for error in errors:
        errorlist.append(errorcatagory(error))
    return valerrormessage(errorlist)

def errorcatagory(error):
    """Takes a list containing a string and an integer. It sets the string as
    the errortype and the integer as the errorposition. It will pull the
    relevant error text for the error type and if the error is
    considered catastrophic ("Empty","NoData", "FileNotFound",
    "PermissionError"), it will print an error message before exiting the
    script. If the error is recoverable, the function will return the
    errorposition and errortext to the errorhandler function.
    """
    errortype = error[0]
    errorposition = error[1]
    if errortype in ["Empty","NoData", "FileNotFound", "PermissionError"]:
        return [errortext[errortype]]
    elif errortype in ["Value"]:
        return errorposition, errortext[errortype]

def valerrormessage(errorlist):
    """Takes a list of lists. Each nested list contains string and an interger.
    It prints the string from the first list and the integer in each list.
    """
    errormessage = errorlist[0][1]
    errorposition = [erroritem[0] for erroritem in errorlist]
    return f"{errormessage}\n Error rows: {errorposition}"
