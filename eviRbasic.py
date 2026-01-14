

with open('eviR.txt', 'w') as e:
    e.write('ayoh! 11/25/2025')


with open('eviR.txt','r') as e:
    content = e.read()
    print(content)
