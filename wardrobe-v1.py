#!usr/bin/env python3
"""
WARDROBE
@VERSION 1
@author Rehan Kodekar
@DATE 2017-04-21
"""


class Clothing(object):
    """
    The clothing class defines a name of the clothing and 
    quality in terms of cleanliness
    """

    def __init__(self, name, clean=True):
        self.name = name
        self.clean = clean

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean

    def setName(self, newName):
        self.name = newName

    def setClean(self, changeClean):
        self.clean = changeClean

    def __str__(self) -> str:
        return '[' + self.name + ', ' + str(self.clean) + ']'


def main():
    print('Wardrobe')
    myJeans = Clothing('Black jeans', False)
    myShirt = Clothing('White shirt', True)
    print(myJeans.getName())
    print(myShirt.isClean())
    print(myJeans)


if __name__ == '__main__':
    main()
