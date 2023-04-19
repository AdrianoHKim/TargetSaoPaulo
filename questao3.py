""" 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;

b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
"""

import json


if __name__ == '__main__':
    # Carregar os dados do arquivo JSON (Supondo que o arquivo JSON esta na mesma pasta do script)
    with open('dados.json', 'r') as f:
        dados = json.load(f)

    # Filtrando os dias sem faturamento
    valor_filtrado = [d for d in dados if d['valor'] > 0]

    # Calculando os dias com maior e menor faturamento
    menor = min(valor_filtrado, key=lambda d: d['valor'])
    maior = max(valor_filtrado, key=lambda d: d['valor'])

    # Calculando a media de faturamento
    soma_valores = sum(d['valor'] for d in valor_filtrado)
    num_dias = len(valor_filtrado)
    media = soma_valores / num_dias

    # Calculando a quantidade de dias com faturamento acima da media
    dias_acima_da_media = sum(1 for d in valor_filtrado if d['valor'] > media)

    # Mostrando os resultados
    print(f"Menor valor faturado em um dia: R$ {menor['valor']} no dia {menor['dia']}")
    print(f"Maior valor faturado em um dia: R$ {maior['valor']} no dia {maior['dia']}")
    print(f"Media de faturamento diario: R$ {media:.2f}")
    print(f"Quantidade de dias com faturamento acima da media: {dias_acima_da_media}")
