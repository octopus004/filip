
ime = ['f','i','l','i','p']
c= {}   
b = [None] * len(ime)

comparisons = 0
swaps = 0
add = 0


for j in ime:
    c[j] = 0
    swaps+=1

for j in ime:
    c[j] +=1
    comparisons +=1
    swaps+=1

keys = list(c.keys())

for j in range(1,len(keys)):
    key = keys[j]
    c[key] = c[keys[j-1]] + c[key]
    comparisons+=1
    swaps+=1
    add+=1

for j in range(len(ime)-1, -1, -1):
    b[c[ime[j]]-1] = ime[j]
    c[ime[j]] -= 1
    swaps+=1

print(b, comparisons, swaps, add)