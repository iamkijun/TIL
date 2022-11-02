s = "-1 -2 -3 -4"

def solution(s):
    num = list(map(int, s.split()))
    ans = [min(num),max(num)]
    ans = str(f'{ans[0]} {ans[1]}')
    return ans

print(solution(s))