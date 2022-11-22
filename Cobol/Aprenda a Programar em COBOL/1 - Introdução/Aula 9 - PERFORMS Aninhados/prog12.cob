       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG12.
       ENVIRONMENT DIVISION.
       DATA DIVISION.

      *    Programa Para Exibir Mensagens, Agora Usando Paragrafos Aninhados

       WORKING-STORAGE SECTION.

       01  MENSAGEM PIC X(80).
       01  ID-MENSAGEM PIC 9(2).

       PROCEDURE DIVISION.

       PROGRAM-BEGIN.

           MOVE 0 TO ID-MENSAGEM.*>Iniciando a Variavel Antes de Usar (Boa Pratica)
      *    1� Mensagem
           MOVE " Sanchez, Vai Logo Marca a Maldita Reuni�o dos Mamacos"
            TO MENSAGEM.

           PERFORM ADICIONAR-ID.

      *    2� Mensagem
           MOVE " Mamaco, VC e os Larapios Comandam a Reuni�o Agora" TO
            MENSAGEM.

           PERFORM ADICIONAR-ID.

       PROGRAM-DONE.
           STOP RUN.

       ADICIONAR-ID.
      *    Aki Entram os Performs dentro do Perform, OU SEJA, Perforoms Aninhados
           PERFORM AUMENTAR-ID.
           PERFORM PRINTAR-MENSAGEM.

       AUMENTAR-ID.
           ADD 1 TO ID-MENSAGEM.

       PRINTAR-MENSAGEM.
           DISPLAY
               ID-MENSAGEM
               MENSAGEM.
      *    Repare que o Programa � o Mesmo, ele s� mudou a Forma, de uma outra maneira
      *    Pense no Perform como fun��o, e os performs aninhados s�o
      *    Fun��es dentro de Fun��es

      *    1� Roda o 1� MOVE, 2� Vai Rodar o ADICIONAR-ID. depois dentro DELE
      *    Vai Rodar o  AUMENTAR-ID e PRINTAR-MENSAGEM, Feito isso
      *    Vai para 2� Mensagem que repete o ciclo
