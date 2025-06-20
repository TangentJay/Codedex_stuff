# Write code below 💖 6/17/2025


class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        
    def speak(self):
        print(2*f"{self.name}!")
    
    def display_details(self):
        print(f'Entry number: {self.entry}')
        print(f'Name: {self.name}')
    
        if len(self.types) == 1:
            print(f'Type: {self.types[0]}')
        else:
            print(f'Types: {", ".join(self.types)}')
        
        print(f'Description: {self.description}')
    
        if self.is_caught:
            print(f'{self.name} is a duplicate')
        else:
            print(f'{self.name} has not been caught')

# Create Pokémon
pikachu = Pokemon(
    entry=25, 
    name='Pikachu', 
    types=['Electric ⚡'], 
    description='It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.',
    is_caught=True
)

ninjask = Pokemon(
    entry=291, 
    name='Ninjask', 
    types=['Bug', 'Flying'], 
    description='Ninjask is known for its speed. It is said to be nearly invisible due to its lightning-fast movements.',
    is_caught=False
)

misdreavus = Pokemon(
    entry=200, 
    name='Misdreavus', 
    types=['Ghost'], 
    description="If you hear a sobbing sound emanating from a vacant room, it's undoubtedly a bit of mischief from Misdreavus.",
    is_caught=True
)


print("Pokédex Entries:")
print("================")

pikachu.speak()
pikachu.display_details()

ninjask.speak()
ninjask.display_details()

misdreavus.speak()
misdreavus.display_details()