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

# Repeticoes
# Quantidades esécificas

match(r'\d{4}', '1234')
# o match só funciona ao encontrar a quantidade especificada:
match(r'\d{4}', '123')
match(r'\d{4}', '12345')

# repeticoes gananciosas (retornarao o minimo e além do mesmo.
# encontrando ao menos dois
match(r'\d{2,}', '12')
match(r'\d{2,}', '1223456')
# Mas se a string nao possui o minimo necessario ele retorna None
match(r'\d{2,}', '1')
# repeticoes preguicosas (retornarao apenas o minimo caso ele seja encontrado)
# Basta adicionar uma interrogacao apos a chave
match(r'\d{2,}?', '123456')

# Minimo e maximo de repeticoes
# Para limitar o inimo e maximo basta adicionar dois valoes internos as chaves separados por virgula para cada valor respectivo.
match(r'\d{2,4}', '123456')
match(r'\d{2,4}', '12')
match(r'\d{2,4}?', '123456') # encontrando o minimo possivel

# quando temos um elemento opcional
match(r'\d{0,1}', '12345')
match(r'\d{,1}', '12345')
# Modificiador de repeticao e repete o que vem antes
match(r'\d?', '12345') # seria o mesmo que o anterior. A interrogacao indica 0 ou um da sequencia
# preguicoso: minimo possivel
match(r'\d{0,1}?', '12345')
match(r'\d??', '12345') # seria o mesmo que o anterior . A primeira interrogacao indica 0 ou 1 e a
# segunda interrogacao o transforma em minimo possivel. É o modificador do operador de repeticao o transofrmando em preguicoso

# 0 ou mais vezes
match(r'\d{0,}', '')
match(r'\d{0,}', '12345')
match(r'\d*', '') # asterisco indica 0 ou mais vezes
match(r'\d*?', '12345') # transformando em preguicoso

# Uma ou mais vezes
match(r'\d{1,}', '12345')
match(r'\d+', '12345') # operador + exigindo no minimo uma ocorrencia
match(r'\d+', 'abc')
match(r'\d+?', '123456') # transformando em preguicoso

# exemplo importancia repeticoes preguicosas
text = 'attr1="value1" attr2="value2"'
# buscando valores dos atributos. Os mesmos estao entre aspas.
findall(r'".+"', text) # mas o re vai buscar a partir da primeira aspas até a ultima como se fosse uma coisa so.
findall(r'".+?"', text) # Agora, sim!

# Match object
m = match(r'\d+', '12345')
type(m)
m.start()
m.end()
m.span() # slice do valor encontrado
# quando nao encontrado, se retorna None.

# extraido informacoes com re:
html = '<input type="text" id="id_cpf" name="cpf">'
pattern = r'<(.+?) type="(.+?)" id="(.+?)" name="(.+?)"' # parenteses para definir grupos de identificacao
m = match(pattern, html)
m
m.groups() # NO PLURAL!
m.group(0) # retorna tudo
m.group(1)
m.group(1,3)

# generalizando o pattern

html2 = '<input id="id_cpf" name="cpf" type="text">'
# Vamos adicionar um grupo de nao captura
pattern = r'<(.+?) (?:(?:type="(.+?)"|id="(.+?)"|name="(.+?)") ?)*' # parenteses com interrogacao e dois pontos para gerar grupo de nao captura
m = match(pattern, html)
m
m = match(pattern, html2)
m.groups() # as ordens dos grupos sao definidas pelo python  seguindo a ordem definida no pattern

# named group
pattern = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|id="(?P<id>.+?)"|name="(?P<name>.+?)") ?)*' # ?P<tag> para deifnir grou name
m = match(pattern, html2)
m.groups()
m.groupdict() # surge com o named group