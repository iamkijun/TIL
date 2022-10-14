import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N, K = map(int, input().split())

Q = list(range(1,N+1))
yo = []


rem = K-1

for i in range(N):

    yo.append(Q.pop(rem))
    if Q:
        rem = (rem + K-1)%len(Q)
    else:
        break

print('<',end ="")
for val in yo:
    if val == yo[-1]:
        break
    print(val, end=", ")
    
print(yo[-1], end="")
print('>')