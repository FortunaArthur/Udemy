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
           *>IF RESPOSTA = "S"*> TAMBÉM FUNCIONA
           IF RESPOSTA IS EQUAL "S" *> Não colcoar ponto final nas condições dos ifs*>
               DISPLAY "É Logico Porra, É BOM DE ++".

           IF RESPOSTA = "N"
               DISPLAY "Maldito Herbivoro".

      *    LEMBRETE, ELE só vai aceitar Respostas de S/N em Maiusculo
