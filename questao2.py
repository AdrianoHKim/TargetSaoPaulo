""" 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser
previamente definido no código;

OBS.:  Uma caracteristica essencial da sequencia Fibonacci é:

N é um numero fibonacci SE (5N^2 + 4) OU (5N^2 - 4) for um quadrado perfeito.
"""

import math

if __name__ == '__main__':
    def quadradoperfeito(num):
        # achando a raiz do numero
        s = int(math.sqrt(num))
        return s*s == num


    def numerofibonacci(n):
        # retorna verdadeiro se o numero esta na sequencia fibonacci ou retorna falso se nao estiver
        return quadradoperfeito(5*n*n + 4) or quadradoperfeito(5*n*n - 4)


    n = int(input("Informe o numero que deseja checar: "))
    if numerofibonacci(n):
        print("O numero informado esta na sequencia Fibonacci.")
    else:
        print(n, "nao e um numero Fibonacci.")
