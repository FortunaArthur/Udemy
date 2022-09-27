       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG3.
      *    Demonstrando o uso de Variaveis
      *    Somar 2 N�meros e Mostrar o Resultado
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION. *> As Variasveis Devem estar Dentro DESTA Se��o*>

       01  PRIMEIRO-NUMERO PIC 9(2).*>PIC, PICTURE, PICTURE IS, � a Defini��o*>
       01  SEGUNDO-NUMERO PICTURE 99. *> 99 � o N limite que essa variavel comporta, (01-99)*>
       01  RESULTADO PICTURE IS 999.*> OU 9(3), 3== Numero de Casas Decimais

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.*> N�o se Declara Variaveis Aki*>
      *    DISPLAY � BASICAMNETE 1 PRINT
           DISPLAY "Informe o 1� Numero:".
           ACCEPT PRIMEIRO-NUMERO. *> Acemelhar o Dado Fornecido a Variavel*>
      *    Comando | Nome da Variavel que vc Declarou la em Cima*>

           DISPLAY "Informe o 2� Numero:".
           ACCEPT SEGUNDO-NUMERO.

      *    Acemelhar o RESULTADO a Conta que ser� feita com as Variaveis
           COMPUTE RESULTADO = PRIMEIRO-NUMERO + SEGUNDO-NUMERO.
      *    Compute vai Executar as Opera��es Aritimedicas B�sicas
           DISPLAY "O Resultado da Soma �: " RESULTADO.

       PROGRAM-DONE.
           STOP RUN.
