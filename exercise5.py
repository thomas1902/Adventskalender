import re
def supplyStacks():
    with open('exercise5input') as f:
        ausgabe = f.readlines()
        liste1 = []
        liste2 = []
        liste3 = []
        liste4 = []
        liste5 = []
        liste6 = []
        liste7 = []
        liste8 = []
        liste9 = []
        for item in ausgabe:
            if ']' in item:
                item = item.replace('\n', '').replace(']', ' ').replace('[', ' ')
                liste1.append(item[1])
                liste2.append(item[5])
                liste3.append(item[9])
                liste4.append(item[13])
                liste5.append(item[17])
                liste6.append(item[21])
                liste7.append(item[25])
                liste8.append(item[29])
                liste9.append(item[33])
                dictonary = {
                    1:liste1,
                    2:liste2,
                    3:liste3,
                    4:liste4,
                    5:liste5,
                    6:liste6,
                    7:liste7,
                    8:liste8,
                    9:liste9
                }
            if 'move' in item:
                listeZahl = list(map(int, re.findall(r'\d+', item)))
                currentList = (dictonary[listeZahl[1]])
                newCurrentList = []
                for i in currentList:
                    if i != ' ':
                        newCurrentList.append(i)
                secondList = (dictonary[listeZahl[2]])
                newSecondList = []
                for i in secondList:
                    if i != ' ':
                        newSecondList.append(i)
                dictonary[listeZahl[1]] = newCurrentList
                insert = newCurrentList[0:listeZahl[0]]
                for word in insert:
                    newSecondList.insert(0,word)
                    newCurrentList.remove(word)
                dictonary[listeZahl[2]] = newSecondList
                dictonary[listeZahl[1]] = newCurrentList
    print('sulution exercise5.1:', dictonary)
supplyStacks()

def supplyStacks2():
    with open('exercise5input') as f:
        ausgabe = f.readlines()
        liste1 = []
        liste2 = []
        liste3 = []
        liste4 = []
        liste5 = []
        liste6 = []
        liste7 = []
        liste8 = []
        liste9 = []
        for item in ausgabe:
            if ']' in item:
                item = item.replace('\n', '').replace(']', ' ').replace('[', ' ')
                liste1.append(item[1])
                liste2.append(item[5])
                liste3.append(item[9])
                liste4.append(item[13])
                liste5.append(item[17])
                liste6.append(item[21])
                liste7.append(item[25])
                liste8.append(item[29])
                liste9.append(item[33])
                dictonary = {
                    1:liste1,
                    2:liste2,
                    3:liste3,
                    4:liste4,
                    5:liste5,
                    6:liste6,
                    7:liste7,
                    8:liste8,
                    9:liste9
                }
            if 'move' in item:
                listeZahl = list(map(int, re.findall(r'\d+', item)))
                currentList = (dictonary[listeZahl[1]])
                newCurrentList = []
                for i in currentList:
                    if i != ' ':
                        newCurrentList.append(i)
                secondList = (dictonary[listeZahl[2]])
                newSecondList = []
                for i in secondList:
                    if i != ' ':
                        newSecondList.append(i)
                dictonary[listeZahl[1]] = newCurrentList
                insert = newCurrentList[0:listeZahl[0]]
                insert.reverse()
                for word in insert:
                    newSecondList.insert(0,word)
                    newCurrentList.remove(word)
                dictonary[listeZahl[2]] = newSecondList
                dictonary[listeZahl[1]] = newCurrentList
    print('sulution exercise5.2:',dictonary)
supplyStacks2()