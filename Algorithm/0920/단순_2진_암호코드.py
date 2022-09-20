import sys
sys.stdin = open('input.txt','r')

dct3 = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}


def solve():
    for st in arr:
        if '1' in st:
            # [1] 연속된 0, 1의 개수를 저장 cnts
            cnts = []
            old = 0  # 시작위치(1 또는 0값)
            for i in range(len(st)):
                if st[old] != st[i]:
                    cnts.append(i - old)
                    old = i

            # [2] cnts[] -> 암호변환 (dct3참조)
            ans = []
            for i in range(1, 32, 4):
                ans.append(dct3["".join(map(str, cnts[i:i + 3]))])

            # [3] 검증후 오류없으면 합, 오류면 0리턴
            even = ans[0] + ans[2] + ans[4] + ans[6]
            odd = ans[1] + ans[3] + ans[5] + ans[7]
            if (even * 3 + odd) % 10 == 0:
                return even + odd
            else:
                return 0


T = int(input())
# T = 10
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve()
    print(f'#{test_case} {ans}')