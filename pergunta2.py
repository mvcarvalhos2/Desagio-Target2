def verificar_letra_a(string):
    string_lower = string.lower()
    
    contador_a = string_lower.count('a')
    
    if contador_a > 0:
        print(f"A letra 'a' aparece {contador_a} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

string = input("Digite uma string: ")
verificar_letra_a(string)
