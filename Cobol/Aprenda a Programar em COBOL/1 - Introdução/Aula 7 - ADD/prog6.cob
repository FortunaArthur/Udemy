       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG6.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  IDADE PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "Qual sua Idade?"
           ACCEPT IDADE.

           DISPLAY "Hoje vc tem " IDADE " anos".
      *    Adicionando valor a variavel
           ADD 10 TO IDADE.

           DISPLAY "Daki a 10 anos sua idade vai ser " IDADE.

       PROGRAM-DONE.
           STOP RUN.
