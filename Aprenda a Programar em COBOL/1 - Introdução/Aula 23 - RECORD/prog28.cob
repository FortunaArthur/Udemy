       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG28.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Demonstra��o de RECORD

       WORKING-STORAGE SECTION.

       01  FUNCIONARIO.
      *    Por uma Conven��o de KD Variavel que vc coloca identan��o
      *    VC COLOCA 5
           05 CODIGO PIC 9(2).
           05 NOME PIC X(20).
           05 ENDERECO PIC X(20).
           05 SALARIO PIC 9(4)V9(2).

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           MOVE 33 TO CODIGO.
           MOVE "Jose" TO NOME.
           MOVE "Rua da Mans�o Foster" TO ENDERECO.
           MOVE 2500.00 TO SALARIO.

           DISPLAY FUNCIONARIO.

       PROGRAM-DONE.
           STOP RUN.
