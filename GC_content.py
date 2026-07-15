file = open("rosalind_fib.txt")

fasta_name = []
gc_content = []


seq = ""
for line in file :
    line = line.strip("\n")
    if line.startswith('>'):
        line = line.replace(">","")
        fasta_name.append(line)
        if seq :
            sum = 0
            for base in seq :
                if base =="C" or base =="G":
                    sum += 1
            gc_content.append((sum/len(seq))*100)


            seq = ""
    else : 
        seq += line
        
sum = 0
for base in seq :
    if base =="C" or base =="G":
        sum += 1
gc_content.append((sum/len(seq))*100)

max = 0
index = 0 
for i in range(len(gc_content)) :
    if gc_content[i] > max :
        index = i





print(fasta_name[index])
print(gc_content[index])