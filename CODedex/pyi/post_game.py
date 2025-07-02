# Codedex_stuff/CODedex/pyi/post_game.py
'''
* Author: TanB
* Created: 7/1/2025
* Company: Oosode

'''

#Players that stood out to me. There is way to many and I know I am forgetting a lot of them.
Gladiators=[ {'name':'Michael Vick','position': 'QB', 'jersey': 7, 'career_passing_yards': 22464,'career_touchdowns': 234},
{'name':'Donovan McNabb', 'position': 'QB','jersey': 7,'career_passing_yards':22764,'career_touchdowns':133 },
{'name': 'Tom Brady', 'position': 'QB', 'jersey': 5, 'career_passing_yards':37276,'career_touchdowns': 234},
{'name':'Ricky Williams', 'position': 'RB', 'jersey': 34,'career_rushing_yards': 10236,'career_touchdowns': 66},
{'name': 'Deion Sanders', 'position': 'CB', 'jersey': 21, 'career_interceptions': 53, 'career_touchdowns': 22},
{'name': 'Emmitt Smith','position':'RB','jersey':22,'career_rushing_yards': 18355, 'career_touchdowns': 164 },
{'name': 'Chad Ochocinco', 'position': 'WR','jersey': 85, 'career_receiving_yards': 11594, 'career_touchdowns': 67},

]

Gladiators.append({'name': 'Aaron Rodgers', 'position': 'QB', 'jersey': 12,'career_passing_yards': 59855, 'career_touchdowns':475})

positions=[Gladiator['position'] for Gladiator in Gladiators ]
print('Players positions: ', positions)

for Gladiator in Gladiators:
    if Gladiator['name']=='Tom Brady':
        Gladiator['career_passing_yards']+= 69
        Gladiator['career_touchdowns'] += 4

print('Tom updated: ',Gladiators[2])

total_yards = sum(Gladiator.get('career_passing_yards', 0) for Gladiator in Gladiators) \
             + sum(Gladiator.get('career_rushing_yards', 0) for Gladiator in Gladiators) \
             + sum(Gladiator.get('career_receiving_yards', 0) for Gladiator in Gladiators)

print(f'Total combined yards for all players: {total_yards}')

total_touchdowns=sum(Gladiator['career_touchdowns']for Gladiator in Gladiators)

playerz=len(Gladiators)

avg_yards=total_yards/playerz
avg_td=total_touchdowns/playerz

print(f'Avg yrd:  {avg_yards}')
print(f'Avg td: {avg_td  }')