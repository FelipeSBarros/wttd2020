from re import match, search, findall
# raw string
text = 'felipe\nbarros'
print(text)
# usando raw string
text = r'felipe\nbarros'
print(text)

# metacaracter | (usado como OU - or)
match('a|b', 'abc')
match('a|b', 'bcd')
match('a|b', 'cde')