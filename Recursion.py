# Fabonacci series using recursion

def fibo(n):
    if n <=1:
        return n
    else:
        ans  = fibo(n-1) + fibo(n-2)
        print(ans)
        return ans

fibo(9)