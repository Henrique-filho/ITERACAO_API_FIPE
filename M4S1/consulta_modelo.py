#ATIVIDADE M4S1:
#ITERANDO DADOS DA API https://deividfortuna.github.io/fipe/ COLSULTANDO TIPOS DE VEICULOS DE UMA DETERMINADA MARCA.
import requests

from classes_consulta import Marca 
from classes_consulta import Veiculo

consulta_fipe = Marca()

marcas = consulta_fipe.obter_todas_marcas()
for marca in marcas:
    print(f"ID da Marca: {marca['codigo']} - Nome da Marca: {marca['nome']}")

class Fipe:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.url_modelos = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos'
        self.headers = {'user-agent': 'Consulta-fipe'}
        self.modelos = self._get_modelos()

    def _get_modelos(self):
        resposta = requests.get(self.url_modelos, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json().get('modelos', [])
        return[]
        
    def __iter__(self):
        self.indice = 0
        return self
    
    def __next__(self):
        if self.indice < len(self.modelos):
            modelo = self.modelos[self.indice]
            self.indice += 1
            return {
                'ID': modelo.get('codigo'),
                'NOME': modelo.get('nome')
            }
        else:
            raise StopIteration
        

selecionar_marca = input("Digite o ID da marca que deseja consultar:")
marca_selecionada = selecionar_marca
iterador = Fipe(marca_selecionada)

for modelo in iterador:
    print(f"ID: {modelo['ID']} - Nome: {modelo['NOME']}")


from classes_consulta import Modelo

consulta = Modelo()
id_veiculo = input('Digite o ID do veículo desejado: ')
consulta.atributo_modelo(id_veiculo)




