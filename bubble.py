
comparisons = 0
swaps = 0

list = ['f', 'i','l','i','p']

n = len(list)
for j in range(n-1):
    for i in range(n-j-1):
        comparisons+=1
        if(list[i] > list[i+1]):
            swaps+=1
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
       
print(comparisons, swaps)


