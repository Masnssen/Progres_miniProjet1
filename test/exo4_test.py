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


nbElm = 10

dht = dict()
dht[hash(0)] = Peer(0, dht, 0)



for i in range(1, nbElm):
    dht[hash(i)] = Peer(i, dht, 0)

for titre in listeTitre:
    dht[hash(0)].publish_page(titre, dht)

result = dht[hash(0)].search("vector column", dht)
print(result)
"""

print("Le nombre de titre est : ", len(listeTitre))
for elm in listeTitre:
    dht[hash(0)].publish_page(elm, dht)

print(dht[hash(0)].retrieve_page(listeTitre[3]))
"""