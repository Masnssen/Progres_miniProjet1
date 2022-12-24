from Peer import *

p = Peer(1, 1, 1, 1, [])
p.update_finger([1, 8, 14, 18])

print(p.give_neighbors())