# projects/bot1.py

'''
* Author: TanB
* Created: 7/20/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

# Define the chatbot function which will handle all user input and output
def chatbot():
    
    print('Hi! I\'m BOB. Your best friend forever and ever!.')
    print('Ask me a question or type \'quit\' to exit.')  
   
    # We will start an infinite loop to keep the conversation going
    while True:
        
        user_input = input('You: ').lower().strip()

        
        if user_input in {'hi', 'hello', 'sup', 'yo'}:
            print('BOB: AYO, How can I help you?')

        
        elif 'name' in user_input:
            print('BOB: My nombre ist BOB. What\'s yours?')

        #  list the things the bot can do
        elif 'help' in user_input:
            print('BOB: I can chat, answer simple questions, or tell a joke.')

        # Joke response
        elif 'joke' in user_input:
            print('BOB: Why is Smite the best MOBA? Because it\'s got the best gods!')

        # 'quit' or 'q', to end the conversation and break the loop
        elif user_input == 'quit' or user_input == 'q':
            print('BOB: L8ter Gator.')  
            break  

        # If input doesn't match any known patterns, ask the user to try again
        else:
            print('BOB: PNO1 (Production Number 01), I\'m still Noob you, Boon. Doesn\'t compute... yet... Try again.')  # Fixed typo
        
# Call the chatbot function 
chatbot()
