import sys
sys.stdin = open("input.txt","r")

# def solve():
#     for leng in range(N,1,-1): #길이 N부터 1씩 감소
#         for lst in arr1:
#             for i in range(N-leng+1): #  시작 위치
#                 if lst[i:i+leng] == lst[i:i+leng][::-1]:
#                     return leng
#
#         for lst in arr2:
#             for i in range(N-leng+1): #  시작 위치
#                 if lst[i:i + leng] == lst[i:i + leng][::-1]:
#                     return leng
#     return leng

def is_sym(arr, leng):
    for lst in arr:
        for i in range(N-leng+1): #시작위치
            for j in range(leng//2):
                if lst[i+j] != lst[i+(leng-1)-j]:
                    break
            else: #for-else, break 안했다는건 모두 일치!
                return True
    return False

T = 10

for t in range(1,T+1):
    a = int(input())
    N = 100

    arr1 = [input() for _ in range(N)]
    arr2 = list(zip(*arr1))

    # ans = solve()

    for ans in range(N, 1, -1):
        if is_sym(arr1, ans) or is_sym(arr2, ans):
            break

    print(f'#{t} {ans}')