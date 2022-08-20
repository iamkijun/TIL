l=[]
max_len = 0
for i in range(5):
    a = input()
    l.append(a)
    if len(a) > max_len:
        max_len = len(a)

for i in range(max_len):
    for j in range(5):
        try:
            print(l[j][i], end="")
        except:
            pass