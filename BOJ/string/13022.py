import sys
sys.stdin = open('string/input.txt','r')

T = int(input())
for t in range(T):
    s = list(input().split())
    animal = ''
    while True:
        animal = list(input().split())

        if animal == ['what','does','the','fox','say?']:
            break
        else:
            for i in range(s.count(animal[2])):
                s.remove(animal[2])
    
    print(*s)

