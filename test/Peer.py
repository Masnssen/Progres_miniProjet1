from math import pow, log
import hashlib 

class Peer :
    nbMax = pow(2, 128)
    listePeers = dict()
    def __init__(self, id, hash, pred, suc, finger):

        self.id = id 
        self.hash = hash 
        self.pred = pred                                       
        self.suc = suc 
        self.finger = finger 
        self.listePeers[hash] = self 


    def successor(self, key, hash_list):
        #Si la clé dépasse l'espace des clés 
        if(key > self.nbMax):
            key = key%self.nbMax

        #Parcours la liste des paires pour savoir ou se situe la clè k
        for i in range(0,len(hash_list)-1):
            if key >= hash_list[i] and key < hash_list[i+1]: #Si la clé k est entre l'élement i et i+1 alors returner l'élement i+1
                return hash_list[i+1]
        return hash_list[0] # si on est la alors la clé et entre le dernier élement et le premier 

    def predecessor(self, key, hash_list):
        #Si la clé dépasse l'espace des clés autorisé ou elle est négatif ou null alors ne rien retourner
        if(key > self.nbMax):
            key = key % self.nbMax
        #Parcours la liste des paires pour savoir ou se situe la clè k
        for  i in range(0,len(hash_list)-1):
            if key > hash_list[i] and key <= hash_list[i+1]: #Si la clé k est entre l'élement i et i+1 alors returner l'élement i
                return hash_list[i]
        return hash_list[len(hash_list)-1] # si on est la alors la clé et entre le dernier élement et le premier alors returner le dernier élement

    def update_finger(self, hash_list): 
        ###Mettre a jour le successor de la clè 
        self.suc = self.successor(self.hash, hash_list)
        self.pred = self.predecessor(self.hash, hash_list)

        m = int(log(self.nbMax)/log(2)) #m= nombre de bits de la clé max
        k = self.hash
        self.finger = [] #initialiser la table finger
       
        for i in range(0,m): #ne pas dépasser 2^m (la dèrnière clé passible dans m)
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
        print(self.listePeers[self.suc].id)
        print(self.listePeers[self.pred].id)
        return self.listePeers[self.suc]  

    def isincharge(key):
        return "we have"

    def lookup(key, dht):
        return "we have"

    def table():
        return "Table"

    def publish_page(self, page_title, dht):
        return 'To do'
    
    def retrieve_page(self, page_title):
        return "To do"
    
    def search(self, search_string, dht):
        return "To do"
    

