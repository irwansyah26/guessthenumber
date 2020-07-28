import random

def guess():
    
    a = 1
    b = 5
    life = 3
    lvl = 1

    print('=' * 80)
    print('''\
                Welcome to Guess the Number Game!
                You have 3 lifes at the start.
                If you guess wrong, you will lose 1 life.
                and If you guess right, you will get 1 life and
                advance to the next level. Good Luck!''')
    print('=' * 80)
    
    while life != 0:
        num = random.randrange(a, b)
        print('Level', lvl,'( Range', a, 'to', b, ')')
        #print(num) #uncomment to view the answer
        answer = int(input('Anwer : '))

        while answer != num:
            life -= 1
            print('Wrong, Now you have', life, 'Life Left\n')
            answer = int(input('Anwer : '))

            if life == 0:
                break
            
        else:
            lvl += 1
            life +=1
            b +=3
            print('Nice, Now you have', life, 'Life Left\n')
    else:
        print('\nYou Lost\n')

#running the function
guess()

#play again
ask = input('Do you want to play again? ').strip().lower()
while ask == 'y':
    guess()
    ask = input('Do you want to play again? ')   
