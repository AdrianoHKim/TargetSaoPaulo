""" 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
 
"""


import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Faturamento mensal por estado
    faturamento_mensal = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    # Calculando o faturamento total
    faturamento_total = sum(faturamento_mensal.values())

    # Calculando a representacao porcentual de cada estado
    porcentagens = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_mensal.items()}

    # Resultado das porcentagens
    for estado, percentage in porcentagens.items():
        print(f"{estado}: {percentage:.2f}%")

    # Gerando opcao para mostrar um grafico
    mostrar_grafico = input("Deseja vizualizar o resultado em um grafico? (s/n) ").lower() == 's'
    if mostrar_grafico:
        # Criando o grafico
        plt.pie(porcentagens.values(), labels=porcentagens.keys(), autopct='%1.1f%%')
        plt.title("Representacao percentual de cada estado: ")
        plt.show()
