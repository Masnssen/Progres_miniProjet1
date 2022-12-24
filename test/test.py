from Peer import *

p1 = Peer(1, 1, 1, 1, [])
p2 = Peer(8, 8, 8, 8, [])
p3 = Peer(14, 14, 14, 14, [])
p4 = Peer(18, 18, 18, 18, [])

p1.update_finger([1, 8, 14, 18])
p1.refresh_finger()