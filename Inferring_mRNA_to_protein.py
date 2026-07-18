file = open("rosalind_mrna.txt")

for line in file:
    line = line.strip()
    prot = line

dictionnaire_genetique = {
"F":2,"L":6,"S":6,"Y":2,"C":2,"W":1,"P":4,"H":2,"Q":2,"R":6,"I":3,"M":1,"T":4,"N":2,"K":2,"V":4,"A":4,"D":2,"E":2,"G":4
}

values = []

for base in line :
    values.append(dictionnaire_genetique[base]) 
values.append(3)

sum = 0 

for i in range(len(values)):
    if i == 0:
        sum += values[i]
    else : 
        sum *= values[i]

print(sum%1000000)
