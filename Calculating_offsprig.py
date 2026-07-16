file = open("rosalind_iev.txt")


population = file.read().split()

population = [int(x) for x in population]

Offspring_per_couple = 2

list_proba = [1,1,1,0.75,0.5,0]


result = 0

for i in range(len(population)) : 
    result += population[i]*list_proba[i]*Offspring_per_couple


print(result)
