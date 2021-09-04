from ConexaoBanco import *
from BuscaCep import *

cep = input("Digite o cep\n")

rs = ConexaoBanco.consultacep(ConexaoBanco,cep)

encontrou = False
for linha in rs:
    encontrou = True

if(not encontrou):
    bc = BuscaCep.getdadoscep(BuscaCep,cep)
    ConexaoBanco.inserecep(ConexaoBanco, bc)
    rs = ConexaoBanco.consultacep(ConexaoBanco,cep)

for linha in rs:
  print (linha)

