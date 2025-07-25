# projects/minigame3.py
'''
* Author: TanB
* Created: 7/19/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

# Welcome message
print('=== AFRICAN ADVENTURE ===')

# Using strip and title to make it look cleaner
name = input('What\'s your name, traveler? ').strip().title()

print(f'\nWelcome {name}! You just won a free trip through Africa.')
print('Each place is full of surprises, so choose wisely!\n')

# ask user if they are ready
ready = input('Ready to plan your African adventure? (yes/no): ').strip().lower()

if ready == 'yes' or ready == 'y':
    # First stop: pick a country
    print('\nYour first stop!')
    print('1 - Egypt (pyramids + desert)')
    print('2 - Kenya (safari + animals)')

    country = input('Choose where to begin (1 or 2): ').strip()

    if country == '1':
        print('\nYou’re in Egypt! Teh pyramids are huge.')
        print('Two tour options:')
        print('A - Ride camels in teh desert')
        print('B - Cruise teh Nile River')

        tour = input('Pick your tour (A/B): ').strip().upper()

        if tour == 'A':
            print('\nYou find a hidden tomb! It’s named after you. You\'re FAMOUS now!')
        elif tour == 'B':
            print('\nYou help save a goat and become an honorary village elder. LEGEND status!')
        else:
            print('\nYou waited too long and missed both tours. Back to teh hotel!')

    elif country == '2':
        print('\nWelcome to Kenya! Time for a wild safari.')
        print('A - Masai Mara (lions + wildebeests)')
        print('B - Amboseli (elephants + Kilimanjaro views)')

        safari = input('Pick your safari (A/B): ').strip().upper()

        if safari == 'a':
            print('\nYou snap amazing lion photos. Nat Geo buys them. New career unlocked!')
        elif safari == 'b':
            print('\nYou bond with a baby elephant. It’s named after you.!')
        else:
            print('\nYou chill at teh lodge. Food\'s good at least!')

    # Second leg of teh trip
    print('\nNext stop on your trip:')
    print('3 - Morocco (markets + mountains)')
    print('4 - South Africa (city + ocean)')

    next_country = input('Where to now? (3 or 4): ').strip()

    if next_country == '3':
        print('\nYou\'re in Morocco! Teh market is wild and colorful.')
        item = input('Do you buy a magic lamp or a leather bag? (lamp/bag): ').strip().lower()

        if item == 'lamp':
            print('\nYou get 3 wishes! Teh genie hooks you up with unlimited travel.')
        elif item == 'bag':
            print('\nYou learn leather crafting and start a business. Nice hustle!')
        else:
            print('\nYou couldn’t decide and teh market closed. Maybe next time!')

    elif next_country == '4':
        print('\nNow in Cape Town! Teh views are amazing.')
        activity = input('Hike Table Mountain or visit penguins? (hike/penguins): ').strip().lower()

        if activity == 'hike':
            print('\nYou find a brand-new flower. It’s named after you!')
        elif activity == 'penguins':
            print('\nYou rescue an oil-covered penguin. Teh aquarium gives you a job!')
        else:
            print('\nYou chill on teh beach. Sometimes relaxing is perfect too.')

    else:
        print('\nThat’s not a real option! Teh plane is stuck waiting for you to decide.')

else:
    print('\nNo worries! Come back when you’re feeling more adventurous. Karibu tena!')

# Ending message
print('\n=== SAFARI NJEMA! (Have a good journey!) ===')
print('Play again and explore more African wonders!')
