import sys

file = open(sys.argv[1])


entrées = file.read().split()

entrées = [ int(x) for x in entrées ]
total = sum(entrées)
total_minus_1 = total - 1 


homo_dominant = entrées[0]/total
heterozyguous = entrées[1]/total
homo_recessive = entrées[2]/total

prob_het_het = heterozyguous * ((entrées[1] - 1) / total_minus_1) * 0.25
prob_rec_rec = homo_recessive * ((entrées[2] - 1) / total_minus_1) * 1.0
prob_het_rec = heterozyguous * (entrées[2] / total_minus_1) * 0.5
prob_rec_het = homo_recessive * (entrées[1] / total_minus_1) * 0.5

result = 1 - (prob_het_het + prob_rec_rec + prob_het_rec + prob_rec_het)
print(result)