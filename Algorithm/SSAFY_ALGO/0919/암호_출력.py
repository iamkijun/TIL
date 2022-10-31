import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    S = input()
    
    li = []

    for i in range(len(S)):
        if S[i].isdigit():
            li.append(int(S[i]) * 16**(len(S)-1-i))
        else:
            li.append((ord(S[i])-55) * 16**(len(S)-1-i))
            
    x = sum(li)
    y =''
    while x>0:
        y=str(x%2)+y
        x//=2

    print(f'#{t}', end =' ')
    while True:
        if y[:4] == '1101':
            print(0, end= " ")
            y= y[4:]
        elif y[0:5] == '01101':
            print(0, end= " ")
            y= y[5:]
        elif y[:6] == '001101':
            print(0, end= " ")
            y= y[6:]
        
        elif y[:5] == '10011':
            print(1, end= " ")
            y= y[5:]
        elif y[:6] == '010011':
            print(1, end= " ")
            y= y[6:]

        elif y[:6] == '111011':
            print(2, end= " ")
            y= y[6:]

        
        elif y[:6] == '110001':
            print(3, end= " ")
            y= y[6:]
        

        elif y[:6] == '100011':
            print(4, end= " ")
            y= y[6:]
        

        elif y[:6] == '110111':
            print(5, end= " ")
            y= y[6:]
        
        elif y[:4] == '1011':
            print(6, end= " ")
            y= y[4:]
        elif y[0:5] == '01011':
            print(6, end= " ")
            y= y[5:]
        elif y[:6] == '001011':
            print(6, end= " ")
            y= y[6:]

        elif y[:6] == '111101':
            print(7, end= " ")
            y= y[6:]

        elif y[:5] == '11001':
            print(8, end= " ")
            y= y[5:]
        elif y[:6] == '011001':
            print(8, end= " ")
            y= y[6:]

        elif y[:6] == '101111':
            print(9, end= " ")
            y= y[6:]

        else:
            print()
            break
    
    
