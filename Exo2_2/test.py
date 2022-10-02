import json
listeUri = {
    "URI_1" : { 
        "10.10.0.1": [True, 0] , 
        "10.10.0.1": [True, 0]
    },
    "URI_2" : { 
        "10.10.0.1": [True, 0] , 
        "10.10.0.1": [True, 0]
    }
}


objetPython = json.dumps(listeUri)

ref = json.loads(objetPython)

print(ref)

