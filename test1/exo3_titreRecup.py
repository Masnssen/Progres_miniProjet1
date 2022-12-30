import hashlib
import wikipedia

listeTitre = [] #La liste des titres 
pageInitial = "Computer science"
#Recupèrer la page initiale
page_initial = wikipedia.page(pageInitial)
listeTitre.append(pageInitial)

#Récupèrer la liste des titres des link de la page initiale 
listeLinks = page_initial.links
for elm in listeLinks:
    if elm not in listeTitre:
        listeTitre.append(elm)

#Les titres de deuxieme degrer 
i = 1
taille = len(listeTitre)
print("La taille de la liste est ", taille)
while i < 5:
    try:
        page = wikipedia.page(listeTitre[i])
    except wikipedia.exceptions.PageError:
        i += 1
        continue
    listeLinks = page.links

    for elm in listeLinks:
        if elm not in listeTitre:
            listeTitre.append(elm)
    
    i += 1
    print(i)


listeTitre = ','.join(listeTitre)
file = open("name_site", "w")
file.write(listeTitre)
file.close()
