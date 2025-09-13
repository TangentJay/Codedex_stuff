def scuffed_xor(wd, key):

    zug = ''

    Klen = len(key)

    for i, xyz in enumerate(wd):
        Kchar = key[i%Klen]

        zug += chr(ord(xyz) ^ ord(Kchar))

    return zug.encode('latin-1').hex()


xorr = scuffed_xor('Yoh!', 'key')
print(f'Hex: {xorr}')