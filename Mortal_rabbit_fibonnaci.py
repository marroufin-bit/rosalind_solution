file = open("rosalind_fibd.txt")
data = file.read().split()
data = [int(x) for x in data]
max_month = data[0]
living_limit = data[1]

rabbits_age = [0] * living_limit
rabbits_age[0] = 1


for month in range(1,max_month):
    new_rabbits = sum(rabbits_age[1:])
    rabbits_age = [new_rabbits] + rabbits_age[:-1]


print(sum(rabbits_age))

