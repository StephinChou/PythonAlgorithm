import time
def isOK(x,k):
    for i in range(1,k):
        if x[i] == x[k] or abs(x[i]-x[k]) == abs(i-k):
            return False      
    return True
def print_queen(x,n):
    for i in range(n):
        pos = x[i]-1
        print('O '*pos + 'X ' + 'O '*(n-pos-1))
    print('')
sumsum = 0
def queen(n):
    global sumsum
    x = [0 for i in range(n+1)]
    k=1
    while k >0:
        x[k] += 1 #判断当前行的下一个位置是否合适
        if x[k] > n:
            x[k] = 0
            k -= 1
        elif isOK(x,k):
            if k == n:#完成一个解
                print_queen(x[1:],n)
                sumsum += 1
                x[k],k = 0,k-1
            else:
                k += 1
queen(8)
print(sumsum)





