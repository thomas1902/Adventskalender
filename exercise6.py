def tuningTrouble():
    with open('exercise6input') as f:
        ausgabe = f.readlines()
        liste = []
        counter = -1
        differentChars = 0
        index = 0
        unicatelist = []

        for sentence in ausgabe:
            for character in sentence:
                counter +=1
                liste.append(character)
                if len(liste) == 5:
                    samecounterListe = []
                    TrueList = []
                    for element in liste[0:-1]:
                        samecounter = 0
                        for secondelement in liste[0:-1]:
                            if element == secondelement:
                                samecounter = samecounter + 1
                        samecounterListe.append(samecounter)
                    for number in samecounterListe:
                        if number == 1:
                            TrueList.append(True)
                        else : TrueList.append(False)
                    if False not in TrueList:
                        print(counter)
                        break
                    del (liste[0])

def tuningTroublePartTwo():
    with open('exercise6input2') as f:
        ausgabe = f.readlines()
        liste = []
        counter = -1
        differentChars = 0
        index = 0
        unicatelist = []

        for sentence in ausgabe:
            for character in sentence:
                counter += 1
                liste.append(character)
                if len(liste) == 15:
                    samecounterListe = []
                    TrueList = []
                    for element in liste[0:-1]:
                        samecounter = 0
                        for secondelement in liste[0:-1]:
                            if element == secondelement:
                                samecounter = samecounter + 1
                        samecounterListe.append(samecounter)
                    for number in samecounterListe:
                        if number == 1:
                            TrueList.append(True)
                        else:
                            TrueList.append(False)
                    if False not in TrueList:
                        print(counter)
                        break
                    del (liste[0])


tuningTrouble()
tuningTroublePartTwo()