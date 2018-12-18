# Debugged. Works Ok.
def bin_encrypt(s):  # binary cipher encrypt function
    st = s.split()
    ciph = []
    for word in st:
        for letter in word:
            ciph.append(bin(ord(letter))[2:])
    return ' '.join(ciph)


# Debugged. Works Ok.
def bin_decrypt(s):  # binary cipher decrypt function
    st = s.split()
    enc = ''
    for n in st:
        enc += chr(int(n, 2))
    return enc