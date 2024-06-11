import curses
import random

dice_str: list = [
    ['         ',
     '         ',
     '         ',
     '         ',
     '         ',],
    ['┌───────┐',
     '│       │',
     '│   ⓿   │',
     '│       │',
     '└───────┘'],
    ['┌───────┐',
     '│ ⓿     │',
     '│       │',
     '│     ⓿ │',
     '└───────┘'],
    ['┌───────┐',
     '│ ⓿     │',
     '│   ⓿   │',
     '│     ⓿ │',
     '└───────┘'], 
    ['┌───────┐',
     '│ ⓿   ⓿ │',
     '│       │',
     '│ ⓿   ⓿ │',
     '└───────┘'],
    ['┌───────┐',
     '│ ⓿   ⓿ │',
     '│   ⓿   │',
     '│ ⓿   ⓿ │',
     '└───────┘'],
    ['┌───────┐',
     '│ ⓿   ⓿ │',
     '│ ⓿   ⓿ │',
     '│ ⓿   ⓿ │',
     '└───────┘']]
class dice_hand:

    def __init__(self, dice: list) -> None:
        self.dice = dice
    
    def __len__(self) -> int:
        return len(self.dice)
    
    def __getitem__(self, position: int) -> int:
        return self.dice(position)
    
    def __str__(self) -> str:
        print_data = ''
        for i in range(5):
            for die in self.dice:
                print_data +=dice_str[die][i] + ' '
            print_data += '\n'
        for num in range(len(self.dice)):
            print_data += f'    {num+1}    ' + ' '
        print_data += '\n'
        return print_data

    def choose_dice(self, dice: list) -> None:
        chosen = []
        for count, dice in enumerate(self.dice):
            if count in dice:
                chosen.append(dice)
                dice.remove()


if __name__ == '__main__':
    
    print('Dicematch!')
    player = dice_hand([random.randint(1, 6) for _ in range(5)])
    print(player)
    chosen_dice = input('score: ')
    player.choose_dice(chosen_dice.split())
    print(player)
    