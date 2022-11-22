       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG21.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Usando PERFORM UNTIL Programa Para Fazer Tabuada

       WORKING-STORAGE SECTION.

       01  NUMERO PIC 99.
       01  MULTIPLICADOR PIC 999.
       01  PRODUTO PIC 9(4).

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

       EXIBIR.
           DISPLAY "Tabuada de Multiplicação de " NUMERO " == "
      *    Ele não pergunta mais o tamanho da tabuada, faz direto tamanho 6
      *    Tamanho 6 PQ, ele só para quando for MAIOR QUE 5, igual a 5 não para
           PERFORM CALCULO UNTIL MULTIPLICADOR > 5. *> se Botar >= ele vai até 5*>
      *    Parece 1 for i in range ou 1 While
      *    Faça o CALCULO até que o MULTIPLICADOR seja MAIOR QUE 5

       CALCULO.
           ADD 1 TO MULTIPLICADOR.
           COMPUTE PRODUTO = NUMERO * MULTIPLICADOR
           DISPLAY
           NUMERO " * " MULTIPLICADOR " = " PRODUTO.
