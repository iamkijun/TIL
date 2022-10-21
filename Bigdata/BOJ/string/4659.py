def good(s):
    
    collection = ['a','e','i','o','u']
    count=0
    for i in range(len(s)):
        if s[i] in collection:
            count+=1
    
    if count > 0:
        pass
    else:
        return 0
            

    for i in range(len(s)-2):
        if s[i] in collection and s[i+1] in collection and s[i+2] in collection:
            return 0
        elif s[i] not in collection and s[i+1] not in collection and s[i+2] not in collection:
            return 0
        else:
            continue

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] == 'e' and s[i+1] == 'e':
                continue
            elif s[i] == 'o' and s[i+1] == 'o':
                continue
            else:
                return 0

    return 1

while True:
    S = input()
    if S == 'end':
        break

    if good(S):
        print(f'<{S}> is acceptable.')
    else:
        print(f'<{S}> is not acceptable.')
