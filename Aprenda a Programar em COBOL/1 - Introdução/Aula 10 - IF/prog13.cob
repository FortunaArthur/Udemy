       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG13.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Perguntar ao Usuario se ele Gosta de Churrasco

       WORKING-STORAGE SECTION.

       01  RESPOSTA PIC X.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           PERFORM PERGUNTA.

           PERFORM EXIBE-RESPOSTA.

       PROGRAM-DONE.
           STOP RUN.

       PERGUNTA.
           DISPLAY "VC Gosta de Churrasco? (S/N)".
           ACCEPT RESPOSTA.

       EXIBE-RESPOSTA.
           *>IF RESPOSTA = "S"*> TAMB�M FUNCIONA
           IF RESPOSTA IS EQUAL "S" *> N�o colcoar ponto final nas condi��es dos ifs*>
               DISPLAY "� Logico Porra, � BOM DE ++".

           IF RESPOSTA = "N"
               DISPLAY "Maldito Herbivoro".

      *    LEMBRETE, ELE s� vai aceitar Respostas de S/N em Maiusculo
