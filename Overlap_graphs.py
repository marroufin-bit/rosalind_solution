fasta_dict = {}
current_id = ""

with open("rosalind_grph.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]  
            fasta_dict[current_id] = ""
        else:
            fasta_dict[current_id] += line



for key1 in fasta_dict.keys():
    for key2 in fasta_dict.keys():
        if fasta_dict[key1][-3:] ==  fasta_dict[key2][:3] and key1 != key2:
            print(key1,key2)


