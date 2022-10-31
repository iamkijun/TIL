N= int(input())
li = []
re = ""
def divisor(n):
    for i in range(1,N+1):
        if N % i == 0:
            li.append(i)
    for j in range(len(li)-1): # 이부분 리스트를 출력 못하겠어서 해맸습니다.
        print(li[j], end=" ")# 이부분 리스트를 출력 못하겠어서 해맸습니다.
    
    return N

print(divisor(N))