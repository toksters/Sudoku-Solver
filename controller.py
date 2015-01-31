import model

class controller:
    def __init__(self,coordinate,dictionary):
        self.values = model.check(coordinate,dictionary)
        self.coordinate = coordinate
        self.dictionary = dictionary

    def getCommon(self):
        self.common = self.values.finalCheck()
        return self.common
