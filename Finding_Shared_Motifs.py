sequences = []

with open("rosalind_lcsm.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            sequences.append("")
        else:
            sequences[-1] += line

sequences.sort(key=len,reverse=False)

def extract_sous_chaine(seq):
    sous_chaine = set()
    for i in range(len(seq)):
        for j in range(1,len(seq)-i+1):
            sous_chaine.add(seq[i:i+j])
    sous_chaine = sorted(sous_chaine,key=len,reverse=True)
    return sous_chaine 

query = extract_sous_chaine(sequences[0])
sequences.pop(0)


for el in query:
    if all(el in targets for targets in sequences):
        print(el)
        break


    

