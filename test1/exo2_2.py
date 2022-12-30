from Peer import *
import hashlib

def hash(key):
    #return int(hashlib.sha1(str(key).encode()).hexdigest(), base = 16)
    return key


dht = dict()
dht[hash(0)] = Peer(0, dht, 0)


for i in range(1, 100):
    dht[hash(i)] = Peer(i, dht, 0)
    

distMoy = 0
maxDist = 0

for i in range(0, 100):
    res, dist, chemin = dht[hash(42)].lookup(i, dht)
    print(res)
    distMoy += dist 
    if maxDist < dist:
        maxDist = dist 
    
print("La distance moyenne est ", distMoy/100, ' La distance max est ', maxDist)
"""

taille = 0
for i in range(0, 999):
    dht[i].update_finger(hash_list)
    taille += len(dht[i].finger)

print("La taille moyenne des finger est ", taille/10000)       
"""                                                                                     