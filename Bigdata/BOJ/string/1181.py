N = int(input())
l = []

for i in range(N):
    a = input()
    l.append(a)

l = set(l)
l = list(l)

l = sorted(l, key = lambda x: (len(x),x))

for j in range(len(l)):
    print(l[j])