#!usr/bin/env python3
"""
This is the inheritance part of the tutorial
and some keyword like instance of and many more
"""

"""
WARDROBE
@VERSION 3
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

    def __str__(self):
        return '[' + 'Name of clothing : ' + self.name + ', ' + 'Is  the clothing clean : ' + str(self.clean) + ', ' \
               + 'No of times worn : ' + str(self.time_worn) + ', ' + 'Max number of wears allowed :' + str(
            self.maxWears) + ']'


# This statment while the keyword class declaration means that the class Shirt inherits from the
# class Clothing
class Shirt(Clothing):
    def __init__(self, name, clean=True, no_of_times_worn=0, max_wears=1, full_sleeve=False):
        super().__init__(name, clean, no_of_times_worn, max_wears)
        self.fullSleeve = full_sleeve

    def hasFullSleeve(self):
        return self.fullSleeve

    def __str__(self):
        return '[' + super().__str__() + ', ' + 'Is Full sleeve : ' + str(self.fullSleeve) + ']'


def main():
    print('Wardrobe')
    myClothes = [Clothing('Black jeans', False), Clothing('Gap cap', True, 20, 1000), Clothing('Hoody', True, 30, 40),
                 Shirt('White shirt', True, 0, 1), Shirt('Black shirt', False, 1, 1, True)]

    print('\n\n===================Full Wardrobe===================\n')
    for i in range(len(myClothes)):
        print(myClothes[i])
    print('\n===================Clean Clothes===================\n')
    for i in range(len(myClothes)):
        if myClothes[i].isClean():
            print(myClothes[i])
    print('\n===================Shirts===================\n')
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            print(myClothes[i])
    print('\n===================Clean Shirt===================\n')
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if myClothes[i].isClean():
                print(myClothes[i])
    print('\n===================Dirty Shirt===================\n')
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if not myClothes[i].isClean():
                print(myClothes[i])
    print('\n===================Full Sleeve====================\n')
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if myClothes[i].hasFullSleeve():
                print(myClothes[i])
    print('\n===================Half Sleeve====================\n')
    for i in range(len(myClothes)):
        if isinstance(myClothes[i], Shirt):
            if not myClothes[i].hasFullSleeve():
                print(myClothes[i])


if __name__ == '__main__':
    main()
