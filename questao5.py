""" 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua
 preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

string = input("Escreva uma palavra: ")
string_reversa = ""

# Invertendo os caracteres
for i in range(len(string)-1, -1, -1):
    string_reversa += string[i]

print("Palavra invertida:", string_reversa)
