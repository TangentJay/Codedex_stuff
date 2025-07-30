# CODedex/pyi/fileHandling/07pt2.py
'''
* Author: TanB
* Created: 7/26/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#

with open('Ello.txt', 'r') as b:
    print(b.read())
#dictionary
liked_games = {'MMO1' : 'FFXI', 'MMO2' :'WOW', 'RPG1':'FFX',
               'RPG2': 'FFXIII series'
}

def write_liked_games_2_file(liked_games, file_name):
    with open('gamez.txt','w') as f:
        f.write('Likedd games:\n')
        for game_type, game_name in liked_games.items():
            f.write(f'{game_type}: {game_name}\n')


    print(f'Added to games to {file_name}')



write_liked_games_2_file(liked_games, 'gamez.txt')



with open('gamez.txt','r') as g:
    print(g.read())