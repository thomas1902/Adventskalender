def searchHighestCalories():
    with open("C:/Users/thoma/OneDrive/Dokumente/Allgemein/Zahlen.txt") as f:
        lines = f.readlines()
        print(lines)
        liste = []
        TheSum = 0
        for number in lines:
            if number != '\n\n':
                if number == '\n':
                   TheSum = 0
                if number != '\n':
                    count = int(number)
                    TheSum += count
                    print('die summe:',TheSum)
                    liste.append(TheSum)
    liste.sort()
    print(liste)

searchHighestCalories()