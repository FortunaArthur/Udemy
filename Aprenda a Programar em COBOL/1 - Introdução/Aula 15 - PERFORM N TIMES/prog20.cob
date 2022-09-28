       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG20.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Usando PERFORM N Times. Programa Para Fazer Tabuada

       WORKING-STORAGE SECTION.

       01  NUMERO PIC 99.
       01  MULTIPLICADOR PIC 999.
       01  PRODUTO PIC 9(4).
       01  QUANTOS PIC 99.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.
           PERFORM INICIAR. *> Iniciar as Variaveis *>
           PERFORM TABUADA.
           PERFORM EXIBIR.

       PROGRAM-DONE.
           STOP RUN.

       INICIAR.
           MOVE 0 TO MULTIPLICADOR.

       TABUADA.
           DISPLAY "Qual Numero de Multiplicação? (01-99)".
           ACCEPT NUMERO.

           DISPLAY "Qual o Tamanho da Tabuada?"
           ACCEPT QUANTOS.

       EXIBIR.
           DISPLAY "Tabuada de Multiplicação de " NUMERO " == "
           PERFORM CALCULO QUANTOS TIMES. *> Aki o calculo será feito pela quantidade de vezes *>
      *    Faça QUANTOS vz o CALCULO

       CALCULO.
           ADD 1 TO MULTIPLICADOR.
           COMPUTE PRODUTO = NUMERO * MULTIPLICADOR
           DISPLAY
           NUMERO " * " MULTIPLICADOR " = " PRODUTO.
