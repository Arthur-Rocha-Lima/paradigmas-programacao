def soma(a,b):
    return a + b

# print(soma(3,4))
# print(soma(3,4))

def aplicar_duas_vezes(func, valor):
    return func(func(valor))

def incrementar(x):
    return x + 1

# print(incrementar(6))

print(aplicar_duas_vezes(incrementar, 6))