# Regular expression
import re

# Match
re.match('abc', 'abc') # retorna match object
# span: posicao (indice) onde o padrao foi encontrado
# match: texto encontrado

re.match('abc', 'dabcz') # retorna None pq ele busca a str desde o início.

# Search

re.search('abc', 'dabcz')

# Find All

re.findall('abc', '123abc456abc789a')
