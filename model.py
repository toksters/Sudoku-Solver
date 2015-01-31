class check:

    ## Takes in coordinate of textbox (eg. "B4") and a dictionary of all of the
    ## values for each textbox with the coordinate being the key for each value
    def __init__(self, coordinate, dictionary):
        self.coordinate = coordinate
        self.rowKey = coordinate[0:1]
        self.rowKey1 = coordinate[0:1]
        self.rowKeyOrig = coordinate[0:1]
        self.columnKey = coordinate[1:2]
        self.columnKey1 = coordinate[1:2]
        self.columnKeyOrig = coordinate[1:2]
        self.dictionary = dictionary

    ## Checks row for any matching values and returns a list of possible values
    def checkRow(self):
        self.rowKey = self.rowKeyOrig
        self.columnKey = self.columnKeyOrig
        possibleVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        remainingColumns = 9 - int(self.columnKey) #How many boxes ahead
        for i in range(remainingColumns):
            self.columnKey = int(self.columnKey) + 1
            rowCoordinates = self.rowKeyOrig + str(self.columnKey)
            rowValue = self.dictionary[rowCoordinates]
            for j in range(len(possibleVal) - 1):
                if(int(possibleVal[j]) == int(rowValue)):
                    possibleVal.pop(j)
            if(int(self.dictionary[rowCoordinates]) == possibleVal[len(possibleVal) - 1]):
                possibleVal.pop()
        placeHold = 1
        for i in range(int(self.columnKeyOrig)):
            rowCoordinates = str(self.rowKeyOrig) + str(placeHold)
            placeHold += 1
            for j in range(len(possibleVal)-1):
                if int(possibleVal[j]) == int(self.dictionary[rowCoordinates]):
                   possibleVal.pop(j)
            if(int(self.dictionary[rowCoordinates]) == possibleVal[len(possibleVal) - 1]):
                possibleVal.pop()
        self.rowKey = self.rowKeyOrig
        self.columnKey = self.columnKeyOrig
        return possibleVal

    def checkColumn(self):
        self.rowKey1 = self.rowKeyOrig
        self.columnKey1 = self.columnKeyOrig
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        possibleVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        letterPos = 0
        for i in range(len(self.letters)):
            if(self.letters[i] == self.rowKey1):
                letterPos = i + 1
        remainingRows = 9 - letterPos
        for i in range(remainingRows):
            letterPos = letterPos + 1
            self.rowKey = self.letters[letterPos - 1]
            columnCoordinates = str(self.rowKey1) + str(self.columnKey1)
            columnValue = self.dictionary[columnCoordinates]
            for j in range(len(possibleVal) - 1):
                if(possibleVal[j] == int(columnValue)):
                    possibleVal.pop(j)
            if(int(self.dictionary[columnCoordinates]) == possibleVal[len(possibleVal) - 1]):
                possibleVal.pop()
        for i in range(letterPos):
            columnCoordinates = self.letters[i] + str(self.columnKey1)
            for j in range(len(possibleVal) - 1):
                if int(possibleVal[j]) == int(self.dictionary[columnCoordinates]):
                    possibleVal.pop(j)
            if(int(self.dictionary[columnCoordinates]) == possibleVal[len(possibleVal) - 1]):
                possibleVal.pop()
        self.rowKey1 = self.rowKeyOrig
        self.columnKey1 = self.columnKeyOrig
        return possibleVal

    def checkBox(self):
        possibleVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        box1 = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
        box2 = ["a4", "a5", "a6", "b4", "b5", "b6", "c4", "c5", "c6"]
        box3 = ["a7", "a8", "a9", "b7", "b8", "b9", "c7", "c8", "c9"]
        box4 = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]
        box5 = ["d4", "d5", "d6", "e4", "e5", "e6", "f4", "f5", "f6"]
        box6 = ["d7", "d8", "d9", "e7", "e8", "e9", "f7", "f8", "f9"]
        box7 = ["g1", "g2", "g3", "h1", "h2", "h3", "i1", "i2", "i3"]
        box8 = ["g4", "g5", "g6", "h4", "h5", "h6", "i4", "i5", "i6"]
        box9 = ["g7", "g8", "g9", "h7", "h8", "h9", "i7", "i8", "i9"]
        for i in range(9):
            if(self.coordinate == box1[i]):
                for j in range(len(box1)):
                    for k in range(len(possibleVal) - 1):
                        #print(self.dictionary[box1[j]],possibleVal[k])
                        if(int(self.dictionary[box1[j]]) == int(possibleVal[k])):
                            #print("hi")
                            del possibleVal[k]
                        if(self.dictionary[box1[j]] == possibleVal[len(possibleVal) - 1]):
                            print("hi")
                            del possibleVal[len(possibleVal)-1]
                    #print("pos:",possibleVal)
            if(self.coordinate == box2[i]):
                for j in range(len(box2)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box2[j]]) == int(possibleVal[k])):
                            del possibleVal[k]
                        if(self.dictionary[box2[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box3[i]):
                for j in range(len(box3)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box3[j]]) == int(possibleVal[k])):
                            del possibleVal[k]
                        if(self.dictionary[box3[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box4[i]):
                for j in range(len(box4)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box4[j]]) == int(possibleVal[k])):
                            del possibleVal[k]
                        if(self.dictionary[box4[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box5[i]):
                for j in range(len(box5)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box5[j]]) == int(possibleVal[k])):
                            possibleVal.pop(k)
                        if(self.dictionary[box5[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box6[i]):
                for j in range(len(box6)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box6[j]]) == int(possibleVal[k])):
                            possibleVal.pop(k)
                        if(self.dictionary[box6[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box7[i]):
                for j in range(len(box7)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box7[j]]) == int(possibleVal[k])):
                            possibleVal.pop(k)
                        if(self.dictionary[box7[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box8[i]):
                for j in range(len(box1)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box8[j]]) == int(possibleVal[k])):
                            possibleVal.pop(k)
                        if(self.dictionary[box8[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
            if(self.coordinate == box9[i]):
                for j in range(len(box9)):
                    for k in range(len(possibleVal) - 1):
                        if(int(self.dictionary[box9[j]]) == int(possibleVal[k])):
                            possibleVal.pop(k)
                        if(self.dictionary[box9[j]] == possibleVal[len(possibleVal) - 1]):
                            possibleVal.pop()
        return possibleVal
          

    def finalCheck(self):
        rows = self.checkRow()
        columns = self.checkColumn()
        boxes = self.checkBox()
        allpossible = rows + columns + boxes
        repeats = []
        nums = []
        left = []
        singreps = []
        #rows = [2,4,6,3]
        #columns = [3,4,5,6,7]
        #boxes = [2,3,7]
        allpossible = rows + columns + boxes
        repeats = []
        nums = []
        left = []
        singreps = []

        for j in range(len(allpossible)):
            if(allpossible[j] in nums):
                repeats.append(allpossible[j])
            else:
                nums.append(allpossible[j])

#print(repeats)
#print(nums)

        for i in range(len(repeats)):
            if(repeats[i] in singreps):
                left.append(repeats[i])
            else:
                singreps.append(repeats[i])

#print(singreps)
        #print("left",left)
        return left
        
