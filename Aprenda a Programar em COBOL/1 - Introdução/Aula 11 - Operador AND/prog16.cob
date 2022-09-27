       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG16.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
      *    No codigo da aula ele coloca com 3 casas decimais, MAS
      *    Não vi sentido nisso então voltei pra 2
       01  VALOR PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "--- USO DO AND ---".
           DISPLAY "Informe 1 Numero Maior que 10 e Menor que 100".
           DISPLAY "na faixa de 11 até 99".
           ACCEPT VALOR.

           IF VALOR > 10 AND VALOR < 100
               DISPLAY "O Numero " VALOR " Esta no Intervalo".

       PROGRAM-DONE.
           STOP RUN.
