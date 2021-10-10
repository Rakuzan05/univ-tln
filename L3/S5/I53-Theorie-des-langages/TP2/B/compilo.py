import Scanner, Parser, Codegen, sys, os    #Appel des modules précédents

if (os.path.isfile(sys.argv[1])):           #Cas d'un fichier
    f = open(sys.argv[1],"r")
    str_s = f.read()
else:
    str_s = sys.argv[1]                     #Cas d'une chaîne de caractères

l = Scanner.scanner(str_s)                  #Analyse lexicale

if l:
    postfix = Parser.parser(l)              #Analyse syntaxique
else:
    exit(1)

if postfix:                                 #Simulation de la pile + passage en postfixe
    Codegen.codegen(postfix)
    os.system("chmod u+x a.out")
