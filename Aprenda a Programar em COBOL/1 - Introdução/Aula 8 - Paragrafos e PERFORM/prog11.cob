       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG11.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Programa Para Exibir Mensagens, Agora Usando Paragrafos

       WORKING-STORAGE SECTION.

       01  MENSAGEM PIC X(80).
       01  ID-MENSAGEM PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.

           MOVE 0 TO ID-MENSAGEM.*>Iniciando a Variavel Antes de Usar (Boa Pratica)
      *    1° Mensagem
           MOVE " Sanchez, Vai Logo Marca a Maldita Reunião dos Mamacos"
            TO MENSAGEM.

           PERFORM ADICIONAR-ID.

      *    2° Mensagem
           MOVE " Mamaco, VC e os Larapios Comandam a Reunião Agora" TO
            MENSAGEM.

           PERFORM ADICIONAR-ID.

       PROGRAM-DONE.
           STOP RUN.

       ADICIONAR-ID.
           ADD 1 TO ID-MENSAGEM.
           DISPLAY
               ID-MENSAGEM
               MENSAGEM.
