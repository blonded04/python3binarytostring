def bin_encrypt(string):
	st=string.lower()
	keys='a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 { } ; , . [ ] ( )'
	keys.split()
	values='1100001 100000 1100010 100000 1100011 100000 1100100 100000 1100101 100000 1100110 100000 1100111 100000 1101000 100000 1101001 100000 1101010 100000 1101011 100000 1101100 100000 1101101 100000 1101110 100000 1101111 100000 1110000 100000 1110001 100000 1110010 100000 1110011 100000 1110100 100000 1110101 100000 1110110 100000 1110111 100000 1111000 100000 1111001 100000 1111010 100000 110001 100000 110010 100000 110011 100000 110100 100000 110101 100000 110110 100000 110111 100000 111000 100000 111001 100000 110000 1111011 100000 1111101 100000 111011 100000 101100 100000 101110 100000 1011011 100000 1011101 100000 101000 100000 101001'
	values.split()
	table={}
	ciph=''
	for i in range(len(keys)):
		table[keys[i]]=values[i]
	for j in st:
		if j in table:
			ciph += table[j]
		else:
			ciph += '-UnknownSymbol-'
	return ciph


def bin_decrypt(string):
	st=string.split()
	values='a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 { } ; , . [ ] ( )'
	keys.split()
	keys='1100001 100000 1100010 100000 1100011 100000 1100100 100000 1100101 100000 1100110 100000 1100111 100000 1101000 100000 1101001 100000 1101010 100000 1101011 100000 1101100 100000 1101101 100000 1101110 100000 1101111 100000 1110000 100000 1110001 100000 1110010 100000 1110011 100000 1110100 100000 1110101 100000 1110110 100000 1110111 100000 1111000 100000 1111001 100000 1111010 100000 110001 100000 110010 100000 110011 100000 110100 100000 110101 100000 110110 100000 110111 100000 111000 100000 111001 100000 110000 1111011 100000 1111101 100000 111011 100000 101100 100000 101110 100000 1011011 100000 1011101 100000 101000 100000 101001'
	values.split()
	table={}
	enc=''
	for i in range(len(keys)):
		table[keys[i]]=values[i]
	for j in st:
		if j in table:
			enc += table[j]
		else:
			enc += ('-UnknownSymbol-:'+j)
	return enc