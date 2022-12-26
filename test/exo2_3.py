from Peer import *


"""
dht = dict()
peers = [1, 8, 14, 21, 32, 38, 42, 48, 51, 56]

for elm in peers:
    dht[elm] = Peer(elm, elm, elm, elm, [])

for elm in peers:
    dht[elm].update_finger(peers)
    print("La finger table de ", elm, " est : ", dht[elm].finger)

"""




dht = dict()
dht[0] = Peer(0,0, 0)
hash_list = [0]
taille = len(dht[0].finger)
min = 0
max = 0
for i in range(1, 1000):
    dht[i] = Peer(i, i, 0)
    hash_list.append(i)
    
for i in range(0, 1000):
    dht[i].refresh_finger()
    taille += len(dht[i].finger)
    if len(dht[min].finger) > len(dht[i].finger):
        min = i
    
    if len(dht[max].finger) < len(dht[i].finger):
        max = i

distMoy = 0
maxDist = 0

for i in range(1, 1000):
    res, dist, chemin = dht[42].lookup(i, dht)
    distMoy += dist 
    if maxDist < dist:
        maxDist = dist 

print("La taille moyenne des finger est ", taille/1000)
print("La taille min d'une finger est ", len(dht[min].finger))
print("La taille max d'une finger est ", len(dht[max].finger))
print("La distance moyenne est ", distMoy/1000, ' La distance max est ', maxDist)
                                                                                           