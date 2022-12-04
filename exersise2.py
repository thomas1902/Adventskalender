def calculateTotalScore():
    with open("C:/Users/thoma/OneDrive/Dokumente/Allgemein/Adventskalender_Tag2.txt") as f:
        ausgabe = f.readlines()
        Score = 0
        print(ausgabe)
        for match in ausgabe:
            firstChar = match[0]
            secondChar = match[2]
            temporalScore = 0
            if(firstChar == 'A'):
                if(secondChar=='X'):
                    temporalScore = temporalScore+4
                elif(secondChar=='Y'):
                    temporalScore = temporalScore+8
                elif(secondChar=='Z'):
                    temporalScore=temporalScore+3

            if(firstChar == 'B'):
                if (secondChar == 'X'):
                    temporalScore = temporalScore + 1
                elif (secondChar == 'Y'):
                    temporalScore = temporalScore + 5
                elif (secondChar == 'Z'):
                    temporalScore = temporalScore + 9

            if (firstChar == 'C'):
                if (secondChar == 'X'):
                    temporalScore = temporalScore + 7
                elif (secondChar == 'Y'):
                    temporalScore = temporalScore + 2
                elif (secondChar == 'Z'):
                    temporalScore = temporalScore + 6

            Score += temporalScore

            print(firstChar,secondChar,temporalScore,Score)

def calculateTotalScorePrediction():
    with open("C:/Users/thoma/OneDrive/Dokumente/Allgemein/Adventskalender_Tag2.txt") as f:
        ausgabe = f.readlines()
        Score = 0
        for match in ausgabe:
            firstChar = match[0]
            secondChar = match[2]
            temporalScore = 0
            if(firstChar == 'A'):
                if(secondChar=='X'):
                    temporalScore = temporalScore+3
                elif(secondChar=='Y'):
                    temporalScore = temporalScore+4
                elif(secondChar=='Z'):
                    temporalScore=temporalScore+8

            if(firstChar == 'B'):
                if (secondChar == 'X'):
                    temporalScore = temporalScore + 1
                elif (secondChar == 'Y'):
                    temporalScore = temporalScore + 5
                elif (secondChar == 'Z'):
                    temporalScore = temporalScore + 9

            if (firstChar == 'C'):
                if (secondChar == 'X'):
                    temporalScore = temporalScore + 2
                elif (secondChar == 'Y'):
                    temporalScore = temporalScore + 6
                elif (secondChar == 'Z'):
                    temporalScore = temporalScore + 7

            Score += temporalScore

            print(firstChar,secondChar,temporalScore,Score)



calculateTotalScorePrediction()