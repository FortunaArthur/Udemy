       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG29.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Demonstra��o de RECORD
      *    Usando FILLER agora

       WORKING-STORAGE SECTION.

       01  FUNCIONARIO.
      *    Por uma Conven��o de KD Variavel que vc coloca identan��o
      *    VC COLOCA 5
           05 CODIGO PIC 9(2).
           05 FILLER PIC X(2) VALUE "--".
           05 NOME PIC X(10).
           05 FILLER PIC X(4) VALUE "===".
           05 ENDERECO PIC X(30).
           05 FILLER PIC X(1) VALUE "*".
           05 SALARIO PIC 9(4)V9(2).
      *    Basicamente � uma Separa��o de Campos pra Melhor Vizualiza��o

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           MOVE 33 TO CODIGO.
           MOVE "Jose" TO NOME.
           MOVE "Rua da Mans�o Foster" TO ENDERECO.
           MOVE 2500.00 TO SALARIO.

           DISPLAY FUNCIONARIO.

       PROGRAM-DONE.
           STOP RUN.
