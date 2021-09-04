import postgresql


# Classe criada para comportar os códigos relativos ao acesso ao banco de dados

class ConexaoBanco(object):

    # Conexão com o banco de testes criado localmente
    _db = postgresql.open("pq://admin:admin@localhost/teste")

    # Método generico com a função de executar buscas ao banco de dados

    def consulta(self,sql):
        rs = None
        try:
            rs = self._db.prepare(sql)
        except Exception as e:
            print(e)
            return None
        return rs

    # Método generico com a função de executar alterações no banco de dados

    def executa(self,sql):
        try:
            self._db.execute(sql)
        except:
            return False;
        return True;

    # Método criado para realizar a consulta pelo cep na tabela de localização

    def consultacep(self,cep):
        return self.consulta(self,""" select * from localizacao where cep = '%s' """ %cep)

    # Método que recebe o json do retorno da busca por cep na api do viacep e monta o insert

    def inserecep(self,json):
        cep = json['cep']

        for char in cep:
            if char in "-":
                cep = cep.replace(char, '')

        query = ('insert into localizacao values (default, \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'
                 %(cep,json['localidade'],json['uf'],json['ibge'],json['ddd'],json['siafi']))
        self.executa(self,query)

