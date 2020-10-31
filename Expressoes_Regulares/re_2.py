from re import match, search, findall

# explorando o meta caracter '.' = qualquer caracter

match('.', 'abc')

match('.', '012')

match('.', ' ')

match('.', '\t\t')

match('.', '\n')# retorna None por se quebra de linha. nao e caracter

# Para o search o \n tbm nao e caracter, por isso ele segue buscando qualquer caracter seguinte ao \n
search('.', '\nas')

findall('.', 'abc')

# Ancoras ^$ inicio e fim de string

findall('^.', 'abc\nmbs\nebc') # busca por caracteres no inicio da primeira linha

findall('^.', 'abc\nabs\nebc', re.MULTILINE) # busca por caracteres de primeira linha para varias linhas diferentes

findall('.$', 'abc\nabs\nebc') # retorna caracter que esteja no fim da string

findall('.$', 'abc\nabs\nebc', re.MULTILINE) # retorna ultimos caracter que esteja no fim de cada linha

# usando ^e $
findall('^.$', 'abc\nabs\nebc') # retorna None pq ele esta buscando um caracter que seja ao mesmo tempo inicio e fim da string

findall('^.$', 'a')

match('^$', '') # unica forma do inicio encontrar o final e quando nao ha caracter entre eles.

findall('^$', '\n', re.MULTILINE) #Mostra que a quebra de linha \n nao é entendida como um caracter. alem disso retornam duas strings vazias mostrando a quebra de linha