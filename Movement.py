def move_forward(marty):
    if(marty):
        print("Marty is well connected")
        marty.walk(2,'auto',0,25,1500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def move_left(marty):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("left",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_right(marty):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("right",1,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0


def move_backward(marty):
    if(marty):
        print("Marty is well connected")
        marty.walk(2,'auto',0,-25,1500) # Walk still work the same way , but negative distance make it walk backward 
    else:
        print("Marty is sadely not connected")
        return 0
    return 0


def move_dance(marty):
    if(marty):
        print("Marty is well connected")
        marty.dance()
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_celebrate(marty):
    if(marty):
        print("Marty is well connected")
        marty.celebrate()
    else:
        print("Marty is sadely not connected")
        return 0
    

def move_kickL(marty):
    if(marty):
        print("Marty is well connected")
        marty.kick(str = 'left')
    else:
        print("Marty is sadely not connected")
        return 0
    


def move_kickR(marty):
    if(marty):
        print("Marty is well connected")
        marty.kick(str = 'right')
    else:
        print("Marty is sadely not connected")
        return 0

def lire_fichier(path):
    with open(path, 'r') as f:
        lignes = [line.strip() for line in f.readlines()]
    taille_grille = int(lignes[0].split()[1])
    coordonnees = [(int(pos[0]), int(pos[1])) for pos in lignes[1:]]
    return taille_grille, coordonnees

def chemin_fct(depart, arrivee):
    chemin = []
    x1, y1 = depart
    x2, y2 = arrivee

    pas_x = 1 if x2 > x1 else -1
    for x in range(x1, x2, pas_x):
        chemin.append((x + pas_x, y1))

    pas_y = 1 if y2 > y1 else -1
    for y in range(y1, y2, pas_y):
        chemin.append((x2, y + pas_y))

    return chemin
