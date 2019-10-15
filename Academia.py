#Programa de Academia

#IMPORTA A INTERFACE GRAFICA E ARQUIVOS
from tkinter import *
import os

janela_principal = Tk()
janela_principal.title("SOFT GYM EVOLULION X")


#VERIFICA SE O ICONE ESTÀ NA PASTA E MOSTRA SE TRUE
if(not os._exists('treino128x128.ico')):
    janela_principal.iconbitmap('treino128x128.ico')


#DADOS DO USUARIO PADRÃO
nome = "JOAO".upper()

Senha = str(123456)
idade = 32
sexo = "MASCULINO"
altura = 1.75
peso = 71
biceps_direito = 28.25
biceps_esquerdo = 28.25
coxa_direita = 50.25
coxa_esquerda = 50.25
antibraco_direito = 25.50
antibraco_esquerdo = 25.50
panturrilha_direita = 32
panturrilha_esquerda = 33.50
abdomen = 86
cintura = 50
quadril = 40
torax = 94
ombro = 103

#FUNÇÃO SENHA#


#MENU 1CADASTRO USUARIO#


def Janela_Cadastro():
    Janela_Cadastro = Tk()
    Janela_Cadastro.title("CADASTRO USUARIO")

    # VERIFICA SE O ICONE ESTÀ NA PASTA E MOSTRA SE TRUE
    if (not os._exists('treino128x128.ico')):
        janela_principal.iconbitmap('treino128x128.ico')

    Janela_Cadastro.geometry("500x500")

    Frame_Direito = Label(Janela_Cadastro)
    Frame_Direito.pack(side=RIGHT)

    Frame_Esquerdo = Label(Janela_Cadastro)
    Frame_Esquerdo.pack(side=LEFT)

    Label(Frame_Esquerdo, text="NOME: ").pack()
    Nome = Entry(Frame_Esquerdo)
    Nome.pack()

    Label(Frame_Esquerdo, text="IDADE: ").pack()
    Idade = Entry(Frame_Esquerdo)
    Idade.pack()

    Label(Frame_Esquerdo, text="SEXO: ").pack()
    Sexo = Entry(Frame_Esquerdo)
    Sexo.pack()

    LbAltura = Label(Frame_Esquerdo, text="ALTURA: ")
    LbAltura.pack()
    Altura = Entry(Frame_Esquerdo)
    Altura.pack()

    LbPeso = Label(Frame_Esquerdo, text="PESO: ")
    LbPeso.pack()
    Peso = Entry(Frame_Esquerdo)
    Peso.pack()

    LbBicepsD = Label(Frame_Direito, text="BICEPS DIREITO: ")
    LbBicepsD.pack()
    Biceps_direito = Entry(Frame_Direito)
    Biceps_direito.pack()

    LbBicepsE = Label(Frame_Esquerdo, text="BICEPS ESQUERDO: ")
    LbBicepsE.pack()
    Biceps_esquerdo = Entry(Frame_Esquerdo)
    Biceps_esquerdo.pack()

    LbCD = Label(Frame_Direito, text="COXA DIREITA: ")
    LbCD.pack()
    Coxa_direita = Entry(Frame_Direito)
    Coxa_direita.pack()

    LbCE = Label(Frame_Esquerdo, text="COXA ESQUERDA: ")
    LbCE.pack()
    Coxa_esquerda = Entry(Frame_Esquerdo)
    Coxa_esquerda.pack()

    LbBracoD = Label(Frame_Direito, text="ANTI BRAÇO DIREITO: ")
    LbBracoD.pack()
    Antibraco_direito = Entry(Frame_Direito)
    Antibraco_direito.pack()

    LbBracoE = Label(Frame_Esquerdo, text="ANTI BRAÇO ESQUERDO: ")
    LbBracoE.pack()
    Antibraco_esquerdo = Entry(Frame_Esquerdo)
    Antibraco_esquerdo.pack()

    LbPanturrilhaD = Label(Frame_Direito, text="PANTURRILHA DIREITA: ")
    LbPanturrilhaD.pack()
    Panturrilha_direita = Entry(Frame_Direito)
    Panturrilha_direita.pack()

    LbPanturrilhaE = Label(Frame_Esquerdo, text="PANTURRILHA ESQUERDA: ")
    LbPanturrilhaE.pack()
    Panturrilha_esquerda = Entry(Frame_Esquerdo)
    Panturrilha_esquerda.pack()

    LbAbdomen = Label(Frame_Direito, text="ABDÔMEN: ")
    LbAbdomen.pack()
    Abdomen = Entry(Frame_Direito)
    Abdomen.pack()

    LbCintura = Label(Frame_Direito, text="CINTURA: ")
    LbCintura.pack()
    Cintura = Entry(Frame_Direito)
    Cintura.pack()

    LbQuadril = Label(Frame_Direito, text="QUADRIL: ")
    LbQuadril.pack()
    Quadril = Entry(Frame_Direito)
    Quadril.pack()

    LbTorax = Label(Frame_Direito, text="TÓRAX: ")
    LbTorax.pack()
    Torax = Entry(Frame_Direito)
    Torax.pack()

    LbOmbro = Label(Frame_Direito, text="OMBRO: ")
    LbOmbro.pack()
    Ombro = Entry(Frame_Direito)
    Ombro.pack()

    def BtSalva_clique():
        global nome
        global idade
        global sexo
        global altura
        global peso
        global biceps_direito
        global biceps_esquerdo
        global coxa_direita
        global coxa_esquerda
        global antibraco_direito
        global antibraco_esquerdo
        global panturrilha_direita
        global panturrilha_esquerda
        global abdomen
        global cintura
        global quadril
        global torax
        global ombro

        ###SALVANDO TODOS OS DADOS PASSADOS PARA AS VARIAVEIS EXTERNAS

        nome                 =   str(Nome.get()).upper()
        idade                =   int(Idade.get())
        sexo                 =   str(Sexo.get())
        altura               =   float(Altura.get())
        peso                 =   float(Peso.get())
        biceps_direito       =   float(Biceps_direito.get())
        biceps_esquerdo      =   float(Biceps_esquerdo.get())
        coxa_direita         =   float(Coxa_direita.get())
        coxa_esquerda        =   float(Coxa_esquerda.get())
        antibraco_direito    =   float(Antibraco_direito.get())
        antibraco_esquerdo   =   float(Antibraco_esquerdo.get())
        panturrilha_direita  =   float(Panturrilha_direita.get())
        panturrilha_esquerda =   float(Panturrilha_esquerda.get())
        abdomen              =   float(Abdomen.get())
        cintura              =   float(Cintura.get())
        quadril              =   float(Quadril.get())
        torax                =   float(Torax.get())
        ombro                =   float(Ombro.get())

        #Muda o Nome do Botão Salvar e a cor para Amarelo
        BtSalva["text"]="SALVO"
        BtSalva["bg"] = "yellow"


    BtSalva = Button(Janela_Cadastro, text="SALVAR", command= BtSalva_clique)
    BtSalva.pack(side=BOTTOM)

#Menu 02 - Lista de Treino

def ListaTreino():
    janelaTreino = Tk()
    janelaTreino.title("LISTA TREINO SEMANAL")

    janelaTreino.geometry()

    arquivo = open("treino.txt")

    Texto = Label(janelaTreino)
    Texto.pack(side=LEFT)

    for linha in arquivo.readlines():
        Texto['text'] += linha


# MENU 3 AVANÇO DURANTE TREINO

# MENU ATUALIZA O CADASTRO DO USUARIO#


def Atualiza_Cadastro():
    Janela_Cadastro = Tk()
    Janela_Cadastro.title("AVANÇO MENSAL")

    Janela_Cadastro.geometry("500x500")

    Frame_Direito = Label(Janela_Cadastro)
    Frame_Direito.pack(side=RIGHT)

    Frame_Esquerdo = Label(Janela_Cadastro)
    Frame_Esquerdo.pack(side=LEFT)

    LbAltura = Label(Frame_Esquerdo, text="ALTURA: ")
    LbAltura.pack()
    Altura = Entry(Frame_Esquerdo)
    Altura.pack()

    LbPeso = Label(Frame_Esquerdo, text="PESO: ")
    LbPeso.pack()
    Peso = Entry(Frame_Esquerdo)
    Peso.pack()

    LbBicepsD = Label(Frame_Direito, text="BICEPS DIREITO: ")
    LbBicepsD.pack()
    Biceps_direito = Entry(Frame_Direito)
    Biceps_direito.pack()

    LbBicepsE = Label(Frame_Esquerdo, text="BICEPS ESQUERDO: ")
    LbBicepsE.pack()
    Biceps_esquerdo = Entry(Frame_Esquerdo)
    Biceps_esquerdo.pack()

    LbCD = Label(Frame_Direito, text="COXA DIREITA: ")
    LbCD.pack()
    Coxa_direita = Entry(Frame_Direito)
    Coxa_direita.pack()

    LbCE = Label(Frame_Esquerdo, text="COXA ESQUERDA: ")
    LbCE.pack()
    Coxa_esquerda = Entry(Frame_Esquerdo)
    Coxa_esquerda.pack()

    LbBracoD = Label(Frame_Direito, text="ANTI BRAÇO DIREITO: ")
    LbBracoD.pack()
    Antibraco_direito = Entry(Frame_Direito)
    Antibraco_direito.pack()

    LbBracoE = Label(Frame_Esquerdo, text="ANTI BRAÇO ESQUERDO: ")
    LbBracoE.pack()
    Antibraco_esquerdo = Entry(Frame_Esquerdo)
    Antibraco_esquerdo.pack()

    LbPanturrilhaD = Label(Frame_Direito, text="PANTURRILHA DIREITA: ")
    LbPanturrilhaD.pack()
    Panturrilha_direita = Entry(Frame_Direito)
    Panturrilha_direita.pack()

    LbPanturrilhaE = Label(Frame_Esquerdo, text="PANTURRILHA ESQUERDA: ")
    LbPanturrilhaE.pack()
    Panturrilha_esquerda = Entry(Frame_Esquerdo)
    Panturrilha_esquerda.pack()

    LbAbdomen = Label(Frame_Direito, text="ABDÔMEN: ")
    LbAbdomen.pack()
    Abdomen = Entry(Frame_Direito)
    Abdomen.pack()

    LbCintura = Label(Frame_Direito, text="CINTURA: ")
    LbCintura.pack()
    Cintura = Entry(Frame_Direito)
    Cintura.pack()

    LbQuadril = Label(Frame_Direito, text="QUADRIL: ")
    LbQuadril.pack()
    Quadril = Entry(Frame_Direito)
    Quadril.pack()

    LbTorax = Label(Frame_Direito, text="TÓRAX: ")
    LbTorax.pack()
    Torax = Entry(Frame_Direito)
    Torax.pack()

    LbOmbro = Label(Frame_Direito, text="OMBRO: ")
    LbOmbro.pack()
    Ombro = Entry(Frame_Direito)
    Ombro.pack()

    def BtSalva_clique():
        #PEGA TODAS AS VARIAVEIS EXTERNAS
        global nome
        global altura
        global peso
        global biceps_direito
        global biceps_esquerdo
        global coxa_direita
        global coxa_esquerda
        global antibraco_direito
        global antibraco_esquerdo
        global panturrilha_direita
        global panturrilha_esquerda
        global abdomen
        global cintura
        global quadril
        global torax
        global ombro

        ### CALCULAR PORCENTAGEM DE CRESCIMENTO ANTES DE SALVAR NOVOS VALORES

        Crescimento_altura               = ((float(Altura.get())              *100)/ altura               )-100
        Crescimento_peso                 = ((float(Peso.get())                *100)/ peso                 )-100
        Crescimento_biceps_direito       = ((float(Biceps_direito.get())      *100)/ biceps_direito       )-100
        Crescimento_biceps_esquerdo      = ((float(Biceps_esquerdo.get())     *100)/ biceps_esquerdo      )-100
        Crescimento_coxa_direita         = ((float(Coxa_direita.get())        *100)/ coxa_direita         )-100
        Crescimento_coxa_esquerda        = ((float(Coxa_esquerda.get())       *100)/ coxa_esquerda        )-100
        Crescimento_antibraco_direito    = ((float(Antibraco_direito.get())   *100)/ antibraco_direito    )-100
        Crescimento_antibraco_esquerdo   = ((float(Antibraco_esquerdo.get())  *100)/ antibraco_esquerdo   )-100
        Crescimento_panturrilha_direita  = ((float(Panturrilha_direita.get()) *100)/ panturrilha_direita  )-100
        Crescimento_panturrilha_esquerda = ((float(Panturrilha_esquerda.get())*100)/ panturrilha_esquerda )-100
        Crescimento_abdomen              = ((float(Abdomen.get())             *100)/ abdomen              )-100
        Crescimento_cintura              = ((float(Cintura.get())             *100)/ cintura              )-100
        Crescimento_quadril              = ((float(Quadril.get())             *100)/ quadril              )-100
        Crescimento_torax                = ((float(Torax.get())               *100)/ torax                )-100
        Crescimento_ombro                = ((float(Ombro.get())               *100)/ ombro                )-100

        ###SALVANDO TODOS OS CRESCIMENTOS EM ARQUIVO

        crescimento = open("CrescimentoUsuario.txt",'w',encoding="utf8")

        crescimento.write("\n \nPROGRESSO MENSAL (%):\n \n")
        crescimento.write("USUARIO: %s \n" %nome)
        crescimento.write("Altura: %.2f \n" %Crescimento_altura)
        crescimento.write("Peso: %.2f \n" %Crescimento_peso)
        crescimento.write("Biceps_direito: %.2f \n" %Crescimento_biceps_direito)
        crescimento.write("Biceps_esquerdo: %.2f \n" %Crescimento_biceps_esquerdo)
        crescimento.write("Coxa_direita: %.2f \n" %Crescimento_coxa_direita)
        crescimento.write("Coxa_esquerda: %.2f \n" %Crescimento_coxa_esquerda)
        crescimento.write("Antibraco_direito: %.2f \n" %Crescimento_antibraco_direito)
        crescimento.write("Antibraco_esquerdo: %.2f \n" %Crescimento_antibraco_esquerdo)
        crescimento.write("Panturrilha_direita: %.2f \n" %Crescimento_panturrilha_direita)
        crescimento.write("Panturrilha_esquerda: %.2f \n" %Crescimento_panturrilha_esquerda)
        crescimento.write("Abdomen: %.2f \n" %Crescimento_abdomen)
        crescimento.write("Cintura: %.2f \n" %Crescimento_cintura)
        crescimento.write("Quadril: %.2f \n" %Crescimento_quadril)
        crescimento.write("Torax: %.2f \n" %Crescimento_torax)
        crescimento.write("Ombro: %.2f \n" %Crescimento_ombro)

        ###SALVANDO TODOS OS DADOS PASSADOS PARA AS VARIAVEIS EXTERNAS

        altura =                float(Altura.get())
        peso =                  float(Peso.get())
        biceps_direito =        float(Biceps_direito.get())
        biceps_esquerdo =       float(Biceps_esquerdo.get())
        coxa_direita =          float(Coxa_direita.get())
        coxa_esquerda =         float(Coxa_esquerda.get())
        antibraco_direito =     float(Antibraco_direito.get())
        antibraco_esquerdo =    float(Antibraco_esquerdo.get())
        panturrilha_direita =   float(Panturrilha_direita.get())
        panturrilha_esquerda =  float(Panturrilha_esquerda.get())
        abdomen =               float(Abdomen.get())
        cintura =               float(Cintura.get())
        quadril =               float(Quadril.get())
        torax =                 float(Torax.get())
        ombro =                 float(Ombro.get())

        # Muda o Nome do Botão Salvar e a cor para Amarelo
        BtSalva["text"] = "SALVO!"
        BtSalva["bg"] = "yellow"

    BtSalva = Button(Janela_Cadastro, text="SALVAR", command=BtSalva_clique)
    BtSalva.pack(side=BOTTOM)

# MENU 4 - RELATORIO DE AVANÇO MENSAL

def Relatorio_Mensal():

    janelaRelatorio = Tk()
    janelaRelatorio.title("PROGRESSO MENSAL")


    janelaRelatorio.geometry()

    arquivo = open("CrescimentoUsuario.txt")

    Texto = Label(janelaRelatorio)
    Texto.pack(side=LEFT)

    for linha in arquivo.readlines():
        Texto['text'] += linha

#FUNÇÃO DE ALTERAÇÃO DE SENHA#

def AlterarSenha():
    global nome
    global Senha

    janela_AlteraSenha = Tk()
    janela_AlteraSenha.title("ALTERAÇÃO DE SENHA")
    janela_AlteraSenha.geometry("300x150+400+400")


    def RealizarAlteracaoSenha():
        #SENHA VAI RECEBER A NOVA SENHA DIGITADA#

        global Senha
        Senha = str(CampoSenha.get()).upper()

        LbMensagem["text"] = "SENHA ALTERADA COM SUCESSO"


    LbNome = Label(janela_AlteraSenha, text="USUARIO "+nome)
    LbNome.pack()

    LbSenha = Label(janela_AlteraSenha, text="NOVA SENHA: ")
    LbSenha.pack()

    CampoSenha = Entry(janela_AlteraSenha)
    CampoSenha.pack()

    BtAlterar = Button(janela_AlteraSenha, text="ALTERAR", width=10, command=RealizarAlteracaoSenha)
    BtAlterar.pack()

    LbMensagem = Label(janela_AlteraSenha, text="PREENCHA NOVA SENHA \n ANTES DE ALTERAR", bg="blue")
    LbMensagem.pack()

#INICIO LOGINxMENU#


def Janela_Cadastro_Click():
    global nome
    global Senha

    def RealizarLogin():
        global nome
        global Senha

        Login_Informado = str(CampoLogin.get()).upper()
        Senha_Informada = str(CampoSenha.get()).upper()

        if ((nome == Login_Informado) and (Senha == Senha_Informada)):
            LbMensagem["text"] = "LOGIN REALIZADO!"
            LbMensagem["bg"] = "green"
            Janela_Cadastro()
        else:
            LbMensagem["text"] = "USUARIO OU SENHA INVALIDOS"
            LbMensagem["bg"] = "red"

    janela_Login = Tk()
    janela_Login.title("LOGIN")
    janela_Login.geometry("200x200+300+300")

    LbLogin = Label(janela_Login, text="LOGIN: ")
    LbLogin.pack()

    CampoLogin = Entry(janela_Login)
    CampoLogin.pack()

    LbSenha = Label(janela_Login, text="SENHA: ")
    LbSenha.pack()

    CampoSenha = Entry(janela_Login)
    CampoSenha.pack()

    BtEntrar = Button(janela_Login, text="ENTRAR", width=10, command=RealizarLogin)
    BtEntrar.pack()

    LbMensagem = Label(janela_Login, text="INFORME DADOS CORRETOS")
    LbMensagem.pack()


def Atualiza_Cadastro_Click():
    global nome
    global Senha

    def RealizarLogin():
        global nome
        global Senha

        Login_Informado = str(CampoLogin.get()).upper()
        Senha_Informada = str(CampoSenha.get()).upper()

        if ((nome == Login_Informado) and (Senha == Senha_Informada)):
            LbMensagem["text"] = "LOGIN REALIZADO!"
            LbMensagem["bg"] = "green"
            Atualiza_Cadastro()
        else:
            LbMensagem["text"] = "USUARIO OU SENHA INVALIDOS"
            LbMensagem["bg"] = "red"

    janela_Login = Tk()
    janela_Login.title("LOGIN")
    janela_Login.geometry("200x200+300+300")

    LbLogin = Label(janela_Login, text="LOGIN: ")
    LbLogin.pack()

    CampoLogin = Entry(janela_Login)
    CampoLogin.pack()

    LbSenha = Label(janela_Login, text="SENHA: ")
    LbSenha.pack()

    CampoSenha = Entry(janela_Login)
    CampoSenha.pack()

    BtEntrar = Button(janela_Login, text="ENTRAR", width=10, command=RealizarLogin)
    BtEntrar.pack()

    LbMensagem = Label(janela_Login, text="INFORME DADOS CORRETOS")
    LbMensagem.pack()


def Relatorio_Mensal_Click():

    global nome
    global Senha

    def RealizarLogin():
        global nome
        global Senha

        Login_Informado = str(CampoLogin.get()).upper()
        Senha_Informada = str(CampoSenha.get()).upper()

        if((nome==Login_Informado)and(Senha==Senha_Informada)):
            LbMensagem["text"] = "LOGIN REALIZADO!"
            LbMensagem["bg"] = "green"
            Relatorio_Mensal()
        else:
            LbMensagem["text"] = "USUARIO OU SENHA INVALIDOS"
            LbMensagem["bg"] = "red"

    janela_Login = Tk()
    janela_Login.title("LOGIN")
    janela_Login.geometry("200x200+300+300")

    LbLogin = Label(janela_Login, text="LOGIN: ")
    LbLogin.pack()

    CampoLogin = Entry(janela_Login)
    CampoLogin.pack()

    LbSenha = Label(janela_Login, text="SENHA: ")
    LbSenha.pack()

    CampoSenha = Entry(janela_Login)
    CampoSenha.pack()

    BtEntrar = Button(janela_Login,text="ENTRAR", width=10, command=RealizarLogin)
    BtEntrar.pack()

    LbMensagem = Label(janela_Login, text="INFORME DADOS CORRETOS")
    LbMensagem.pack()

    janela_Login.mainloop()

#ALTERAÇÃO DE SENHA#

def Alteracao_Senha_Click():
    global nome
    global Senha

    def RealizarLogin():
        global nome
        global Senha

        Login_Informado = str(CampoLogin.get()).upper()
        Senha_Informada = str(CampoSenha.get()).upper()

        if ((nome == Login_Informado) and (Senha == Senha_Informada)or(("ADMINISTRADOR"==Login_Informado) and ("MASTER"==Senha_Informada))):
            LbMensagem["text"] = "LOGIN REALIZADO!"
            LbMensagem["bg"] = "green"
            AlterarSenha()
        else:
            LbMensagem["text"] = "USUARIO OU SENHA INVALIDOS"
            LbMensagem["bg"] = "red"

    janela_Login = Tk()
    janela_Login.title("LOGIN")
    janela_Login.geometry("200x200+300+300")

    LbLogin = Label(janela_Login, text="LOGIN: ")
    LbLogin.pack()

    CampoLogin = Entry(janela_Login)
    CampoLogin.pack()

    LbSenha = Label(janela_Login, text="SENHA: ")
    LbSenha.pack()

    CampoSenha = Entry(janela_Login)
    CampoSenha.pack()

    BtEntrar = Button(janela_Login, text="ENTRAR", width=10, command=RealizarLogin)
    BtEntrar.pack()

    LbMensagem = Label(janela_Login, text="INFORME DADOS CORRETOS")
    LbMensagem.pack()

    janela_Login.mainloop()


#FINAL LOGINxMENU#
#LABEL DO MENU CUJO MENUs VÃO FICAR#
menu = Label(janela_principal, bg="#3333EE")
menu.pack(side=TOP, fill=X)

#MENUs#
menu1 = Button(menu, text="CADASTROS", bg="#0000CC",command=Janela_Cadastro_Click)
menu1.pack(side=LEFT, fill=BOTH, expand=1)

menu2 = Button(menu,text="LISTA DE TREINO", bg="#0000CC", command=ListaTreino)
menu2.pack(side=LEFT, fill=BOTH, expand=1)

menu3 = Button(menu, text="AVANÇOS", bg="#0000CC", command=Atualiza_Cadastro_Click)
menu3.pack(side=LEFT, fill=BOTH, expand=1)

menu4 = Button(menu, text="RELATÓRIOS", bg="#0000CC", command=Relatorio_Mensal_Click)
menu4.pack(side=LEFT, fill=BOTH, expand=1)

menu5 = Button(menu, text="ALTERA SENHA", bg="#0000CC", command=Alteracao_Senha_Click)
menu5.pack(side=LEFT, fill=BOTH, expand=1)

####FOTO NA JANELA

img = PhotoImage(file="Header.png")

buttonPP = Label(janela_principal, image=img)
buttonPP.pack()

janela_principal.geometry("1000x500")
janela_principal.mainloop()
