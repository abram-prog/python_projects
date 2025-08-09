sticks = 10
player = 1

while True:
    print(f'\nSticks left: {sticks}')
    try:
        take = int(input(f'Player {player}, how many sticks do you take?(1-3)'))
    except ValueError:
        print(f'You have to enter the number 1, 2 or 3')
        continue
    if take not in (1,2,3):
        print(f'You can only take 1, 2 or 3 sticks')
        continue
    if take > sticks:
        print(f"You can't take that much - there are fewer sticks left")
        continue
    sticks -= take

    if sticks == 0:
        print(f'Player {player} took the last stick and lost.')
        print(f'The player {2 if player == 1 else 1} won !')
        break

    player = 2 if player == 1 else 1
