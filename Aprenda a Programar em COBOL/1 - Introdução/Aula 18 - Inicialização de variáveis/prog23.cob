       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG23.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Inicialização de Variaveis

       WORKING-STORAGE SECTION.

       01  NUMERO PIC 9(2) VALUE 15.*>Já vai iniciar ocm 15*>
       01  MENSAGEM PIC X(20) VALUE "Curso de COBOL".*>Já Vai Iniciar com essa Mensagem*>
      *    ZERO, ZEROS, ZEROES
       01  NUMERO2 PIC 99 VALUE ZEROS.*>Vai Iniciar com 00*>
      *    SPACE, SPACES
       01  TEXTO PIC X(30) VALUE SPACES.*>Vai Iniciar com 30 Espaços Vazios*>

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.
           DISPLAY "NUMERO: " NUMERO.
           DISPLAY "MENSAGEM: " MENSAGEM.

           DISPLAY "-------------------".

           DISPLAY "NUMERO2: " NUMERO2.
           DISPLAY "TEXTO: " TEXTO.

           DISPLAY "ATRIBUINDO VALORES".
           ADD 20 TO NUMERO2.
           DISPLAY "NUMERO2: " NUMERO2.

       PROGRAM-DONE.
           STOP RUN.
