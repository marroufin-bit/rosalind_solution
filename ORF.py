seq = ""
with open("rosalind_orf.txt") as file:
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            pass
        else:
            seq += line
dictionnaire_genetique = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}
liste_prot =[]
arn_sens = seq.replace("T", "U")
complements = str.maketrans("ACGT", "UGCA")
arn_reverse = seq.translate(complements)[::-1]

def extraire_orf(arn_seq):
    for j in range(3):
        prot_chaine = ""
        for i in range(j, len(arn_seq) - 2, 3):
            codon = arn_seq[i:i+3]
            aa = dictionnaire_genetique.get(codon)
            if aa == "Stop":
                prot_chaine += "*"
            elif aa:
                prot_chaine += aa
            else:
                break

        for idx in range(len(prot_chaine)):
            if prot_chaine[idx] == "M":
                fin = prot_chaine.find("*", idx)
                if fin != -1:
                    liste_prot.append(prot_chaine[idx:fin])

extraire_orf(arn_sens)
extraire_orf(arn_reverse)

for prot in set(liste_prot):
    print(prot)