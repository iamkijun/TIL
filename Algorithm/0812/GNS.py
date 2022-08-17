import sys
sys.stdin = open("input.txt", "r", encoding='UTF-8')

T = int(input())
alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
num = [0,1,2,3,4,5,6,7,8,9]
def alpha_to_num(a):
    for i in range(10):
        if a == alpha[i]:
            return num[i]

def num_to_alpha(b):
    for j in range(10):
        if b == num[j]:
            return alpha[j]

for t in range(1,T+1):
    T, N= input().split()
    N = int(N)
    li = list(map(str, input().split()))

    for i in range(N):
        li[i] = alpha_to_num(li[i])
    
    li.sort()

    for j in range(N):
        li[j] = num_to_alpha(li[j])

    print(T)
    print(*li)

        


    