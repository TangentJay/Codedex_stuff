# CODedex/pyi/functional_programming/12hola2.py
'''
* Author: TanB
* Created: 8/10/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''

# CODedex/pyi/functional_programming/12hola2.py
def translator(language):
    translations = {'spanish': {'hello': 'hola', 'goodbye': 'adios', 'thank you': 'gracias'},
                    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
                    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'},
                    'german': {'hello' : 'hallo', 'goodbye' : 'tschüß', 'thank you' : 'danke'}}
    
    def translate_word(word):
        if word.lower() in translations[language]:
            return translations[language][word.lower()]
        else:
            return 'Translation not available'
        
    return translate_word

translate_2_german = translator('german')

print(translate_2_german('thank you'))
print(translate_2_german('hallo')) #error
print(translate_2_german('goodbye'))