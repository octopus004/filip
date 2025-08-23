
list = ['f', 'i','l','i','p']
comparisons = 0
swaps = 0
n = len(list)
for i in range(0,n-1):
    min = list[i]
    pos = i
    for j in range(i+1,n):
        comparisons +=1
        if(list[j] < min):
            min = list[j]
            pos = j
    if(pos!=i):
        list[pos] = list[i]
        list[i] = min
        swaps+=1

    
print(comparisons,swaps)