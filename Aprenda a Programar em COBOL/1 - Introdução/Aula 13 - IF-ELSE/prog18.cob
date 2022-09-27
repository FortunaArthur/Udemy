       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG18.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  VALOR PIC 9(3).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "--- USO DO IF-ELSE ---".
           DISPLAY "Informe 1 Numero Maior que 10 e Menor que 100".
           DISPLAY "na faixa de 11 até 99".
           ACCEPT VALOR.

           IF VALOR > 10 AND VALOR < 100
               DISPLAY "O Numero " VALOR " Esta no Intervalo"
      *    QUANDO FOR USAR ELSE, VC NÃO PODE BOTAR O PONTO NO FINAL DO IF
      *    SOMENTE NO FINAL DO DISPLAY DO ELSE.
           ELSE
               DISPLAY "INVALIDO".
      *    LEMBRETE, ELSE-IF NÃO É ACEITO
      *    SOMENTE IF ELSE NORMAL
       PROGRAM-DONE.
           STOP RUN.
