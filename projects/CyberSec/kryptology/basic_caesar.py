def scuffed_caesar(txt, sft):


    pw =''
    for char in txt:
        if char.isalpha():
            start = 65 if char.isupper() else 97 #ASCII codes A =65, a =97

            pw += chr((ord(char) - start + sft ) %26 + start)

        else:
            pw += char
    return pw


txt = 'BobBx'
sft = 4
print(scuffed_caesar(txt,sft))

inKrypted = scuffed_caesar(txt, sft)
unKrypted = scuffed_caesar(txt, -sft)

print(f'Encrypted: {inKrypted}')
print(f'Decrypted: {unKrypted}')

