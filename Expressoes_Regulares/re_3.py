from re import match, search, findall
# classes de caracter sao os cracteres dentro de colchetes
findall('[aeiou]', 'Felipe Barros') # perceber que ele esta buscando cada uma das opcoes da classe de caracteres e não a sequencia em si!
# classe de caracteres com negacao: basta adicionar no inicio a ancora ^
# Case sensitive!
findall('[^aeiou]', 'Felipe Barros')

# usando range
findall('[a-f]', 'Felipe Barros')
findall('[A-F]', 'Felipe Barros')
# definindo Maiuscula e mais de um range

findall('[a-fA-F]', 'Felipe Barros')

# sequencias especiais
findall('[\w]', 'Felipe Barros') # seria o mesmo que [a-zA-Z0-9_]
# E nao precisa estar como uma classe de caracter
findall('\w', 'Felipe Barros')

# sequecias especiais:
# \d == [0-9]
# \D == [^0-9] # Negacao!
# \s == [\t\n\r\f\v]
# \S == [^\t\n\r\f\v] # Negacao!
# \w == [a-zA-Z0-9_]
# \W == [^a-zA-Z0-9_] # Negacao!
