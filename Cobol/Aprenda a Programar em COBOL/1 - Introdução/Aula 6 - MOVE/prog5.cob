       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG5.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  MINHA-MENSAGEM PIC X(20).
       01  NOME PIC X(10).
       01  NUMERO PIC 9(2).

       PROCEDURE DIVISION.

           DISPLAY "Qual seu Nome?".
           ACCEPT NOME.
      *    O MOVE está atribuindo a string "ola" para varivel MINHA-MSG
           MOVE "Ola" TO MINHA-MENSAGEM.
      *    Atribui "1" int a variavel NUMERO
           MOVE 1 TO NUMERO.
           DISPLAY "Mensagem " NUMERO ": " MINHA-MENSAGEM NOME.

      *    Aki o string "olá" é subscrita pela string "Tchau"
      *    Ele não vai guardar o dado se o mesmo for subscrito
           MOVE "Tchau" TO MINHA-MENSAGEM.

      *    Aki a msm coisa "2" vai sobscrever o "1"
           MOVE 2 TO NUMERO.
           DISPLAY "Mensagem " NUMERO ": " MINHA-MENSAGEM NOME.

       PROGRAM-DONE.
           STOP RUN.
