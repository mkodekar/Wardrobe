#!usr/bin/env python3
"""
WARDROBE
@VERSION 2
@author Rehan Kodekar
@DATE 2017-04-23
"""


class Clothing(object):
    """
    The clothing class defines a name of the clothing and 
    quality in terms of cleanliness
    """

    def __init__(self, name, clean=True, no_of_times_worn=0, max_wears=1):
        self.name = name
        self.clean = clean
        self.time_worn = no_of_times_worn
        self.maxWears = max_wears

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean

    def setName(self, newName):
        self.name = newName

    def setClean(self, changeClean):
        self.clean = changeClean

    def wear(self):
        self.time_worn = +1
        if self.time_worn >= self.maxWears:
            self.clean = False

    def wash(self):
        self.clean = True
        self.time_worn = 0

    def __str__(self) -> str:
        return '[' + 'Name of clothing : ' + self.name + ', ' + 'Is  the clothing clean : ' + str(self.clean) + ', ' \
               + 'No of times worn : ' + str(self.time_worn) + ', ' + 'Max number of wears allowed :' + str(self.maxWears) + ']'


def main():
    print('Wardrobe')
    myJeans = Clothing('Black jeans', False)
    myShirt = Clothing('White shirt', True)
    myCap = Clothing('Gap cap', True, 20, 1000)
    mySweater = Clothing('Hoody', True, 30, 40)
    print(myJeans.getName())
    print(myShirt.isClean())
    print(myJeans)
    print(myCap)
    print(mySweater)
    # After i wear the jeans it bcomes dirty
    # lets make the string method print our more compact answer in dictionay format
    myJeans.wear()
    print(myJeans)
    myJeans.wash()
    print(myJeans)


if __name__ == '__main__':
    main()
