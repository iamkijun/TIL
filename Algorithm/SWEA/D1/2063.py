N = int(input())

a = map(int, input().split())
a = list(a)

a.sort(reverse = False)

num = N // 2
print(a[num])