import json
import requests


# Classe criada para comportar os códigos relativos á busca de cep

class BuscaCep(object):

    # Método que busca através de uma requisição get no portal do viacep os dados relacionados ao cep digitado

    def getdadoscep(self, cep):
        url = ('http://www.viacep.com.br/ws/%s/json' % cep)
        tnc = {'chave':'parametro','chave2':'parametro2'}
        requisicao = requests.get(url,tnc)
        if requisicao.status_code == 200:
            dados_json = json.loads(requisicao.text)
            return dados_json