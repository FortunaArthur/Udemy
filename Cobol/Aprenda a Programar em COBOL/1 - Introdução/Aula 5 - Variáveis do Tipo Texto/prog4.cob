       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG4.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.
      *    Tipo STRING de tamanho 10
       01  NOME PIC XXXXXXXXXX.
      *    Outra forma --> PIC X(10)

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.
           DISPLAY "Qual seu Nome?".
           ACCEPT NOME.

           DISPLAY "Salve " NOME.

       PROGRAM-DONE.
           STOP RUN.
