N = int(input())
total = 0


for i in range(N):
    li = []
    a=0
    s = list(input())

    for j in range(len(s)):
        if s[j] not in li:
            li.append(s[j])
        elif s[j] in li:
            if s[j-1] == s[j]:
                pass
            elif s[j-1] != s[j]:
                a=1
    if a == 0:
        total += 1
        
print(total)