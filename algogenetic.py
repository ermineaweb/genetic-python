import random

# Fonction initPopulation() :
# Initialisation d'une population sous forme de tableau
# la population est composée d'un nombre d'individus
# chaque individu est composé d'un nombre de chromosome
# chaque chromosome prend une valeur aléatoire
# nbIndividu -> nombre d'individus
# nbChromosome -> nombre de chromosomes
# valChromosome -> valeur maximal des chromosomes
# return : un tableau à deux dimensions
def initPopulation(nIndividuals, nChromosome, valMaxChromosome):
    population = [[0] * nChromosome for n in range(nIndividuals)]
    for i in range(0, nIndividuals):
        for c in range(0, nChromosome):
            population[i][c] = (random.randint(1, valMaxChromosome))
    return population

# Fonction selectIndividuals() :
# si la somme des chromosomes de l'individu est compris
# dans l'intervalle de precision, on le garde, sinon on le supprime
# exemple : 
# precision = 80% 
# cible = 10
# l'intervalle sera 8 - 12
# individu : 4, 2, 3 = 9 -> gardé
# individu : 5, 3, 6 = 14 -> supprimé 
def selectIndividuals(pop, target, precision):
    return [p for p in pop if sum(p) in range(int(target*(1-precision)), int(target*(1+precision)))]

# Fonction findTarget() :
# Vérification si un individu de la population correspond à la cible
def findTarget(population, target):
    for p in population:
        if (sum(p) == target):
            return p

# Fonction printPopulation() :
# affichage de la population avec la valeur des individus (somme des chromosomes)
def printPopulation(population):
    print("Population's length : {}".format(len(population)))
    for p in population:
            print("{} - {}".format(p, sum(p, 0)))

# Fonction crossIndividuals() :
# parmi la population d'individus, on prend aléatoirement
# deux individus, on créé un troisième en suivant ce shéma :
# père   PPXX 
# mère   XXMM 
# enfant PPMM
def crossIndividuals(pop):
    newPopulation = [[0] * len(pop[0]) for n in range(len(pop))]
    for p in range(0, len(pop)):
        n = random.randrange(0, len(pop))
        newPopulation[p][0:int(len(pop[0])/2)] = pop[n][0:int(len(pop[0])/2)]
        n = random.randrange(0, len(pop))
        newPopulation[p][-int(len(pop[0])/2):] = pop[n][-int(len(pop[0])/2):]
    return newPopulation
# Autres croisements possibles à tester (idées à développer) :
# - trier les chromosomes des individus avant croisement
# - ne prendre que les extrémités, exemple : PXXX + XXXM -> PXXM
# - rendre un parent "fort", exemple : PPPX + XXXM -> PPPM

# Fonction muteIndividuals() :
# un chromosome aléatoire d'un individu aléatoire est 
# remplacé par un chromosome aléatoire
# on répète l'opération 'nbMutation' fois
def muteIndividuals(pop, valChromosome, nMutation):
    while(nMutation >= 0):
        individu = random.randrange(0, len(pop))
        chromosome = random.randrange(0, len(pop[0]))
        pop[individu][chromosome] = random.randint(0, valChromosome)
        nMutation -= 1
    return pop

# parameters
# paramètres à faire varier
NB_CHROMOSOME_MAX = 5
VAL_CHROMOSOME_MAX = 6
NB_INDIVIDUAL_MAX = 5
PRECISION = 90/100
NB_MUTATION = 2
TARGET = 10
# p est l'individu qui atteint l'objectif 
# si p = cible on a trouvé un individu
p = 0
# compteur de nombre de tentatives
attempts = 1

# MAIN
print("### BUILDING POPULATION")
pop = initPopulation(NB_INDIVIDUAL_MAX, NB_CHROMOSOME_MAX, VAL_CHROMOSOME_MAX)
printPopulation(pop)
p = findTarget(pop, TARGET)
while (not p) and (len(pop) > 0):
    attempts += 1
    print("### INDIVIDUALS SELECTION")
    pop = selectIndividuals(pop, TARGET, PRECISION)    
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    print("### INDIVUALS CROSSING")
    pop = crossIndividuals(pop)
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    print("### MUTATION")
    pop = muteIndividuals(pop, VAL_CHROMOSOME_MAX, NB_MUTATION)
    print("### COMPARE INDIVIDUALS TO TARGET")
    p = findTarget(pop, TARGET)
    if (p or len(pop) <= 0): break
    printPopulation(pop)

if (p):
    print("Individual {} validate the target : {}".format(p, TARGET))
else:
    print("Population is exhausted for target : {}".format(TARGET))
print("Attempts count : {}".format(attempts))
