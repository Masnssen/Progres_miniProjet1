import wikipedia
import hashlib
def getListeMot():
    f = open("name_site", "r")
    content = f.read()
    f.close()

    listeTitre = content.split(',')
    listeMot = []
    for elm in listeTitre:
        mots = elm.split(' ')
        for mot in mots:
            if mot not in listeMot:
                listeMot.append(mot)


    phrase = listeMot
    listeMot = []
    for elm in phrase:
        mots = elm.split('-')
        for mot in mots:
            if mot not in listeMot:
                listeMot.append(mot)
    
    return listeMot

hexa1 = hashlib.sha1("1".encode()).hexdigest()
hexa2 = hashlib.sha1("Computer science".encode()).hexdigest()
print(int(hexa1, base = 16))
print(int(hexa2, base = 16))


