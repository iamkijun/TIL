from curses.ascii import islower, isupper
import sys
sys.stdin = open('input.txt','r')

while True:
    try:
        S = input()

        gan_mo = ['a','i','y','e','o','u']
        gan_ja = ['b','k','x','z','n','h','d','c','w','g','p','v','j','q','t','s','r','l','m','f']

        gan_bmo = ['A','I','Y','E','O','U']
        gan_bja = ['B','K','X','Z','N','H','D','C','W','G','P','V','J','Q','T','S','R','L','M','F']


        new_S = []

        for i in range(len(S)):
            if S[i] in gan_mo:
                new_S.append(gan_mo[(gan_mo.index(S[i])+3)%6])
            elif S[i] in gan_ja:
                new_S.append(gan_ja[(gan_ja.index(S[i])+10)%20])
            elif S[i] in gan_bmo:
                new_S.append(gan_bmo[(gan_bmo.index(S[i])+3)%6])
            elif S[i] in gan_bja:
                new_S.append(gan_bja[(gan_bja.index(S[i])+10)%20])
            else:
                new_S.append(S[i])

        print(''.join(new_S))
    except:
        break