
list = ['f','i','l','i','p']
h = [2,1]
comparisons = 0
swaps = 0
n = len(list)

for i in range(len(h)):
    inc = h[i]
    for j in range(inc, n):
        y = list[j]
        k = j - inc
        while(k >= 0):
            comparisons +=1
            if(y < list[k]):
                list[k+inc] = list[k]
                k = k-inc
                swaps +=1
            else:
                break
        list[k+inc] = y

   
print(comparisons, swaps)