from ConexaoBanco import *
from BuscaCep import *

continua = True
while (continua) :

    cep = str(input("Digite um cep válido\n"))

    if(len(cep) == 8):

        rs = ConexaoBanco.consultacep(ConexaoBanco,cep)

        encontrou = False
        for linha in rs:
            encontrou = True 

        if(not encontrou):
            bc = BuscaCep.getdadoscep(BuscaCep,cep)
            if(bc['erro'] == True):
                print('CEP não econtrado.')
                continue;

            ConexaoBanco.inserecep(ConexaoBanco, bc)
            rs = ConexaoBanco.consultacep(ConexaoBanco,cep)

        for linha in rs:
            print (linha)

        if(input("Para buscar mais ceps digite 1 e tecle enter\nPara sair do sistema digite qualquer outra coisa\n") != "1"):
            continua = False