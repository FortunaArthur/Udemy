       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG22.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Usando PERFORM VARYING FROM, Programa Para Fazer Tabuada

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
           PERFORM CALCULO
           VARYING MULTIPLICADOR
      *    APARTIR DO VALOR 2, SOME +3 E ASSIM VAI
           FROM 2 BY 3 *> Aki ele pega o multiplicador que A PARTIR DE 2, ele vai somar +3*>
      *    DPS ele somara +3 ao mesmo valor, mais pode mudar esses numeros: TIPO,, FROM 1 BY 1
           UNTIL MULTIPLICADOR > QUANTOS.

       CALCULO.

           COMPUTE PRODUTO = NUMERO * MULTIPLICADOR
           DISPLAY
           NUMERO " * " MULTIPLICADOR " = " PRODUTO.
