def findNumbersContainsInOther():
    with open('exersise4') as f:
        ausgabe = f.readlines()
        counter = 0
        for item in ausgabe:
            firstNumberSplit = item.split('-')
            number1 = int(firstNumberSplit[0])
            secondNumberSplit = firstNumberSplit[1].split(',')
            number2 = int(secondNumberSplit[0])
            number3 = int(secondNumberSplit[1])
            number4 = int(firstNumberSplit[2])
            print(item)
            if (number1<= number3 and number2>= number4) or number1>= number3 and number2<= number4:
                print('STOOOOOOOOOOOOOOOOp')
                counter = counter+1
    print(counter)

findNumbersContainsInOther()
