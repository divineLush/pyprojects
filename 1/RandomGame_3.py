from random import randint

def game():
    randnum = randint(1, 30)
    isover = False

    for i in range(5):
        print('now guess')
        inp = int(input())

        if (inp == randnum):
            isover = True
            break

        if (inp > randnum):
            print('try smaller num')
        else:
            print('try bigger num')


    if (isover):
        print('best')
    else:
        print('fffuuuuuuu')

    print(f'the number was {randnum} btw')


while True:
    game()
    print('wanna play again? y/n')
    ans = input()
    if (ans != 'y'):
        break
