Customer Masker

# Summary
The Customer Masker application is designed to anonymise customer data. The application takes a .csv file with set columns and transforms the data so that it no longer identifies the customers on the list before writing the transformed data to a new .csv file. The application is built in Python3 using only built-in modules. The built-in csv module was not used.

# Installation
After downloading the Customer Masker.zip file. Extract the files contents to where you would like the application to be installed. The application will require Python3 and to be installed and added to PATH in order to run.

#Function

The application is designed to anonymise customer data by replacing all numbers in each column with the average value for the column and replacing all characters in each string value with "X" unless the characters are "@", "." or ",". The application then writes this information to a new file "masked_clients.csv", either creating a new file or overwriting an existing file by the same name. After it has completed this it will print a short analysis of the data from the Name and Billing columns into the console, showing the average, shortest and longest name length, follow by the average, smallest and largest billing. This output is shown below:

Name:    Avg. 12.75, Min. 9, Max. 20
Billing: Avg. 25100.07, Min. 12400.27, Max. 53000.0

# Use
Before running the application, copy your source file into the directory containing the application and rename it customers.csv. The application can only read .csv files. The data in the csv file requires the following columns in order: ID, Name, Email, Billing, Location. The ID and Billing columns can only contain numbers. If either the ID or the billing column contain something other than a number or are blank, the application will skip past that row and its data will not be reflected in the final output, although the remaining data will still run. Once the source file is present the application is ready to be run.

The application is run by using the command python main.py in the windows terminal while in the directory containing the application.

If the input file contained the below...

ID,	Name,	Email,	Billing,	Location
1,	John Smith,	johnsmith@mail.com,	15000,	New York
2,	Kelly Lawrence Gomez,	Kelly@your-mail.com,	20000,	Washington

...The below would be returned in the output file

ID	Name	Email	Billing	Location
1.5	XXXXXXXXXX	XXXXXXXXX@XXXX.XXX	17500	XXXXXXXX
1.5	XXXXXXXXXXXXXXXXXXXX	XXXXX@XXXXXXXXX.XXX	17500	XXXXXXXXXX

#Error messages
There are five error types which will stop the script from running or interfere with the results of the script. These errors are outlined in the table below:
____________________________________________________________________________
Error Name             | Result of error        |Cause of error            |
_______________________|________________________|__________________________|
ValueError             |The offending row will  |Anything but a number in  |
                       |be removed from the     |the ID or Billing column. |
                       |output.                 |                          |
_______________________|________________________|__________________________|
EmptyError             |The script exit without |The source file is empty. |
                       |outputting results.     |                          |
                       |                        |                          |
_______________________|________________________|__________________________|
FileNotFoundError      |The script exit without |The script cannot find    |
                       |outputting results.     |"customers.csv" in its    |
                       |                        |directory.                |
_______________________|________________________|__________________________|
PermissionError        |The script exit without |The output file           |
                       |outputting results.     |"masked_clients.csv" is   |
                       |                        |open.                     |
_______________________|________________________|__________________________|
NoDataError            |The script exit without |The source file contains  |
                       |outputting results.     |headers but no data.      |
                       |                        |                          |
_______________________|________________________|__________________________|

The error messages printed in the console are displayed below:

ValueError: One or more value errors were detected while masking your
 data. While the script has run successfully, the rows containing these errors
 have been excluded from the results! These errors were caused by an unexpected
 entry in either the ID or Billing columns of the input file. These columns can
 only contain numbers, they cannot contain text or be blank. If you have left
 the billing blank for a record because the billing is zero, please enter 0
 instead. Please find below which rows in the input file need to be
 addressed.

EmptyError: An empty error was detected while masking your data. This
 is caused when the source .csv file doesn't contain any data. Please check your
 source file and re-run the script

NoDataError: A no data error was detected while masking your data.
 This is cause by the source file containing headings but no data underneath
 them. Please check your source file and re-run the script

FileNotFoundError: A file not found error was detected while
 masking your data. This is caused when the source file cannot be located.
 Please ensure that the source file is in the same directory as this script and
 is named "customer.csv

PermissionError: A permission error was detected while
 masking your data. This is caused when you have the output file
 "masked_clients.csv" open while attempting to run the script. Please close the
 file and re-run the script again.

#Unexpected results
It is possible to trigger a value error even when the ID and billings columns only contain numbers. If you have two adjacent values in the csv, one begins with " and the second ends with " and then in addition to this you have accidentally added an addition column of data to the data row. A value error will trigger as the two adjacent values will be joined and your data will be misaligned. The fix for this is to ensure that you don't have data outside of the prescribed columns listed in the use section.

#Testing
The testing is run by using the command python tests.py in the windows terminal while in the directory containing the application.
