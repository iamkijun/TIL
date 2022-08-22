import sys
sys.stdin = open('Function/4673.py')

n = int(input())
dic = {}
lose =[]
for i in range(6):
    a,b = map(int,input().split())
    if str(a) in dic:
        if b> dic[str(a)]:
            lose.append([a,dic[str(a)]])
            dic[str(a)] = b

        else:
            lose.append([a,b])
    else:
        dic[str(a)] = b

print((max(dic['4'],dic['3'])*max(dic['2'],dic['1'])-lose[0][1]*lose[1][1])*n)