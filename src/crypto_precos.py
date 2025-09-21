import requests
import json
import time

cripto_simbolos = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'SOL': 'solana',
    'AAVE': 'aave',
    'LINK': 'chainlink',
    'SUI': 'sui',
    'ARB': 'arbitrum',
    'LDO': 'lido-dao',
    'AVAX': 'avalanche-2',
    'XRP': 'ripple'
}

API_URL = "https://api.coingecko.com/api/v3/simple/price"

precos_atuais = {}

def obter_precos():
    print("Obtendo preços...")
    
    nomes_para_api = ",".join(cripto_simbolos.values())

    params = {
        'ids': nomes_para_api,
        'vs_currencies': 'usd'
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        
        dados = response.json()
        
        for simbolo, nome_api in cripto_simbolos.items():
            if nome_api in dados and 'usd' in dados[nome_api]:
                precos_atuais[simbolo] = dados[nome_api]['usd']
                print(f"Preço de {simbolo}: ${precos_atuais[simbolo]}")
            else:
                precos_atuais[simbolo] = 'Não encontrado'
                print(f"Preço de {simbolo} não encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

def salvar_json(dados):
    try:
        with open('/mnt/nas/precos_cripto.json', 'w') as f:
            json.dump(dados, f, indent=4)
        print("Arquivo 'precos_cripto.json' atualizado com sucesso.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

def main():
    while True:
        obter_precos()
        salvar_json(precos_atuais)
        
        print("Aguardando 5 minutos...")
        time.sleep(300)

if __name__ == "__main__":
    main()