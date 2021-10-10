"""
Expr -> Terme Reste_E

Reste_E -> OU Terme Reste_e
        | None

Terme   -> Fact Reste_t

Reste_t -> ET Fact Reste_t
        |  None

Fact    -> BOOL
        |  ! BOOL
        | (Exp)

BOOL    -> VRAI | FAUX

"""
l = []
i = 0
postfixed_l = []
def parser(unilex) :  #Analyse d'une liste d'unités lexicales, reconnaissance d'une expression de taille conforme + retour en notation postfixe
    global i, l
    l = unilex
    if expr() and i == len(l):
        print("Chaine valide")
        return postfixed_l
    else:
        if i >= len(l):
            print(f"Chaine invalide à cause du caractère {l[-1][1]} dépassement d'indice")
        else:
            print(f"Chaine invalide à cause du caractère {l[i][1]}")

#Application de la grammaire pour reconnaître chaque cas

def expr():
    global i
    if terme() and reste_e():
        return True
    return False


def reste_e():
    global i

    if i < len(l) and l[i][1] == "OU" :
        op = "or"
        i += 1
        if terme():
            postfixed_l.append(op)
            if reste_e():
                return True
            else:
                return False
        else:
            return False
    return True

def terme() :
    global i
    if fact() and reste_t():
        return True
    return False

def reste_t():
    global i
    if i < len(l) and l[i][1] == "ET":
        op = "and"
        i += 1
        if fact():
            postfixed_l.append(op)
            if reste_t():
                return True
            else:
                return False
        else:
            return False
    return True

def fact():
    global i
    if i < len(l) and l[i][1] == "NON":
        op = "not"
        i += 1
        if fact():
            postfixed_l.append(op)
        else:
            return False

    elif i < len(l) and l[i][0] == "BOOL":
        postfixed_l.append(l[i][1])
        i += 1

    elif i < len(l) and l[i][1] == '(':
        i += 1
        if expr() :
            if i < len(l) and l[i][1] == ')':
                i += 1
                return True;
            else:
                return False
        else:
            return False
    else:
        if i >= len(l):
            print(f"Chaine invalide à cause du caractère {l[-1][1]} dépassement d'indice")
        else:
            print(f"Chaine invalide à cause du caractère {l[i][1]}")
        return False

    return True


