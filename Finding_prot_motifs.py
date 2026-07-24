import urllib.request

file = open("rosalind_mprt.txt")


fasta_dict = {}

for prot in file:
    prot = prot.strip()
    accession_id = prot.split("_")[0]
    url = f"https://rest.uniprot.org/uniprotkb/{accession_id}.fasta"
    with urllib.request.urlopen(url) as response:
        lines = response.read().decode('utf-8').splitlines()
        fasta_dict[prot] = ""
        for line in lines:
            line = line.strip()
            if not line.startswith('>'):
                fasta_dict[prot] += line



for prot in fasta_dict.keys():
    motif_found = False
    motif_coordonees =[]
    for i in range(len(fasta_dict[prot])-3):
        if fasta_dict[prot][i] == "N" and fasta_dict[prot][i+1] != "P" and fasta_dict[prot][i+2] in "ST"  and fasta_dict[prot][i+3] != "P":
            motif_found = True
            motif_coordonees.append(i+1)
    if motif_found == True :
        print(prot)
        print(*motif_coordonees)


    
