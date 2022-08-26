import sys
sys.stdin = open('input.txt','r')

#빙고 만들기
bingo = [list(map(int, input().split())) for _ in range(5)]

#부르는 숫자 리스트
call = []
for i in range(5):
    call += list(map(int,input().split()))

# [1] 빙고에 있는 번호를 불러와서 0으로 변환해주기
def load(num,arr):
    for i in range(5):
        for j in range(5):
            if num == arr[i][j]:
                arr[i][j] = 0
                return

def is_bingo(arr):
    count = 0
    ver1=0 #대각선\합
    ver2=0 #대각선/합
    for i in range(5):
        #[1]행
        if sum(arr[i]) == 0:
            count +=1
        #[2]열
        ver =0
        for j in range(5):
             ver += arr[j][i]
        if ver == 0:
            count +=1
        #[3]대각선
        ver1 += arr[i][i]
        ver2 += arr[4-i][i]
    if ver1 ==0:
        count +=1
    if ver2 ==0:
        count +=1

    return count


cnt = 0
while True:
    call_num = call[cnt]  # 0번째 인덱스부터
    cnt += 1              # 부른 숫자의 수

    #[1] 0으로 변환
    load(call_num, bingo)

    #[2] 3빙고여부 확인
    if is_bingo(bingo) >= 3:
        break

print(cnt)
