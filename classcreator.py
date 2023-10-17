"""
Creates the Customers() object based on input values from a dictionary input.
The Customers object has three functions attached .masktext(self), which takes
the values of designated class attributes comprised of lists of strings and
replaces all of the characters in the string that aren't @., with X. The second
function takes the values of designated class attributes comprised of lists of
numbers and returns the average of the numbers in each list. The third function
prins the average, smallest and largest Name length, followed bu the average
smallest and largest billing.

"""

import re
# pylint: disable=no-member

class Customers():
    """Used to represent an array of customers. Class attribute names
are set by the keys from the dictionary input. Class attribute values are set
by the value attached to each respective key.

    """
    def __init__ (self, **dict_input):
        for key, value in dict_input.items():
            setattr(self, key, value)

    def masktext(self):
        """Takes in a list of strings from the class attributes and returns the
        lists with all characters other than @., with X.

        """
        #For each string in the list, substitutes characters with X unless the characeter is "@", "." or ",".
        masknames = [re.sub(r'[^@,.]', r"X", name) for name in self.names]
        maskemails = [re.sub(r'[^@,.]', r"X", email) for email in self.emails]
        masklocations = [re.sub(r'[^@,.]', r"X", location) for location in
        self.locations]
        return masknames, maskemails, masklocations

    def masknum(self):
        """Takes in a list of numbers from the class attributes and returns the
        average of all the numbers in the list.

        """
        maskid = sum(self.ids)/len(self.ids)
        maskbilling = sum(self.billings)/len(self.billings)
        return maskid, maskbilling

    def reportwriter(self):
        """Takes in the attribute values of the class. For the name attribute it
        calculates the longest, shortest and average length of the name strings.
        for the billings attribute it calculates the highest, lowest and average
        value of the billings floats, both averages are displayed at two decimal
        places. Once calculated, it populates an f-strings with the calculation
        result and returns it.

        """
        avenamelen = sum(map(len, self.names))/len(self.names)
        minnamelen = len(min(self.names, key=len))
        maxnamelen = len(max(self.names, key=len))
        avebilling = sum(self.billings)/len(self.billings)
        minbilling = min(self.billings)
        maxbilling = max(self.billings)
        return f"""
Name:    Avg. {avenamelen:.2f}, Min. {minnamelen}, Max. {maxnamelen}
Billing: Avg. {avebilling:.2f}, Min. {minbilling}, Max. {maxbilling}
"""
