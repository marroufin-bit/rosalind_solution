import math

file = open("rosalind_lia.txt")

entrées = file.read().split()

entrées = [ int(x) for x in entrées ]

generation = entrées[0]

number_of_organisms = entrées[1]
total_organisms = 2 ** generation
p = 1/4
proba_out = 1 

for i in range(number_of_organisms):
    comb = math.comb(total_organisms, i)
    prob_i = comb * (p ** i) * ((1 - p) ** (total_organisms - i))
    proba_out -= prob_i

print(round(proba_out, 3))