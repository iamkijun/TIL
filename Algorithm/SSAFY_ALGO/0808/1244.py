import sys
sys.stdin = open("s_input.txt","r")

n = int(input())
a = list(map(int, input().split()))
stu_num = int(input())

for k in range(stu_num):
    mf, re_num = map(int, input().split())

    if mf == 1:
        for i in range(n):
            if (i + 1) % re_num == 0:
                if a[i] == 0:
                    a[i] = 1
                elif a[i] == 1:
                    a[i] = 0
    else:
        if a[re_num - 1] == 0:
            a[re_num - 1] = 1
        elif a[re_num - 1] == 1:
            a[re_num - 1] = 0
        j = 1

        while True:
            if re_num - j >= 1 and re_num + j <= n:
                if a[re_num + j - 1] == 0 and a[re_num - j - 1] == 0:
                    a[re_num + j - 1], a[re_num - j - 1] = 1, 1
                    j += 1
                    continue
                elif a[re_num + j - 1] == 1 and a[re_num - j - 1] == 1:
                    a[re_num + j - 1], a[re_num - j - 1] = 0, 0
                    j += 1
                    continue
                else:
                    break
            else:
                break

for i in range(len(a)):
    if i != 0 and i % 20 ==0:
        print("")
    print(a[i], end=" ")