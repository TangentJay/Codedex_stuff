#11/8/2025
#croxxwords

grid = [['','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','','','',''],
        ['','','','','','']]

def display_grid():
    for row in grid:
        print(''.join(row))
(display_grid())

grid[1][0] = 'O'
grid[1][1] = 'o'
grid[1][2] = 's'
grid[1][3] = 'o'
grid[1][4] = 'd'
grid[1][5] = 'e'
#grid[1][6] = '|'
# grid[1][0] = 'O'
# grid[1][1] = 'o'
# grid[1][2] = 's'
# grid[1][3] = 'o'
# grid[1][4] = 'd'
# grid[1][5] = 'e'


clues = {
'oosode': 'ALL THAT IS', 'tanjay':'IS THAT IS ALL'
}

for word, clue in clues.items():
    print(f'Clue:{clue}')
    guess = input('Your guess:')

    if guess == word:
        print('Correct')
    else:
        print('Uno mas')

correct_guess = 0 

for word, clue in clues.items():
    print(f'Clue:{clue}')
    guess = input('Your guess: ')

    if guess==word:
        print('correct!!!1')
        correct_guess += 1
    else:
        print('go again')
if correct_guess==len(clues):
    print('Nice! you solved the xword puzzle!')
    quit()
else:
    print('Try again!')
    

