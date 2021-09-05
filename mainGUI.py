from tkinter import *
from ConexaoBanco import *
from BuscaCep import *

def checaCep(cepFormatado):
    rs = ConexaoBanco.consultacep(ConexaoBanco, cepFormatado)

    encontrou = False
    for linha in rs:
        encontrou = True

    if (not encontrou):
        bc = BuscaCep.getdadoscep(BuscaCep, cepFormatado)

        ConexaoBanco.inserecep(ConexaoBanco, bc)
        rs = ConexaoBanco.consultacep(ConexaoBanco, cepFormatado)

    for linha in rs:
        localidade['text'] = linha['localidade']
        UF['text'] = linha['uf']
        ibge['text'] = linha['ibge']
        ddd['text'] = linha['ddd']
        siafi['text'] = linha['siafi']

janela = Tk()

janela.title("Busca por CEP")

janela.geometry("300x250")
janela.resizable(False,False)
janela.iconbitmap("images/mapa.ico")
janela['bg'] = "pink"

texto = Label(janela, text="Digite o cep", bg="pink", fg="black")
texto.grid(column=0, row=0, padx=10, pady=10)

cep = Entry(janela)
cep.grid(column=1, row=0, padx=10, pady=10)
cep.focus()

botao = Button(janela, text="Buscar", command=lambda: checaCep(cep.get()))
botao.grid(column=2, row=0, padx=10, pady=10)

texto_localidade = Label(janela, text="Localidade", bg="pink")
texto_localidade.grid(column=0, row=1, padx=10, pady=10)

localidade = Label(janela, text="", bg="pink")
localidade.grid(column=1, row=1, padx=10, pady=10)

texto_UF = Label(janela, text="UF", bg="pink")
texto_UF.grid(column=0, row=2, padx=10, pady=10)

UF = Label(janela, text="", bg="pink")
UF.grid(column=1, row=2, padx=10, pady=10)

texto_ibge = Label(janela, text="IBGE", bg="pink")
texto_ibge.grid(column=0, row=3, padx=10, pady=10)

ibge = Label(janela, text="", bg="pink")
ibge.grid(column=1, row=3, padx=10, pady=10)

texto_ddd = Label(janela, text="DDD", bg="pink")
texto_ddd.grid(column=0, row=4, padx=10, pady=10)

ddd = Label(janela, text="", bg="pink")
ddd.grid(column=1, row=4, padx=10, pady=10)

texto_siafi = Label(janela, text="SIAFI", bg="pink")
texto_siafi.grid(column=0, row=5, padx=10, pady=10)

siafi = Label(janela, text="", bg="pink")
siafi.grid(column=1, row=5, padx=10, pady=10)

janela.mainloop()
