import sys
sys.stdin = open('Tree/input.txt','r')

N, Q =map(int, input().split())

li = set()

def visit(n,arr):
    tem = n

    while tem >0:
        if tem in arr:
            ans = tem
            return ans
        tem = tem // 2
    
    li.add(n)
    return 0

for i in range(Q):
    duck = int(input())
    result = visit(duck,li)
    print(result)
