T = int(input())

for i in range(1,T+1):
    n = input()
    y = int(n[:4])
    m = int(n[4:6])
    d = int(n[6:])
    if m in range(1,13):
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d in range(1, 32):
                print(f"#{i} {n[:4]}/{n[4:6]}/{n[6:]}")
            else:
                print(f"#{i} -1")
        elif m == 2:
            if d in range(1, 29):
                print(f"#{i} {n[:4]}/{n[4:6]}/{n[6:]}")
            else:
                print(f"#{i} -1")
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d in range(1, 31):
                print(f"#{i} {n[:4]}/{n[4:6]}/{n[6:]}")
            else:
                print(f"#{i} -1")
    else:
        print(f"#{i} -1")