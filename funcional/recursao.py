# RECURSÃO

# def fatorial(numero):
#     if numero == 0:
#         return 1
#     return numero * fatorial(numero - 1)

# print(fatorial(4))

# FIBONACCI DE 6

def fibonacci(numero):

    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-2) + fibonacci(numero - 1)

print(fibonacci(6))