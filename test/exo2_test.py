from Peer import *
import hashlib


def hash(key):
    return int(hashlib.sha1(str(key).encode()).hexdigest(), base = 16)

dht = dict()
dht[hash(0)] = Peer(0,dht, 0)
taille = len(dht[hash(0)].finger)
min = hash(0)
max = hash(0)
for i in range(1, 1000):
    dht[hash(i)] = Peer(i, dht, 0)
    taille += len(dht[hash(i)].finger)
    if len(dht[min].finger) > len(dht[hash(i)].finger):
        min = hash(i)
    
    if len(dht[max].finger) < len(dht[hash(i)].finger):
        max = hash(i)


print("La taille moyenne des finger est ", taille/1000)
print("La taille min d'une finger est ", len(dht[min].finger))
print("La taille max d'une finger est ", len(dht[max].finger))

                                                                                           