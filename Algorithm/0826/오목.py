import sys
sys.stdin = open('input.txt','r')

def omok(N,arr):
    for i in range(N):
        for j in range(N-4):
            if arr[i][j:j + 5] == 'ooooo':
                return 'YES'
            ver_str = ''
            cro_str1 = ''
            cro_str2 =''
            for d in range(5):
                ver_str += arr[j+d][i]
                try:
                    cro_str1 += arr[i+d][j+d]
                    cro_str2 += arr[i+4-d][j+d]
                except:
                    pass
            if ver_str == 'ooooo' or cro_str2 == 'ooooo' or cro_str1 == 'ooooo':
                return 'YES'

    return 'NO'


T = int(input())

for t in range(1,T+1):
    N = int(input())
    arr = [str(input()) for _ in range(N)]

    print(f'#{t} {omok(N,arr)}')
