# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable userWord.
a = ""
userWord = input('ingresa una palabra: ')
userWord = userWord.upper()
vocales = ['A','E','I','O','U',]
for letra in userWord: #W I L L I A M
    if letra in vocales: #in se usa para verificar si un elemento en un vector
        continue
    a = a+letra
print(a)

# for letra in userWord:
#     if letra == 'A':
#        continue
#     elif letra == 'E':
#         continue
#     elif letra == 'I':
#         continue
#     elif letra == 'O':
#         continue
#     elif letra == 'U':
#         continue
#     else:
#         print(letra)