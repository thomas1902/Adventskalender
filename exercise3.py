import string
def ruckSackSuche():
    with open("C:/Users/thoma/OneDrive/Dokumente/Allgemein/Adventskalender_Tag3.txt") as f:
        Alphabet = list(string.ascii_letters)
        ausgabe = f.readlines()
        counter = 0
        for item in ausgabe:
            item = item.replace('\n','')
            length = len(item)
            firstitem = item[0:int(length/2)]
            seconditem = item[int(length/2):length]
            for letter in firstitem:
                if letter in seconditem:
                    for word in Alphabet:
                        if letter == word:
                            counter = counter+Alphabet.index(word)+1
                    break
        print(counter)

def prioritySearch():
    with open("C:/Users/thoma/OneDrive/Dokumente/Allgemein/Adventskalender_Tag3.txt") as f:
        Alphabet = list(string.ascii_letters)
        ausgabe = f.readlines()
        counter = 0
        liste = []
        for item in ausgabe:
            item = item.replace('\n','')
            liste.append(item)

        newList = []
        for word in liste:
            newList.append(word)
            if (liste.index(word)+1)%3 == 0:
                newList.append('\n')
        temporaryList = []
        for newWord in newList:
            if newWord == '\n':
                for letter in Alphabet:
                    if letter in temporaryList[0] and letter in temporaryList[1] and letter in temporaryList[2]:
                        counter += Alphabet.index(letter)+1
                temporaryList = []
                continue
            if newWord != '\n':
                temporaryList.append(newWord)
        print(counter)














prioritySearch()