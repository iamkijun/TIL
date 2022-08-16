import sys
sys.stdin = open("input.txt","r")

T = int(input())

for t in range(1, T+1):
    # 다섯개의 문자열을 담을 빈 리스트 선언
    arr = []
    # 다섯개의 문자열의 최대 길이를 저장할 변수 max_len 선언
    max_len = 1

    for _ in range(5):
        li = list(map(str, input()))
        arr.append(li)
        
        # 다섯개의 문자열 중 최대 길이를 저장
        if len(li) > max_len:
            max_len = len(li)


    for i in range(5):
        # arr[i]가 최대길이가 아닐경우 빈 문자열 ''을 부족한 만큼 덧붙이기
        if len(arr[i]) < max_len:
            arr[i] = arr[i] +[''] * (max_len-len(arr[i]))

    #출력하고자 하는 문자열 변수 S 선언
    S = ""
    
    #세로로 출력한 값을 S에 저장
    for i in range(max_len):
        for j in range(5):
            S += arr[j][i]

    print(f'#{t} {S}')