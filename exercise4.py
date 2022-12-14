def findNumbersContainsInOther():
    with open('exercise4input') as f:
        ausgabe = f.readlines()
        counter = 0
        for item in ausgabe:
            firstNumberSplit = item.split('-')
            number1 = int(firstNumberSplit[0])
            secondNumberSplit = firstNumberSplit[1].split(',')
            number2 = int(secondNumberSplit[0])
            number3 = int(secondNumberSplit[1])
            number4 = int(firstNumberSplit[2])
            if (number1<= number3 and number2>= number4) or number1>= number3 and number2<= number4:
                counter = counter+1
    print('solution exercise 4.1:',counter)

findNumbersContainsInOther()

def findNumbersContainsInOther2():
    with open('exercise4input') as f:
        ausgabe = f.readlines()
        counter = 0
        for item in ausgabe:
            firstNumberSplit = item.split('-')
            number1 = int(firstNumberSplit[0])
            secondNumberSplit = firstNumberSplit[1].split(',')
            number2 = int(secondNumberSplit[0])
            number3 = int(secondNumberSplit[1])
            number4 = int(firstNumberSplit[2])
            Bereich1 = list(range(number1,number2+1))
            Bereich2 = list(range(number3, number4+1))
            for numberBereich1 in Bereich1:
                if numberBereich1 in Bereich2:
                    counter +=1
                    break
        print('solution exercise 4.2:',counter)
findNumbersContainsInOther2()



