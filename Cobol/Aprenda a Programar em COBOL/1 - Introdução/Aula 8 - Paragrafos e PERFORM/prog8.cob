       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG8.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    O CARA FOI REUTILIZAR O PROG3 PRA EXPLICAR PARAGRAFOS

       WORKING-STORAGE SECTION. *> As Variasveis Devem estar Dentro DESTA Seção*>

       01  PRIMEIRO-NUMERO PIC 9(2).*>PIC, PICTURE, PICTURE IS, É a Definição*>
       01  SEGUNDO-NUMERO PICTURE 99. *> 99 é o N limite que essa variavel comporta, (01-99)*>
       01  RESULTADO PICTURE IS 999.*> OU 9(3), 3== Numero de Casas Decimais

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.*> Não se Declara Variaveis Aki*>

       RECEBE-PRIMEIRO-NUMERO. *> PARAGRAFO*>
      *    DISPLAY É BASICAMNETE 1 PRINT
           DISPLAY "Informe o 1° Numero:".
           ACCEPT PRIMEIRO-NUMERO. *> Acemelhar o Dado Fornecido a Variavel*>
      *    Comando | Nome da Variavel que vc Declarou la em Cima*>

       RECEBE-SEGUNDO-NUMERO.*> PARAGRAFO*>
           DISPLAY "Informe o 2° Numero:".
           ACCEPT SEGUNDO-NUMERO.

       INFORMA-RESULTADO.*> PARAGRAFO*>
      *    Acemelhar o RESULTADO a Conta que será feita com as Variaveis
           COMPUTE RESULTADO = PRIMEIRO-NUMERO + SEGUNDO-NUMERO.
      *    Compute vai Executar as Operações Aritimedicas Básicas
           DISPLAY "O Resultado da Soma é: " RESULTADO.

       PROGRAM-DONE.
           STOP RUN.
