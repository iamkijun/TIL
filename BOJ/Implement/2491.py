import sys
sys.stdin = open('input.txt','r')

N = int(input())

li = list(map(int, input().split()))

count_plus = 1          # 증가하는 수열일때 개수
count_minus = 1         # 감소하는 수열일때 개수
max_plus = 0            # 증가 수열의 최대값
max_minus = 0           # 감소 수열의 최대값


for i in range(N-1):
    # 증가하는 수열일 때
    if li[i]<=li[i+1]:
        count_plus +=1
    elif li[i] > li[i+1]:
        if count_plus > max_plus:
            max_plus = count_plus
        count_plus = 1
    
    # 감소하는 수열일 때
    if li[i] >= li[i+1]:
        count_minus +=1
    elif li[i] < li[i+1]:
        if count_minus > max_minus:
            max_minus = count_minus
        count_minus = 1

#마지막에 비교 못하고 나왔으니까 비교해서 마무리 작업
if count_plus > max_plus:
    max_plus = count_plus
if count_minus > max_minus:
    max_minus = count_minus

#증가수열과 감소수열의 최대값 비교
if max_minus>= max_plus:
    print(max_minus)
else:
    print(max_plus)