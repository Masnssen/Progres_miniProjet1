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


nbElm = 1000

dht = dict()
dht[hash(0)] = Peer(0, dht, 0)



for i in range(1, nbElm):
    dht[hash(i)] = Peer(i, dht, 0)

for titre in listeTitre:
    dht[hash(0)].publish_page(titre, dht)


result = dht[hash(0)].search("vector column", dht)
print(result)

result = dht[hash(0)].search("2d ", dht)
print(result)

result = dht[hash(0)].search("2d geometric", dht)
print(result)

result = dht[hash(0)].search("model", dht)
print(result)

result = dht[hash(0)].search("model geometry vector", dht)
print(result)

result = dht[hash(0)].search("footbal france paris", dht)
print(result)
