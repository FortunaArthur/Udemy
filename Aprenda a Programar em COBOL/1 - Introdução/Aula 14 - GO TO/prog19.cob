       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG19.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

       WORKING-STORAGE SECTION.

       01  RESPOSTA PIC X.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.
           DISPLAY "Inicio do Programa"
           PERFORM CONTINUAR.

      *    Ele vai ignorar a 2� Parte com o GO TO se entrar no IF
           IF RESPOSTA = "N"
               GO TO MENSAGEM.

      *    Se n�o entrar ele continua a execu��o dento do PROGRAM-BEGIN
           DISPLAY "Segunda Parte do Programa".
           PERFORM LOGICA.

       PROGRAM-DONE.
           STOP RUN.

       CONTINUAR.*> esse Paragrafo ta s� tranformando minuscula pra maiuscula*>
           DISPLAY "CONTINUAR? (S/N)"
           ACCEPT RESPOSTA.
           IF RESPOSTA = "n"
               MOVE "N" TO RESPOSTA.

       LOGICA.
           DISPLAY "O Programa s� Mostra 1 Mensagem".

       MENSAGEM.
           DISPLAY "T� DE MADRUGADA".

       PROFISSAO.
           DISPLAY "PROGRAMADOR".
