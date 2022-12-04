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
            list.append(item)


prioritySearch()