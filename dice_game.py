import curses
import random
import re
from pprint import pprint

dice_str: list = [
    ['┌───────┐',
     '│ Take  │',
     '│       │',
     '│ Score │',
     '└───────┘',],
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
smol_die = [['┌───┐',
             '│ X │',
             '└───┘',],
            ['┌───┐',
             '│ 1 │',
             '└───┘',],
            ['┌───┐',
             '│ 2 │',
             '└───┘',],
            ['┌───┐',
             '│ 3 │',
             '└───┘',],
            ['┌───┐',
             '│ 4 │',
             '└───┘',],
            ['┌───┐',
             '│ 5 │',
             '└───┘',],
            ['┌───┐',
             '│ 6 │',
             '└───┘',]]

def scoring_print(dice_values: list, description: str) -> str:
    print_data = ''
    for i in range(len(smol_die[0])):
        for die in dice_values:
            print_data +=smol_die[die][i]
        if i == 1:
            print_data += ' ' + description + '\n'
        else:
            print_data += '\n'
    return print_data.strip()

class Dice_Hand:

    def __init__(self, dice: list, max_busts: int = 5) -> None:
        self.dice = dice
        self.score = 0
        self.at_risk_score = 0
        self.max_busts = max_busts
    
    def __len__(self) -> int:
        return len(self.dice)
    
    def __getitem__(self, position: int) -> int:
        return self.dice(position)
    
    def __str__(self) -> str:
        print_data = ''
        display_dice = [0, *self.dice]
        for i in range(len(dice_str[0])):
            for die in display_dice:
                print_data +=dice_str[die][i] + ' '
            print_data += '\n'
        for num in range(len(display_dice)):
            print_data += f'    {num}    ' + ' '
        print_data += '\n'
        return print_data

    def choose_dice(self, dice: str) -> None:
        scoring_dice = []
        chosen_dice = list(re.sub(r'\D', '', dice))
        chosen_dice = set([int(i) for i in chosen_dice])
        for i in sorted(list(chosen_dice), reverse=True):
            scoring_dice.append(self.dice.pop(i-1))
        return scoring_dice
            
            

if __name__ == '__main__':
    
    print('''
DiceMatch!

Roll and choose dice to score.  
End your turn to collect the points.  
You bust if you roll dice and cannot score points.

Scoring:
''', end='')
    print(scoring_print([1], '10 points'))
    print(scoring_print([5], '50 points'))
    print(scoring_print([2,2,2], '3 of a kind: die value * 100'))
    print(scoring_print([3,3,3,3], '4 of a kind: die value * 500'))
    print(scoring_print([4,4,4,4,4], '5 of a kind: die value * 1000'))
    print(scoring_print([1,2,3,4], 'Small Straight: 1000 points'))
    print(scoring_print([2,3,4,5,6], 'Large Straight: 5000 points'))
    print()
    player = Dice_Hand([random.randint(1, 6) for _ in range(5)])
    print(player)
    chosen_dice = input('score: ')
    print(player.choose_dice(chosen_dice))
    print(player)

    # print(player)
    