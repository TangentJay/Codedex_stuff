# CODedex/list_packs/dna.py
'''
* Author: TanB
* Created: 7/6/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
#DNA
# We will make a list of dna sequence
dna_sequence=['GCT','AGC', 'AGG', 'TAA','ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA','ACC','GGA']

item_to_find=['CCC','CAT']

item_found=False

for i in dna_sequence:
    if i in item_to_find:
        item_found=True

if item_found:
    print('item found!')
else:
    print('Item not hier!')

