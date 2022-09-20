T = int(input())

l = [[]]

for i in range(T):
    n = int(input())
	
    print("#%d"%(i+1))

    for j in range(n):

        a, b = map(str, input().split())
        b = int(b)

        for k in range(b):
            l[-1].append(a)
            if len(l[-1]) == 10:
                l.append([])
    
    s = ""

    
    for m in range(len(l)):
        for n in range(len(l[m])):
                s = s + l[m][n]
        print(s)
        s = ""

    l = [[]]