       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG17.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
      *    No codigo da aula ele coloca com 3 casas decimais, MAS
      *    N�o vi sentido nisso ent�o voltei pra 2

       01  VALOR PIC 9(2).
       01  NOME PIC X(20).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "--- USO DO OR ---".
           DISPLAY "Informe 1 Nome".
           ACCEPT NOME.

           DISPLAY "Informe 1 Numero".
           ACCEPT VALOR.

           IF VALOR > 10 OR NOME = "CHAVES"
               DISPLAY "A CONDI��O � VERDADEIRA".

       PROGRAM-DONE.
           STOP RUN.
