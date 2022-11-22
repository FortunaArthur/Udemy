       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG25.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Mover para Varias Variaveis

       WORKING-STORAGE SECTION.

       01  6-BYTES PIC X(6).
       01  5-BYTES PIC X(5).
       01  4-BYTES PIC X(4).
       01  3-BYTES PIC X(3).
       01  2-BYTES PIC X(2).
       01  1-BYTES PIC X(1).

       01  5-DIGITOS PIC 9(5).
       01  4-DIGITOS PIC 9(4).
       01  3-DIGITOS PIC 9(2).
       01  2-DIGITOS PIC 9(2).
       01  1-DIGITOS PIC 9(1).

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           MOVE "Arthur" TO 6-BYTES 5-BYTES 4-BYTES
                           3-BYTES 2-BYTES 1-BYTES.

           MOVE 6789 TO 5-DIGITOS 4-DIGITOS 3-DIGITOS
                        2-DIGITOS 1-DIGITOS.

      *    É SÓ COLOCAR TODAS AS VARIAVEIS QUE VC QUER PARA MOVER OS DADOS

           DISPLAY 6-BYTES.
           DISPLAY 5-BYTES.
           DISPLAY 4-BYTES.
           DISPLAY 3-BYTES.
           DISPLAY 2-BYTES.
           DISPLAY 1-BYTES.

           DISPLAY "===================================="

           DISPLAY 5-DIGITOS.
           DISPLAY 4-DIGITOS.
           DISPLAY 3-DIGITOS.
           DISPLAY 2-DIGITOS.
           DISPLAY 1-DIGITOS.

       PROGRAM-DONE.
           STOP RUN.

      *    LEMBRETE, VARIAVEIS TIPO TEXTO, O COBOL CORTA DA ULTIMA DA DIREITA
      *    VARIAVEIS TIPO NUMERIO, ELE CORDA DA ULTIMA DA ESQUERDA
