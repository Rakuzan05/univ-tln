HEADER = '\033[95m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Codes pour l'affichage en couleur du / des caractère(s) érronés

def scanner(s):
    list_ul = []
    OP = {'+', '-', '*', '/'}
    i = 0
    while i < len(s):
        if s[i].isdigit(): #Identification d'un nombre + ajout sans les cotes dans la liste
            nb = 0
            while i < len(s) and s[i].isdigit():
                nb *= 10
                nb += int(s[i])
                i += 1
            i -= 1 #Décrémentation de i pour garder le bon indice après la prochaine incrémentation
            list_ul.append(('NOMBRE', nb))

        elif s[i] in OP:
            list_ul.append(('OP', s[i]))
        elif s[i] == '(':
            list_ul.append(('PAR_OUV', s[i]))   #Gestion des autres cas (Opérateur, parenthèses ouvrantes et fermantes, erreur)
        elif s[i] == ')':
            list_ul.append(('PAR_FER', s[i]))
        elif s[i] == ' ' or s[i] == '\n' :
            pass
        else:
            error(s,i)
            return None
        i += 1
    return list_ul

def error(s,i):   #Fonction affichant le caractère lié à l'erreur de syntaxe 
    print(f"{FAIL} ERREUR SYNTAXIQUE {s[0]} {ENDC}")
    for j in range(len(s)):
        print(s[j], end ="", sep="")
        if j == i:
            print(f"{BOLD}{FAIL}{s[j]}{ENDC}", end="",sep="") #Parcours de la chaine jusqu'à retomber sur le caractère érroné passé en paramètre, puis affichage de celui-ci
    print("\n")



