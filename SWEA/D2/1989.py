n = int(input())
for i in range(n):
    a = input()
    re = a[::-1]
    if a == re:
        print("#%d 1"%(i+1))
    elif a != re:
        print("#%d 0"%(i+1))