from math import pow, log
import hashlib 

class Peer :
    nbMax = pow(2, 128)
    def __init__(self, id, hash, pred, suc, finger) :
        self.id = id 
        self.hash = hash 
        self.pred = pred
        self.suc = suc
        self.finger = finger 


    def successor(self, key, hash_list):
        #Si la clé dépasse l'espace des clés 
        if(key > self.nbMax):
            key = key%self.nbMax

        #Parcours la liste des paires pour savoir ou se situe la clè k
        for i in range(0,len(hash_list)-1):
            if key >= hash_list[i] and key < hash_list[i+1]: #Si la clé k est entre l'élement i et i+1 alors returner l'élement i+1
                return hash_list[i+1]
        return hash_list[0] # si on est la alors la clé et entre le dernier élement et le premier 

    
    def update_finger(self, hash_list): 
        
        m = int(log(self.nbMax)/log(2)) #m= nombre de bits de la clé max
        k = self.hash
        self.finger = [] #initialiser la table finger
       
        for i in range(0,m): #ne pas dépasser 2^m (le dèrnière clé passible dans m = 6)
            #Si la clé n'est pas déjà ajoutée et k n'est pas dans sa propre table
            if self.successor( ((k+pow(2,i))%self.nbMax), hash_list) not in self.finger and k != self.successor( ((k+pow(2,i))%self.nbMax), hash_list): 
                self.finger.append(self.successor((k+pow(2,i))%self.nbMax, hash_list)) #ajouter le successeur de la clé (k + 2^j)

    def give_neighbors(self):
        hash_list = [self.hash]
        if self.pred not in hash_list:
            hash_list.append(self.pred)

        if self.suc not in hash_list:
            hash_list.append(self.suc) 
        for elm in self.finger:
            if elm not in hash_list:
                hash_list.append(elm)
        return hash_list

    def refresh_finger():
        return "To do"

    def isincharge(key):
        return "we have"

    def lookup(key, dht):
        return "we have"

    def table():
        return "Table"
