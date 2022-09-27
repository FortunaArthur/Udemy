       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG15.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Programa para Testar Operadores de Comparação

       WORKING-STORAGE SECTION.

       01  VALOR1 PIC 9(2).
       01  VALOR2 PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "Digiter o Primeiro Valor:"
           ACCEPT VALOR1.

           DISPLAY "Digite o Segundo Valor:"
           ACCEPT VALOR2.

           IF VALOR1 = VALOR2
               DISPLAY "Valores Iguais"
               DISPLAY VALOR1 " Igual " VALOR2.
               DISPLAY "Valores Iguais"
               DISPLAY "Valores Iguais"
      *    O IF vai executar todas as instruções dentro dele até encerrar

           IF VALOR1 > VALOR2
               DISPLAY "Primeiro Valor Maior que o Segundo Valor"
               DISPLAY VALOR1 " Maior que " VALOR2.

           IF VALOR1 < VALOR2
               DISPLAY "Segundo Valor Maior que o Primeiro Valor"
               DISPLAY VALOR2 " Maior que " VALOR1.
      *    Caso VC não Digite valor e de Enter, o Cobol vai assumir esse ENTER como 00

       PROGRAM-DONE.
           STOP RUN.
