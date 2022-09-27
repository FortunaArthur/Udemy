       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG10.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Programa Para Exibir Mensagens

       WORKING-STORAGE SECTION.

       01  MENSAGEM PIC X(80).
       01  ID-MENSAGEM PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.

           MOVE 0 TO ID-MENSAGEM.*>Iniciando a Variavel Antes de Usar (Boa Pratica)
      *    1° Mensagem
           MOVE " Sanchez, Vai Logo Marca a Maldita Reunião dos Mamacos"
            TO MENSAGEM.
           ADD 1 TO ID-MENSAGEM.
           DISPLAY ID-MENSAGEM MENSAGEM.

      *    2° Mensagem
           MOVE " Mamaco, VC e os Larapios Comandam a Reunião Agora" TO
            MENSAGEM.
           ADD 1 TO ID-MENSAGEM.
           DISPLAY
               ID-MENSAGEM
               MENSAGEM.

       PROGRAM-DONE.
           STOP RUN.
      *    Repare que 1 comando se repetiu, que foi ADD 1 TO ID-MENSAGEM.
      *    No Proximo Codigo Vamos adicionar Paragrafo pra resolver essa repetição
