import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = input()

    dic = {'S':0, 'D':1, 'H':2, 'C':3}

    arr = [[] for _ in range(4)]

    for i in range(0,len(S), 3):
        num = int(S[i+1:i+3])
        arr[dic[S[i]]].append(num)

    ans = []

    for i in range(4):
        if len(arr[i]) != len(set(arr[i])):
            print(f'#{t} ERROR')
            break
        else:
            ans.append(13-len(arr[i]))
    else:
        print(f'#{t}',*ans)


    new_S = []
