import requests
import json
import time
import logging
import sys

# Lista de símbolos das criptomoedas que você quer rastrear
# A chave é o símbolo que você usou (ex: 'BTC') e o valor é o nome da API da CoinGecko
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

# URL base da API da CoinGecko
API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Dicionário para armazenar os preços atuais
precos_atuais = {}

NFS_PATH = '/mnt/nas/precos_cripto.json'  # Caminho onde o NFS será montado no container

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)  # Apenas console
    ]
)

def obter_precos():
    """Função para obter os preços atuais das criptomoedas."""
    logging.info("Obtendo preços...")
    
    # Converte os nomes da API em uma string separada por vírgula
    nomes_para_api = ",".join(cripto_simbolos.values())

    # Parâmetros da requisição à API
    params = {
        'ids': nomes_para_api,
        'vs_currencies': 'usd'
    }

    try:
        # Faz a requisição HTTP para a API
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Lança um erro para status de erro (4xx ou 5xx)
        
        dados = response.json()
        
        # Preenche o dicionário com os dados
        for simbolo, nome_api in cripto_simbolos.items():
            if nome_api in dados and 'usd' in dados[nome_api]:
                precos_atuais[simbolo] = dados[nome_api]['usd']
                logging.info(f"Preço de {simbolo}: ${precos_atuais[simbolo]}")
            else:
                precos_atuais[simbolo] = 'Não encontrado'
                logging.info(f"Preço de {simbolo} não encontrado.")

    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição: {e}")

def salvar_json(dados):
    """Função para salvar os dados em um arquivo JSON no NFS."""
    try:
        with open(NFS_PATH, 'w') as f:
            json.dump(dados, f, indent=4)
        logging.info(f"Arquivo '{NFS_PATH}' atualizado com sucesso.")
    except IOError as e:
        logging.error(f"Erro ao salvar o arquivo: {e}")

def main():
    """Função principal que roda o script em loop."""
    # O loop vai rodar indefinidamente
    while True:
        obter_precos()
        salvar_json(precos_atuais)
        
        # Espera por 5 minutos (300 segundos) antes de rodar novamente
        logging.info("Aguardando 5 minutos...")
        time.sleep(300)

if __name__ == "__main__":
    main()
