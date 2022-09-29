       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG37.
      *    Programa para Inserir Dados em Arquivos Indexados
      *    WRITE COM INVALID KEY
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           COPY "SELFUNCIONARIO.cob".

       DATA DIVISION.
       FILE SECTION.

           COPY "FDFUNCIONARIO.cob".

       WORKING-STORAGE SECTION.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.
      *    aKI � S� PRA CRIAR E FECHAR
           OPEN I-O ARQUIVO-FUNCIONARIO.

           PERFORM LER-ESCREVER-REGISTRO.

           CLOSE ARQUIVO-FUNCIONARIO.

       PROGRAM-DONE.
           STOP RUN.

       LER-ESCREVER-REGISTRO.
           MOVE SPACES TO FUNCIONARIO-REGISTRO.
           MOVE ZEROS TO FUNCIONARIO-CODIGO.
           DISPLAY "INFORME O CODIGO DO FUNCIONARIO (1-9999)".
           ACCEPT FUNCIONARIO-CODIGO.
           DISPLAY "INFORME O NOME DO FUNCIONARIO:"
           ACCEPT FUNCIONARIO-NOME.
           DISPLAY "INFORME O ENDERECO DO FUNCIONARIO:"
           ACCEPT FUNCIONARIO-ENDERECO.
           DISPLAY "INFORME O TELEFONE DO FUNCIONARIO:"
           ACCEPT FUNCIONARIO-TELEFONE.
           DISPLAY "INFORME O EMAIL DO FUNCIONARIO:"
           ACCEPT FUNCIONARIO-EMAIL.

           WRITE FUNCIONARIO-REGISTRO INVALID KEY
           DISPLAY "CODIGO " FUNCIONARIO-CODIGO " JA CADASTRADO".
