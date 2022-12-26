from Peer import *

"""

dht = dict()
peers = [1, 8, 14, 21, 32, 38, 42, 48, 51, 56]

for elm in peers:
    dht[elm] = Peer(elm, elm)

for elm in peers:
    dht[elm].update_finger(peers)
    print("La finger table de ", elm, " est : ", dht[elm].finger)



#Teste lookup 
print("Le chemin vers 21", dht[8].lookup(54, dht))

"""

dht = dict()
dht[0] = Peer(0, 0, 0)
hash_list = [0]


for i in range(1, 1000):
    dht[i] = Peer(i, i, 0)
    hash_list.append(i)

distMoy = 0
maxDist = 0
for i in range(0, 1000):
    res, dist, chemin = dht[42].lookup(i, dht)
    distMoy += dist 
    if maxDist < dist:
        maxDist = dist 
    
print("La distance moyenne est ", distMoy/1000, ' La distance max est ', maxDist)
"""

taille = 0
for i in range(0, 999):
    dht[i].update_finger(hash_list)
    taille += len(dht[i].finger)

print("La taille moyenne des finger est ", taille/10000)       
"""                                                                                     