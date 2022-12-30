from Peer import *
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

def getListeTitre():
    f = open("name_site", "r")
    content = f.read()
    f.close()

    listeTitre = content.split(",")
    return listeTitre


listeTitre = getListeTitre()

def hash(key):
    return int(hashlib.sha1(str(key).encode()).hexdigest(), base = 16)


nbElm = 1000

dht = dict()
dht[hash(0)] = Peer(0, dht, 0)



for i in range(1, nbElm):
    dht[hash(i)] = Peer(i, dht, 0)
    

print("Le nombre de titre est : ", len(listeTitre))
for elm in listeTitre:
    dht[hash(0)].publish_page(elm, dht)

nbMot = 0
maxMot = 0
for key in dht.keys():
    taille = len(dht[key].table.keys())
    nbMot += taille
    if maxMot < taille:
        maxMot = taille

print("Le nombre de mot indexer est ", nbMot)
print("La taille moyenne de la table est : ",nbMot/nbElm)
print("La taille max est : ", maxMot)



