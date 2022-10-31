import sys
sys.stdin = open('input.txt','r')

#내림차순으로 정렬 (선택정렬)
def selection_sort(lens, arr):
    for i in range(lens-1):
        max_idx = i
        for j in range(i+1, lens):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]
    
    return arr

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())

    subjects = list(map(int, input().split()))

    subjects = selection_sort(N,subjects)       #과목 점수를 내림차순 정렬

    ans = 0 #총점

    for k in range(K):
        ans += subjects[k]
    
    print(f'#{t} {ans}')