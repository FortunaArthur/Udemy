       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG16.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
      *    No codigo da aula ele coloca com 3 casas decimais, MAS
      *    N�o vi sentido nisso ent�o voltei pra 2
       01  VALOR PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "--- USO DO AND ---".
           DISPLAY "Informe 1 Numero Maior que 10 e Menor que 100".
           DISPLAY "na faixa de 11 at� 99".
           ACCEPT VALOR.

           IF VALOR > 10 AND VALOR < 100
               DISPLAY "O Numero " VALOR " Esta no Intervalo".

       PROGRAM-DONE.
           STOP RUN.
