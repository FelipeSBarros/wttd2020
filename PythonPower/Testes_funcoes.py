
# -*- coding: utf-8 -*-

def f1(a, b, c):
    print( a, b, c)
    
print("teste f1")
f1(a='A', b='B', c='C')

def f2(a, b, c, *args):
    print( a, b, c, args)

print("teste f2")
f2('A', 'B', 'C', 'Arg1', 'Arg2')
f2('A', 'B', 'C', 'Arg1', 'Arg2')

def f2_2(*args, a, b, c): # parametros posicionais devem vir antes dos nominais
    print( a, b, c, args)

print("teste f2_2")
f2_2('Arg1', 'Arg2', a='A', b='B', c='C')

def f3(a, b, c, **kwargs):
    print( a, b, c, kwargs)

print("teste f3")
f3('A', b='B', c='C', z='args', y='wargs2')
f3(a='A', b='B', c='C', d='args', e='wargs2')

def f4(a, b, c, *args, **kwargs):
    print( a, b, c, args, kwargs)

print("teste f4")
f4('A', 'B', 'C', 'D', 'E', z='Z', w='W')

def f4_2(*args, a, b, c, **kwargs):
    print(args, a, b, c, kwargs)

print("teste f4_2")
f4_2('args', 'args', a='A', b='B', c='C', z='Z', w='W')