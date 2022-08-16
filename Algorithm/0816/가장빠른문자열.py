import sys
sys.stdin = open("input.txt","r")

T = int(input())
for t in range(1, T+1):

    A, B = map(str, input().split())
    A = list(A)
    B = list(B) # 둘 다 리스트로 변환

    original_len_A = len(A) # 원래 A의 길이 저장

    count = 0 #횟수 세기
    i = 0

    while i <= len(A): # 전부 다 돌았을 때 종료
        if A[i:i+len(B)] == B:
            count +=1 # B에 A가 있을 경우, +1
            A = A[i+len(B):] # A를 그 이후부터로 재선언
            i = 0 #다시 0번째 인덱스부터 돌리기
        else:
            i+=1 # 그렇지 않을 경우, 1씩 돌려서 찾아 나서기

    ans = original_len_A - (len(B)-1) * count #찾은 B의 개수만큼 len(B) -> 1로 바뀌니까 계산해주기

    print(f'#{t} {ans}')