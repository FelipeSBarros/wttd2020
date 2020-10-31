dados = {'nome': 'Felipe', 'idade': 36, 'sexo': 'Masculino'}
# pode-se usar o del para remover chave/valor, porque não quero mais
# e não preciso usar o valor de idade
del dados['idade']

# vou remover e quero usar o valor removido,
# então devo atribuir a uma variável,
# caso contrário, terá exatamente o mesmo comportamento de `del`
sexo = dados.pop('sexo')

# agora é possível usar a variável `sexo`