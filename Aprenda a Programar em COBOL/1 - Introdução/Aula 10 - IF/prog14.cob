       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG14.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Perguntar ao Usuario se ele Gosta de Churrasco
      *    Resolvendo o Problama das Letras

       WORKING-STORAGE SECTION.

       01  RESPOSTA PIC X.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           PERFORM PERGUNTA.

           PERFORM CONVERTER.

           PERFORM EXIBE-RESPOSTA.

       PROGRAM-DONE.
           STOP RUN.

       PERGUNTA.
           DISPLAY "VC Gosta de Churrasco? (S/N)".
           ACCEPT RESPOSTA.

       CONVERTER.
           IF RESPOSTA = "s"
               MOVE "S" TO RESPOSTA.

           IF RESPOSTA IS EQUAL "n"
               MOVE "N" TO RESPOSTA.

       EXIBE-RESPOSTA.
           *>IF RESPOSTA = "S"*> TAMBÉM FUNCIONA
           IF RESPOSTA IS EQUAL "S" *> Não colcoar ponto final nas condições dos ifs*>
               DISPLAY "É Logico Porra, É BOM DE ++".

           IF RESPOSTA = "N"
               DISPLAY "Maldito Herbivoro".
