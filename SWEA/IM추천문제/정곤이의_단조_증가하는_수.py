import sys
sys.stdin = open('input.txt','r')

T = int(input())

def danjo(a,b):
    val = a* b
    val_list=[10]
    while val != 0:
        val_list.append(val%10)
        if val_list[-2] >= val_list[-1]:
            pass
        else:
            return 0
        val = val // 10

    return 1


for t in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort(reverse=True)

    danjo_list =[]

    for i in range(N-1):
        for j in range(i+1,N):
            if danjo(N_list[i],N_list[j]):
                danjo_list.append(N_list[i]*N_list[j])
                break
    if danjo_list:
        print(f'#{t} {max(danjo_list)}')
    else:
        print(f'#{t} -1')