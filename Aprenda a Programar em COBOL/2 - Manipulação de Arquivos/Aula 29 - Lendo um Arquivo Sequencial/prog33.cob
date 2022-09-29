       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG33.
      *    Programa para Ler Arquivos

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT OPTIONAL ARQUIVO-CLIENTE
           ASSIGN TO "clientes.dat"
           ORGANISATION IS SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD ARQUIVO-CLIENTE.

       01  CLIENTE-REGISTRO.
           05 CLIENTE-NOME PIC X(20).
           05 CLIENTE-ENDERECO PIC X(50).
           05 CLIENTE-TELEFONE PIC X(15).
           05 CLIENTE-EMAIL PIC X(30).

       WORKING-STORAGE SECTION.

       01  FINAL-ARQUIVO PIC X.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           OPEN INPUT ARQUIVO-CLIENTE.

           MOVE "N" TO FINAL-ARQUIVO.

           PERFORM LER-PROXIMO-REGISTRO.
      *    Fazer a função e no final atribuir valor "S" no FINAL-ARQUIVO +++++, bora da 1 mudada
           PERFORM EXIBIR-REGISTRO UNTIL FINAL-ARQUIVO NOT = "N".
      *    ERA = "S", +eu mudei pq a logica era fazer até ser diferente

           CLOSE ARQUIVO-CLIENTE.

       PROGRAM-DONE.
           STOP RUN.

       LER-PROXIMO-REGISTRO.
      *    Ler o Arquivo e quando ele achar o final dele Atribua "S" no FINAL-ARQUIVO
           READ ARQUIVO-CLIENTE RECORD AT END MOVE "S" TO FINAL-ARQUIVO.
      *    KD vez q essa parte roda ela le 1 unico registro por vez

       EXIBIR-REGISTRO.
           PERFORM CAMPOS.
           PERFORM LER-PROXIMO-REGISTRO.

       CAMPOS.
           DISPLAY "NOME: " CLIENTE-NOME.
           DISPLAY "ENDERECO: " CLIENTE-ENDERECO.
           DISPLAY "TELEFONE: " CLIENTE-TELEFONE.
           DISPLAY "EMAIL: " CLIENTE-EMAIL.
           DISPLAY "=======================".
