
comparisons = 0
swaps = 0

list = ['f', 'i','l','i','p']

n = len(list)
for i in range(1,n):
    k = list[i]
    j = i - 1
    while(j >= 0):
        comparisons +=1
        if(list[j] > k):
            swaps +=1
            list[j+1] = list[j]
            j = j - 1
        else:
            break
    list[j+1] = k
    
 
print(comparisons, swaps)
