       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG9.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Programa pra demosntrar o uso de PERFORM
       PROCEDURE DIVISION.

       PROGRAM-BEGIN.
           DISPLAY "A Mensagem do Dia".
           PERFORM MENSAGEM.
           DISPLAY "CONCORDA?".

       PROGRAM-DONE.
           STOP RUN.

      *    Todos os Paragrafos VC Coloca Depois do STOP RUN

       MENSAGEM.
           DISPLAY "Isto eh um Programa em COBOL, Legal!".

      *    O Programa vai mostrar o 1° DISPLAY, Vai procurar o Paragrafo
      *    Vai Executar os Comandos do Paragrafo, Feito Isso
      *    O Programa executa o 2° Dispplay e encerra

      *    Cada DISPLAY é Mostrado em Linhas Diferentes
