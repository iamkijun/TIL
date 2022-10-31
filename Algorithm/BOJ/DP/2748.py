import sys
sys.stdin = open('DP/input.txt','r')

N = int(input())

fibo = [0] * 91
fibo[0], fibo[1] = 0,1

def fib(n):
    if n == 0:
        return fibo[0]
    elif n ==1:
        return fibo[1]
    else:
        if fibo[n] == 0:
            fibo[n] = fib(n-1) + fib(n-2)
            return fibo[n]
        else:
            return fibo[n]

print(fib(N))
