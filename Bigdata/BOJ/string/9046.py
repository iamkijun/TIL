T = int(input())

for t in range(T):
    s= input()
    s =s.replace(' ','')

    counts = [0] * 26
    
    for val in s:
        counts[ord(val)-97] += 1

    if counts.count(max(counts)) > 1:
        print("?")
    else:
        print(chr(counts.index(max(counts)) + 97))
