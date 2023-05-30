# importar bibliotecas
from tkinter import * # TEM Q SER ASSIM E PQ SIM
from tkinter import messagebox
from tkinter import ttk

#Grande Steck over Flow, salvo nois
# https://stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter
def RGBZINHO(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """

    """Traduz uma tupla RGB de int para um código de cores amigável para tkinter
    """
    return "#%02x%02x%02x" % rgb   

# ============== CRIAR JANELA
janela = Tk()
janela.title("DP Systems - Painel de Acesso")
janela.geometry("600x300")

# E NUM É Q ESSE RGB FUNCIONO MSM, VLW AI overFlows
# site das cores pra se DIiivertir https://www.rapidtables.org/pt/web/color/RGB_Color.html
janela.configure(bg=RGBZINHO((64, 64, 64)))

#Issu daki é pra deixar respnsivo ou seja, pra poder alterar tamanho com o mouse, se tlg q eu sei, o cara deixo false mais eu vo deixa True
#VOLTEI ATRAZ DEU RUIM DEIXAR TRUE
janela.resizable(width=False, height=False)

# DEIXAR A JANILINHA TRANSPARENTE OH PAI
janela.attributes("-alpha", 0.8)

# ============== FAZER JANELINHAS (WIDGETS)
Frame_Esquerdo = Frame(janela, width=200, height=300, bg=RGBZINHO((0, 102, 204)),relief="raise")
Frame_Esquerdo.pack(side=LEFT)

Frame_Direito = Frame(janela, width=390, height=300, bg=RGBZINHO((135, 135, 0)),relief="raise")
Frame_Direito.pack(side=RIGHT)

# ============== IMPORTAR A LOGO
logo = PhotoImage(file="Udemy/Python/Sistema de Login com Python e SQL/imgs/logo.png")
Rotulo_da_Logo = Label(Frame_Esquerdo, image=logo, bg=RGBZINHO((255,128,0)))
Rotulo_da_Logo.place(x=50, y=100)

# ============== USUARIO
Rotulo_do_Usuario = Label(Frame_Direito, text="Usuário:", font=("Century Gothic", 25), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
Rotulo_do_Usuario.place(x=5, y=50)

# ============== ENTRADA DE DADOS DO USUARIO
Entrada_Usuario = ttk.Entry(Frame_Direito, width=40)
# ajustar x e y demoro + foi
Entrada_Usuario.place(x=130, y=65)

# ============== SENHA (BASICAMENTE MSM COISA DO USAURIO SO MUDA OS NOME, e a altura tb)
Rotulo_da_Senha = Label(Frame_Direito, text="Senha:", font=("Century Gothic", 25), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
Rotulo_da_Senha.place(x=5, y=125)

# ============== ENTRADA DA SENHA
Entrada_Usuario = ttk.Entry(Frame_Direito, width=40)
# agr ajustei LEGAL
Entrada_Usuario.place(x=110, y=140)

# ============== AGORA É OS BUTÃO (AKI VAMO CRIA OS BUTÃO), TO MO FELIZ OUVINDO ROCK JAPONES
Butao_Login = ttk.Button(Frame_Direito, text="Login", width=35)
Butao_Login.place(x=110, y=200)

Butao_Cadastro = ttk.Button(Frame_Direito, text="Cadastrar", width=20)
Butao_Cadastro.place(x=155, y=235)

# MainLoop é o marco final, nada dps do mainloop entra na janela, é o final do codigo da tela
janela.mainloop()
