# importar bibliotecas
from tkinter import * # TEM Q SER ASSIM E PQ SIM
from tkinter import messagebox
from tkinter import ttk

#AGR VAI INTEGRAR COMO BACK END
import DataBaser

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

# Colocando o ICONE
janela.iconbitmap(default="C:/Users/arthu/OneDrive/Documentos/GitHub/Udemy/Python/Sistema de Login com Python e SQL/imgs/LogoIcon.ico") 

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
logo = PhotoImage(file="C:/Users/arthu/OneDrive/Documentos/GitHub/Udemy/Python/Sistema de Login com Python e SQL/imgs/Logo.png")
Rotulo_da_Logo = Label(Frame_Esquerdo, image=logo, bg=RGBZINHO((255,128,0)))
Rotulo_da_Logo.place(x=50, y=100)

# ============== USUARIO
Rotulo_Usuario = Label(Frame_Direito, text="Usuário:", font=("Century Gothic", 20), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
Rotulo_Usuario.place(x=5, y=110)

# ============== ENTRADA DE DADOS DO USUARIO
Entrada_Usuario = ttk.Entry(Frame_Direito, width=40)
# ajustar x e y demoro + foi
Entrada_Usuario.place(x=110, y=120)

# ============== SENHA (BASICAMENTE MSM COISA DO USAURIO SO MUDA OS NOME, e a altura tb)
Rotulo_Senha = Label(Frame_Direito, text="Senha:", font=("Century Gothic", 20), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
Rotulo_Senha.place(x=12, y=159)

# ============== ENTRADA DA SENHA
# não deixar mostrar a senha com show=
Entrada_Senha = ttk.Entry(Frame_Direito, width=40, show="■") #USEI esse site aki https://www.textemoji.org/
# agr ajustei LEGAL
Entrada_Senha.place(x=110, y=170)

# ============== AGORA É OS BUTÃO (AKI VAMO CRIA OS BUTÃO), TO MO FELIZ OUVINDO ROCK JAPONES
# AGORA CRIAR O COMANDO DE LOGAR

def Logar():
    Usuario = Entrada_Usuario.get()
    Senha = Entrada_Senha.get()

    DataBaser.cursor.execute("""
    SELECT * FROM tb_Usuarios WHERE (Usuario = ? AND Senha =?)
    """,(Usuario, Senha))
    print("PASSSOU PORRA")
    Verificar = DataBaser.cursor.fetchone()
    # FAZER VERIFICAÇÃO
    try:
        if Usuario in Verificar and Senha in Verificar:
            messagebox.showinfo(title="Informação de Login", message="Login Confirmado. Bem-Vindo!")
    except:
        messagebox.showinfo(title="Informação de Login", message="Acesso Negado. Verifique seu Cadastro no Sistema")

Butao_Login = ttk.Button(Frame_Direito, text="Login", width=35, command=Logar)
Butao_Login.place(x=110, y=220)

#CRIANDO A FUNÇÃO DE CADASTRO E ASSEMELHANDO ELA NA VARIAVEL DE CADASTRO
def Cadastro():
    # Primeiro é limpar, tirar os butões
    # truque é botar o place la na casa do krl
    Butao_Login.place(x=10000000000000000000000000)
    Butao_Cadastro.place(x=10000000000000000000000000)

    # Segundo é INSERIR OS WIDGETS DE CADASTRO
    Rotulo_Nome = Label(Frame_Direito, text="Nome:", font=("Century Gothic", 20), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
    Rotulo_Nome.place(x=20, y=30)
    Entrada_Nome = ttk.Entry(Frame_Direito, width=40)
    Entrada_Nome.place(x=110, y=40)

    Rotulo_Email = Label(Frame_Direito, text="Email:", font=("Century Gothic", 20), bg=RGBZINHO((135, 135, 0)), fg= RGBZINHO((76, 0, 153)))
    Rotulo_Email.place(x=20, y=70)
    Entrada_Email = ttk.Entry(Frame_Direito, width=40)
    Entrada_Email.place(x=110, y=81)

    # TERCEIRAMENTO, FAZER OS BUTÃO DE REGISTRO E DE VOLTA
    # AGR EU VOI ADCICIONAR OS COMANDOS PRA CADASTRAR

    def CadastrarnoBanco():
        Nome = Entrada_Nome.get()
        Email = Entrada_Email.get()
        Usuario = Entrada_Usuario.get()
        Senha = Entrada_Senha.get()

        #CRIAR A CONDIÇÃO DOCAMPO
        if Nome == "" and Email == "" and Usuario == "" and Senha == "":
            messagebox.showerror(title="Erro de Cadastro", message="Preencha Todos os Campos")
        else:
            #INSERIR OS VALORES NA TABELA, E MELMEBROU MUITO O FORMAT DO PYTHON
            DataBaser.cursor.execute("""
            INSERT INTO tb_Usuarios(Nome, Email, Usuario, Senha) VALUES (?, ?, ?, ?)
            """,(Nome, Email, Usuario, Senha))
            DataBaser.conectar.commit()

            #AGORA Q ENTRA A CAIXA DE MENSAGEM
            messagebox.showinfo(title="Infomação de Cadastro", message="Usuário Cadastrado com Sucesso!")


    Cadastrar = ttk.Button(Frame_Direito, text="Cadastrar", width=35, command=CadastrarnoBanco)
    Cadastrar.place(x=110, y=220)

    #SOOOOOO Q PRA VOLTAR PRO MEUNU, TEN FUNÇÃOZINHA MEU BOM
    def VoltarMenu():
        # fazer a msm coisa do primeiro passo, mandas os widgets pra pqp
        # só dessa vez são os de cadastro
        Rotulo_Nome.place(x=-10000000000000000000000000)
        Entrada_Nome.place(x=-10000000000000000000000000)
        Rotulo_Email.place(x=-10000000000000000000000000)
        Entrada_Email.place(x=-10000000000000000000000000)
        Cadastrar.place(x=-10000000000000000000000000)
        Butao_Voltar.place(x=-10000000000000000000000000)
        # man isso daki na real é uma puta duma gambiarra, porem ela funciona, então ta de boa

        # Segundo passo, trazer os widgest do login de  volta
        Butao_Login.place(x=110)
        Butao_Cadastro.place(x=155)

    Butao_Voltar = ttk.Button(Frame_Direito, text="Voltar", width=20, command=VoltarMenu)
    Butao_Voltar.place(x=155, y=260)

Butao_Cadastro = ttk.Button(Frame_Direito, text="Cadastrar", width=20, command=Cadastro)# colocando função no butão cadastro
Butao_Cadastro.place(x=155, y=260)

# MainLoop é o marco final, nada dps do mainloop entra na janela, é o final do codigo da tela
janela.mainloop()
