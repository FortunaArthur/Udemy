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

      *    Ele vai ignorar a 2° Parte com o GO TO se entrar no IF
           IF RESPOSTA = "N"
               GO TO MENSAGEM.

      *    Se não entrar ele continua a execução dento do PROGRAM-BEGIN
           DISPLAY "Segunda Parte do Programa".
           PERFORM LOGICA.

       PROGRAM-DONE.
           STOP RUN.

       CONTINUAR.*> esse Paragrafo ta só tranformando minuscula pra maiuscula*>
           DISPLAY "CONTINUAR? (S/N)"
           ACCEPT RESPOSTA.
           IF RESPOSTA = "n"
               MOVE "N" TO RESPOSTA.

       LOGICA.
           DISPLAY "O Programa só Mostra 1 Mensagem".

       MENSAGEM.
           DISPLAY "TÁ DE MADRUGADA".

       PROFISSAO.
           DISPLAY "PROGRAMADOR".
