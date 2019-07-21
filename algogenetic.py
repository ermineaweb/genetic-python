import random

# Fonction intialiser() :
# Initialisation d'une population sous forme de tableau
# la population est composée d'un nombre d'individus
# chaque individu est composé d'un nombre de chromosome
# chaque chromosome prend une valeur aléatoire
# nbIndividu -> nombre d'individus
# nbChromosome -> nombre de chromosomes
# valChromosome -> valeur maximal des chromosomes
# return : un tableau à deux dimensions
def initialiser(nbIndividu, nbChromosome, valChromosome):
    population = [[0] * nbChromosome for n in range(nbIndividu)]
    for i in range(0, nbIndividu):
        for c in range(0, nbChromosome):
            population[i][c] = (random.randint(1, valChromosome))
    return population

# Fonction selectionner() :
# si la somme des chromosomes de l'individu est compris
# dans l'intervalle de precision, on le garde, sinon on le supprime
# exemple : 
# precision = 80% 
# cible = 10
# l'intervalle sera 8 - 12
# individu : 4, 2, 3 = 9 -> gardé
# individu : 5, 3, 6 = 14 -> supprimé 
def selectionner(pop, cible, precision):
    return [p for p in pop if sum(p) in range(int(cible*(1-precision)), int(cible*(1+precision)))]

# Fonction comparer() :
# Vérification si un individu de la population correspond à la cible
def comparer(pop, cible):
    for p in pop:
        if (sum(p) == cible):
            return p

# Fonction afficher() :
# affichage de la population avec la valeur des individus (somme des chromosomes)
def afficher(population):
    print("Nombre d'individus : {}".format(len(population)))
    for p in population:
            print("{} - {}".format(p, sum(p, 0)))

# Fonction croiser() :
# parmi la population d'individus, on prend aléatoirement
# deux individus, on créé un troisième en suivant ce shéma :
# père   PPXX 
# mère   XXMM 
# enfant PPMM
def croiser(pop):
    newpopulation = [[0] * len(pop[0]) for n in range(len(pop))]
    for p in range(0, len(pop)):
        n = random.randrange(0, len(pop))
        newpopulation[p][0:int(len(pop[0])/2)] = pop[n][0:int(len(pop[0])/2)]
        n = random.randrange(0, len(pop))
        newpopulation[p][-int(len(pop[0])/2):] = pop[n][-int(len(pop[0])/2):]
    return newpopulation
# Autres croisements possibles à tester (idées à développer) :
# - trier les chromosomes des individus avant croisement
# - ne prendre que les extrémités, exemple : PXXX + XXXM -> PXXM
# - rendre un parent "fort", exemple : PPPX + XXXM -> PPPM

# Fonction muter() :
# un chromosome aléatoire d'un individu aléatoire est 
# remplacé par un chromosome aléatoire
# on répète l'opération 'nbMutation' fois
def muter(pop, valChromosome, nbMutation):
    while(nbMutation >= 0):
        individu = random.randrange(0, len(pop))
        chromosome = random.randrange(0, len(pop[0]))
        pop[individu][chromosome] = random.randint(0, valChromosome)
        nbMutation -= 1
    return pop

# paramètres à faire varier
NB_CHROMOSOME_MAX = 5
VAL_CHROMOSOME_MAX = 6
NB_INDIVIDU_MAX = 5
PRECISION = 90/100
NB_MUTATION = 2
CIBLE = 10
# p est l'individu qui atteint l'objectif 
# si p = cible on a trouvé un individu
p = 0
# compteur de nombre de tentatives
essai = 1

# MAIN
print("### NAISSANCE POPULATION")
pop = initialiser(NB_INDIVIDU_MAX, NB_CHROMOSOME_MAX, VAL_CHROMOSOME_MAX)
afficher(pop)
p = comparer(pop, CIBLE)
while (not p) and (len(pop) > 0):
    essai += 1
    print("### SELECTION")
    pop = selectionner(pop, CIBLE, PRECISION)    
    print("### VERIFICATION")
    p = comparer(pop, CIBLE)
    if (p or len(pop) <= 0): break
    print("### CROISEMENT")
    pop = croiser(pop)
    print("### VERIFICATION")
    p = comparer(pop, CIBLE)
    if (p or len(pop) <= 0): break
    print("### MUTATION")
    pop = muter(pop, VAL_CHROMOSOME_MAX, NB_MUTATION)
    print("### VERIFICATION")
    p = comparer(pop, CIBLE)
    if (p or len(pop) <= 0): break
    afficher(pop)

if (p):
    print("La séquence {} valide la cible : {}".format(p, CIBLE))
else:
    print("Population épuisée, aucune séquence ne correspond à la cible : {}".format(CIBLE))
print("Nombre d'essai : {}".format(essai))
