import sys
sys.stdin = open("s_input.txt","r")

T = int(input())
for test_case in range(1, T+1):
    a = int(input())
    li = [0] * 12
    count = 0

    while a != 0:
        li[a%10] += 1
        a = a // 10

    for i in range(10):
        if li[i] >= 3:
            li[i] -= 3
            count+=1
        if li[i] >= 1 and li[i+1] >= 1 and li[i+2] >=1:
            li[i],li[i+1],li[i+2] = li[i]-1,li[i+1]-1,li[i+2]-1
            count +=1

    if count ==2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
