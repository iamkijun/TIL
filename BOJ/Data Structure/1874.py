import sys
sys.stdin = open('input.txt','r')

n = int(input())
li = []

num_li =[]
for i in range(1, n+1):
    li.append(i)
    a = int(input())
    num_li.append(a)

print(li)
print(num_li)

stk = []
k = 1
resul
for i in range(n):
    while True:
        if new[i] == num_li[i]:
            break
        else:
            stk.append(k)
            k= k+1
            print('+')

print(new)
print(stk)