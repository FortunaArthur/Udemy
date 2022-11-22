1
while True:
    s1 = input("sequencia1: ")
    s2 = input("sequencia2: ")

    if s1 == s2:
        print("IGUAIS")
        False
        break
    else:
        print("Diferentes\n")
    
2
arquivo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo_lista2.txt","w")
texto = input("Digita o texto: ")
escrever = arquivo.write(texto)

arquivo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo_lista2.txt")
ler = arquivo.read()
print("TEXTO QUE VC DIGITOU NO ARQUIVO:")
print(ler)

3
arquivo = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\arquivo_lista2.fasta","w")
texto = input("Digita o texto: ")
escrever = arquivo.write(texto)

4
def abrir():
    nome = input("Nome do arquivo: ")
    arquivo = open(nome)# pegar o arquivo e guardalo
    print("Arquivo Aberto\n")
    return arquivo

def ler(arquivo):# ele vai recever o arquivo da função abrir
    ler = arquivo.read()
    print("Conteudo do Arquivo: ")
    print(ler)
    print("\n")

while True:
    print("1 - Escolher Arquivo" + "\n"
    "2 - Ler Arquivo" + "\n"
    "3 - Fim do Programa")

    menu = int(input("Opção: "))
    if menu == 1:
        arquivo = abrir()
    elif menu == 2:
        ler(arquivo)
    elif menu == 3:
        print("FIM DO PROGRAMA")
        False
        break
    else:
        print("Opção Errada")

#5
abrir = open(r"C:\Users\arthu\Documents\Repositórios GitHub\Udemy\Python & MySQL\Python\2 - Python Intermediario\multi-fasta.fasta",errors="ignore")
# TEM Q COLOCAR ESSA PORRA PQ SE NÃO ELA DA ERRO ( errors="ignore" )

dicionario = {}

'''''''''''''''''''''''''''
ler = abrir.read()
for i in ler:
    print(i)

SE vc usar assim ele vai ler caratcer por caractaer e vai DEMORAR MUITO
'''''''''''''''''''''''''''

linhas = abrir.readlines() #vamos ler as linhas

for i in linhas:
    
    if i[0] == ">":# pegar o cabeçalho e armazenar akela linha
        "se fizer i[1:] ele vai pegar dps do sinal >, ai ele n aparece"
        sekuencia = i.strip()# remover quebra de linha
# O dicionario vai receber a SEKUENCIA como chave, e o vazio "" será o valor
        dicionario[sekuencia] = ""

    else:
        # Adicionar valor as chaves
        dicionario[sekuencia] = dicionario[sekuencia] + i.strip()
# Como o cabeçalho ja foi add, aki ele vai receber as sequencias de kd cabeçalho e add nas suas chaves
# sendo ele msm concatenando com i

print(dicionario)