fasta_dict = {}
current_id = ""
bases =['A','C','G','T']

with open("rosalind_cons.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]  
            fasta_dict[current_id] = ""
        else:
            fasta_dict[current_id] += line

col_number = len(fasta_dict[next(iter(fasta_dict))])
row_number = 4


matrix = []

for i in range(row_number):
    temp =[]
    for j in range(col_number):
        temp += [0]
    matrix.append(temp)


for seq in fasta_dict.keys():
    for i in range(len(fasta_dict[seq])):
        for j in range(len(bases)):
            if fasta_dict[seq][i] == bases[j]:
                matrix[j][i] += 1

        
seq_consensus = ""

for column in range(col_number):
    max = 0
    index = 0
    for row in range(row_number):
        if matrix[row][column] > max :
            max = matrix[row][column]
            index = row
    seq_consensus += bases[index]


print(seq_consensus)
for i in range(len(matrix)):
    print(f"{bases[i]}:",*matrix[i])