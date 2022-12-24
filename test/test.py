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
dht[0] = Peer(0,0)
hash_list = [0]
for i in range(1, 99):
    dht[i] = Peer(i, i)
    hash_list.append(i)



for i in range(0, 99):
    #dht[i].update_finger(hash_list)
    print("La finger table de ", i, " est : ", dht[i].finger)
