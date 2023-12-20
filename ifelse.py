n = int(input('write a number:'))

if n%2 == 1:
    print('weired')

elif n%2 == 0 and n>=2 and n<=5:
    print('not weired')

elif n%2 == 0 and n>=6 and n<=20:
    print('weired')

elif n%2 == 0 and n>20: 
    print('not weired')

else:
    print('invalid')    
