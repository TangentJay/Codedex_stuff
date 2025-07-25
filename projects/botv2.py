# projects/botv2.py
'''
* Author: TanB
* Created: 7/21/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricorn'
    else:
        return None


horoscope_messages = {
'Aries': 'Burn everything down and rise from the ashes. Today, you don’t just lead—you obliterate the competition.',
'Taurus': 'The world will try to rattle your cage, but you stay unshaken. Own your calm, you’re a fortress.',
'Gemini': 'You’ve got a mouth that can burn bridges or build kingdoms. Speak like a king, but listen like a shadow.',
'Cancer': 'Stop hiding behind your shell. Your power lies in your vulnerability, let it consume you.',
'Leo': 'You don’t just take the spotlight—you become it. Shine so bright that they can’t look away, even if they try.',
'Virgo': 'Analyze. Destroy. Rebuild. Your brain is a weapon—don’t let anyone dull its edge.',
'Libra': 'Balance is a lie. There’s only power. Choose your side, and don’t hesitate to break the scales if needed.',
'Scorpio': 'We walk through minefields and never flinch. You were born from chaos, and it’s the only thing you understand.',
'Sagittarius': 'Throw yourself into the abyss and see if it catches you. The world doesn’t scare you—it’s your playground.',
'Capricorn': 'Slow and steady wins the race—but you’re not racing, you’re taking over. Don’t stop until the world bends to you.',
'Aquarius': 'You’re not just ahead of the curve, you’re bending reality itself. Make them question what’s possible.',
'Pisces': 'You dream in colors they’ll never understand. Turn those dreams into chaos—make them real, make them yours.'

}

# -----------------------------
# Main Chatbot Function
# -----------------------------
def chatbot():
    print('Hi! I\'m BOB. Your best friend forever and ever!.')
    print('Ask me a question or type \'quit\' to exit.')  

    while True:
        # Ask the user for input and normalize it
        user_input = input('You: ').lower().strip()

        # Greeting
        if user_input in {'hi', 'hello', 'sup', 'yo'}:
            print('BOB: AYO, How can I help you?')

        # Bot's name
        elif 'name' in user_input:
            print('BOB: My nombre ist BOB. What\'s yours?')

        # List capabilities
        elif 'help' in user_input:
            print('BOB: I can chat, answer simple questions, tell a joke, or give your zodiac sign!')

        # Joke response
        elif 'joke' in user_input:
            print('BOB: Why is Smite the best MOBA? Because it\'s got the best gods!')

        # Horoscope logic
        elif 'horoscope' in user_input or 'zodiac' in user_input:
            try:
                month = int(input('BOB: What\'s your birth month (1–12)? '))
                day = int(input('BOB: And what day? '))
                sign = get_zodiac_sign(month, day)
                if sign:
                    message = horoscope_messages.get(sign, '')
                    print(f'BOB: You\'re a {sign}! {message}')
                else:
                    print('BOB: Hmmm, that date doesn\'t look right...')
            except ValueError:
                print('BOB: Yo, numbers only please.')

        # Exit
        elif user_input == 'quit' or user_input == 'q':
            print('BOB: L8ter Gator.')  
            break  

        # Fallback for unknown input
        else:
            print('BOB: PNO1 (Production Number 01), I\'m still Noob you, Boon. Doesn\'t compute... yet... Try again.')  

# -----------------------------
# Start the chatbot
# -----------------------------
chatbot()
