from Peer import *
import hashlib
import wikipedia

from Peer import *
import hashlib

def getListeTitre():
    f = open("name_site", "r")
    content = f.read()
    f.close()

    listeTitre = content.split(",")
    return listeTitre


listeTitre = getListeTitre()
def hash(key):
    return int(hashlib.sha1(str(key).encode()).hexdigest(), base = 16)


nbElm = 100

dht = dict()
dht[hash(0)] = Peer(0, dht, 0)



for i in range(1, nbElm):
    dht[hash(i)] = Peer(i, dht, 0)

for titre in listeTitre:
    dht[hash(0)].publish_page(titre, dht)

titreRes = dict()
for i in range(0, 2000):
    res, dist = dht[hash(42)].lookup(listeTitre[i], dht)
    contenu = dht[res].retrieve_page(listeTitre[i])
    if res in titreRes:
        titreRes[res] += 1
    else:
        titreRes[res] = 1
    print(i)

maxIndex = 0
cleMax = 0

for key, value in titreRes.items():
    if maxIndex < value:
        maxIndex = value
        cleMax = key

print("Le plus grand nombre d'article indexer par un pair est : ", maxIndex)