months = 36 
pair_generated = 5


for i in range(months):
    if i == 0 :
        pairs_f = 0
        pairs_no_f = 1
    else : 
        pred_pair = pairs_f
        pairs_f += pairs_no_f
        pairs_no_f = pair_generated*pred_pair


result = pairs_no_f + pairs_f

print(result)