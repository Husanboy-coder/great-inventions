import random
t = int(input('How many times do you wanna play: '))
l = ['rock', 'paper', 'scissors']
ps = 0
cs = 0
for i in range(t):
    a = input('Rock/Paper/Scissors: ').lower()
    b = random.choice(l)
    if a == b:
        print('Shoot! PC`s choice:', b, '\nDraw!')
        print(f"\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------")
    elif a == 'rock' and b == 'paper':
        print('Shoot! PC`s choice:', b)
        cs += 1
        print(f'You lost\n   Scores:\nYou: {ps}  PC: {cs}\n--------------------')
    elif a == 'rock' and b == 'scissors':
        print('Shoot! PC`s choice:', b)
        ps += 1
        print(f'You won!\n\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------')
    elif a == 'paper' and b == 'rock':
        print('Shoot! PC`s choice:', b)
        ps += 1
        print(f'You won!\n\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------')
    elif a == 'paper' and b == 'scissors':
        print('Shoot! PC`s choice:', b)
        cs += 1
        print(f'You lost\n\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------')
    elif a == 'scissors' and b == 'rock':
        print('Shoot! PC`s choice:', b)
        cs += 1
        print(f'You lost\n\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------')
    elif a == 'scissors' and b == 'paper':
        print('Shoot! PC`s choice:', b)
        ps += 1
        print(f'You won!\n\n    Scores:\nYou: {ps}  PC: {cs}\n--------------------')
print('Game is over!')
if ps > cs:
    print('Congrats! You are the winner!')
elif ps < cs:
    print('PC won')
else:
    print("Draw")
