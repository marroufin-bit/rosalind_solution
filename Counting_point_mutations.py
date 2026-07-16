file = open("rosalind_hamm.txt")
sequences = []
hamming_distance = 0

for line in file:
    line = line.strip()
    sequences.append(line)

for i in range(len(sequences[0])):
    if sequences[0][i] != sequences[1][i]:
        hamming_distance +=1

print(hamming_distance)