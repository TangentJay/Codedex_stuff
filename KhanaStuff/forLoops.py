for j in range(4,20,3):
    print (j)  # for loop version




j = 4
while j < 20:
    print(j)
    j += 3  #while loop version 
    

balance = 500
interest_rate = .04 
years = 4


for month in range(years * 12):
    print(f'current year es: {years}')
    interest = balance * interest_rate
    balance = round(balance + interest, 2)
    print(f'current balance es {balance}')
    years += 4


pat = 0
while pat <5:
    print('][][][][][')
    print('][][][][][')
    pat += 1
print('00000000')
for patt in range(5):
    print('][][][][][')
    print('][][][][][')

