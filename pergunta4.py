def completar_a():
    sequencia = [1, 3, 5, 7]
    proximo = sequencia[-1] + 2 
    return proximo

def completar_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo = sequencia[-1] * 2  
    return proximo

def completar_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo = len(sequencia) ** 2  
    return proximo

def completar_d():
    sequencia = [4, 16, 36, 64]
    proximo_numero = (len(sequencia) * 2 + 2) ** 2  
    return proximo_numero

def completar_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo = sequencia[-1] + sequencia[-2]  
    return proximo

def completar_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1  
    return proximo

print(f"a) 1, 3, 5, 7, ___ -> {completar_a()}")
print(f"b) 2, 4, 8, 16, 32, 64, ____ -> {completar_b()}")
print(f"c) 0, 1, 4, 9, 16, 25, 36, ____ -> {completar_c()}")
print(f"d) 4, 16, 36, 64, ____ -> {completar_d()}")
print(f"e) 1, 1, 2, 3, 5, 8, ____ -> {completar_e()}")
print(f"f) 2,10, 12, 16, 17, 18, 19, ____ -> {completar_f()}")
