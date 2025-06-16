def move_forward(marty, steps):
    if(marty):
        print("Marty is well connected")
        marty.walk(steps,'auto',0,25,1500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def move_left(marty, steps):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("left",steps,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0
    
def move_right(marty, steps):
    if(marty):
        print("Marty is well connected")
        marty.sidestep("right",steps,35,1000,)
    else:
        print("Marty is sadely not connected")
        return 0


def move_backward(marty, steps):
    if(marty):
        print("Marty is well connected")
        marty.walk(2,'auto',steps,-25,1500) # Walk still work the same way , but negative distance make it walk backward 
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
    coordonnees = []
    for pos in lignes[1:]:
        x = int(pos[0])
        y = int(pos[1])
        if not (0 <= x < taille_grille and 0 <= y < taille_grille):
            raise ValueError(f"Coordonnée ({x}, {y}) hors de la grille {taille_grille}x{taille_grille}")
        coordonnees.append((x, y))
    print(taille_grille)
    print(coordonnees)
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