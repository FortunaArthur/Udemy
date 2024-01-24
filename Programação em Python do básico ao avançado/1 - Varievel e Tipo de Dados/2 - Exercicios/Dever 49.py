#49
#Ja tava puto e me deu 1 preguiça da porra de fazer esse aki, ai peguei nesse site aki
# https://brainly.com.br/tarefa/38885954
print('Preencha os campos abaixo com o horário atual')

h = int(input('Hora: '))

m = int(input('Minuto: '))

s = int(input('Segundo: '))

d = int(input('\nDuração do evento (segundos): '))

s_final = (s + d) % 60

m_final = ( m + (s+d)//60 ) % 60

h_final = ( h + ( m + (s+d)//60 )//60 ) % 24

print(f'O fim do evento se dará às {h_final}h {m_final}min e {s_final} segundos')