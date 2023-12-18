#!C:\Users\HenriqueFilho\Desktop\M4S1\.venv\Scripts\... 
import requests

class Marca:
    def __init__(self):
        self.url_marcas = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
        self.url_modelos = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos'
        self.headers = {'user-agent': 'Consulta-fipe'}
        self.marcas = self._get_marcas()

    def _get_marcas(self):
        resposta = requests.get(self.url_marcas, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json()
        return []

    def _get_modelos(self, marca_id):
        url_modelos = self.url_modelos.format(marca_id)
        resposta = requests.get(url_modelos, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json().get('modelos', [])
        return []

    def obter_todas_marcas(self):
        return self.marcas

    def obter_modelos_por_marca(self, marca_id):
        return self._get_modelos(marca_id)
    

class Veiculo:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.url_modelos = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos'
        self.headers = {'user-agent': 'Consulta-FIPE'}
        self.modelos = self._get_modelos()

    def _get_modelos(self):
        resposta = requests.get(self.url_modelos, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json().get('modelos', [])
        return []

    def get_modelos(self):
        return self.modelos
    

class Modelo:
    def __init__(self):
        self.url_base = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
        self.headers = {'user-agent': 'Consulta-fipe'}

    def atributo_modelo(self, veiculo_id):
        url_veiculo = f'{self.url_base}veiculos/{veiculo_id}'
        print("URL do Veículo:", url_veiculo)
        resposta = requests.get(url_veiculo, headers = self.headers)
        if resposta.status_code == 200:
            dados_veiculo = resposta.json()
            print("Dados do Veículo:")
            print(f"ID: {dados_veiculo['codigo']}")
            print(f"Nome: {dados_veiculo['nome']}")
            print(f"Ano: {dados_veiculo['ano']}")
            print(f'Marca: {dados_veiculo["marca"]["nome"]}')
            print(f'Modelo: {dados_veiculo["modelo"]["nome"]}')
        else: 
            print("classe com defeito"), resposta.status_code 

   