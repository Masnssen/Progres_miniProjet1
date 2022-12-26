from math import pow, log
import hashlib 

class Peer :
    m = 128
    nbMax = 1000
    listePeers = dict()

    def __init__(self, id, hash, entrie):

        self.id = id 
        self.hash = hash
        self.finger = [] 
        if( entrie not in list(self.listePeers.keys())):
            entrie = 0
        if len(list(self.listePeers.keys())) != 0:
            self.pred = self.listePeers[entrie].arrivale(hash)
            self.suc = self.successor(hash, list(self.listePeers.keys())) 
            self.update_finger(list(self.listePeers.keys()))
        else:
            self.pred = hash
            self.suc = hash
        
        self.listePeers[hash] = self
        self.listePeers[self.suc].pred = hash


    def arrivale(self, key):
        pred = self.predecessor(key, list(self.listePeers.keys()))
        self.listePeers[pred].suc = key
        return pred


    def successor(self, key, hash_list):
         #Si y'a aucun element dans hash_list
        if len(hash_list) == 0:
            return key
            
        #Si la clé dépasse l'espace des clés 
        if(key > self.nbMax):
            key = key%self.nbMax

        #Parcours la liste des paires pour savoir ou se situe la clè k
        for i in range(0,len(hash_list)-1):
            if key >= hash_list[i] and key < hash_list[i+1]: #Si la clé k est entre l'élement i et i+1 alors returner l'élement i+1
                return hash_list[i+1]
        return hash_list[0] # si on est la alors la clé et entre le dernier élement et le premier 

    def predecessor(self, key, hash_list):
        #Si y'a aucun element dans hash_list
        if len(hash_list) == 0:
            return key
        #Si la clé dépasse l'espace des clés autorisé ou elle est négatif ou null alors ne rien retourner
        if(key > self.nbMax):
            key = key % self.nbMax
        #Parcours la liste des paires pour savoir ou se situe la clè k
        for i in range(0,len(hash_list)-1):
            if key > hash_list[i] and key <= hash_list[i+1]: #Si la clé k est entre l'élement i et i+1 alors returner l'élement i
                return hash_list[i]
        return hash_list[len(hash_list)-1] # si on est la alors la clé et entre le dernier élement et le premier alors returner le dernier élement

    def update_finger(self, hash_list): 
       
        ###Mettre a jour le successor de la clè 
        #self.suc = self.successor(self.hash, hash_list)
        #self.pred = self.predecessor(self.hash, hash_list)

        m = int(log(self.nbMax)/log(2)) #m= nombre de bits de la clé max
        k = self.hash
        self.finger = [] #initialiser la table finger
       
        for i in range(0,m): #ne pas dépasser 2^m (la dèrnière clé possible dans m)
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

    def refresh_finger(self):
        hash_table = [] 
        peerSuc = self.listePeers[self.suc]
        peerPred = self.listePeers[self.pred]
        
        while peerSuc != peerPred:
            hash_table.append(peerSuc.hash)
            hash_table.append(peerPred.hash)
            peerSuc = self.listePeers[peerSuc.suc]
            peerPred = self.listePeers[peerPred.pred]
        
        if peerSuc.hash not in hash_table:
            hash_table.append(peerSuc.hash)
            
        self.update_finger(hash_table)
        return hash_table

    def isincharge(self, key):
        if key >= self.pred and key < self.hash:
            return True

        if self.hash < self.pred and key >= self.pred: #On est à la fin (ou y a la boucle)
            return True

        return False

    def lookup(self ,key, dht):
    
        #Ajouter le cas ou la cle de la fingerTable est supprimer de la dht    
        chemin = [self.hash] #Ajouter le noeud d'entrer à la liste des chemins
        nbSauts = 0
        if self.isincharge(key) or len(dht.keys()) == 1: #Si le premier pair est responsable de cle, le retourner directement
            return chemin.pop(), nbSauts, chemin
    
        nbSauts += 1
        actuel = self.hash 
        suiv = dht[actuel].suc
        distBest = -1
        

        while not dht[suiv].isincharge(key): #Si le next n'est pas en charge alors
            finger = dht[actuel].finger #Récupérer la finger table 
            best = -1
            if distBest == -1:
                best = 0
                #Calcul de la distance du premier élément de la finger table
                if finger[0] > key : #On regarde devant 
                    distBest = (self.nbMax % finger[0]) + key  
                else:
                    distBest = key - finger[0]
        
        
            #Chercher la distance minimale 
            i = 0
            while i < len(finger):
                if finger[i] > key :
                    dist = (self.nbMax % finger[i]) + key 
                else:
                    dist = key - finger[i]
            
                if dist < distBest :
                    distBest = dist
                    best = i
                i+=1
            
            
            if(best == -1):
                actuel = dht[actuel].suc
                if actuel > key :
                    distBest = (self.nbMax % actuel) + key 
                else:
                    distBest = key - actuel
            
                if dist < distBest :
                    distBest = dist
        
            else:
                actuel = finger[best]

            chemin.append(actuel)
            suiv = dht[actuel].suc
            nbSauts += 1
            
    
        #Ajouter la derniere key
        chemin.append(suiv)
        return suiv, nbSauts, chemin
    

    def table():
        return "Table"

    def publish_page(self, page_title, dht):
        return 'To do'
    
    def retrieve_page(self, page_title):
        return "To do"
    
    def search(self, search_string, dht):
        return "To do"
    

