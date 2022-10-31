import sys
sys.stdin = open('Tree/input.txt','r')

N, Q =map(int, input().split())

li = set()

def visit(n,li):
    tem = n
    tem_li = []

    while tem > 0:
        tem_li.append(tem)
        tem = tem // 2
    
    tem_li = tem_li[::-1]

    for val in tem_li:
        if val in li:
            return val
    
    li.add(n)
    return 0

for i in range(Q):
    duck = int(input())
    result = visit(duck,li)
    print(result)
