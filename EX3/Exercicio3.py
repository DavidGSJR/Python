import json
from statistics import mean

def carregar_dados(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

def analisar_faturamento(dados):
    faturamento_valido = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    media_mensal = mean(faturamento_valido)
    
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

arquivo_json = 'faturamento.json'

try:
    dados_faturamento = carregar_dados(arquivo_json)
    
    menor, maior, dias_acima = analisar_faturamento(dados_faturamento)
    
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{arquivo_json}' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")