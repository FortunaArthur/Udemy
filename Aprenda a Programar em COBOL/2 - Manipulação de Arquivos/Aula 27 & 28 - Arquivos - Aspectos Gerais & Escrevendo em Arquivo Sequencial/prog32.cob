       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG32.
      *    Programa para Manipular Arquivos

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION. *>AKI VC ESTÁ CRIANDO O NOME E O TIPO DO ARQUIVO QUE OS DADOS SERÃO SALVOS*>
       FILE-CONTROL.
           SELECT OPTIONAL ARQUIVO-CLIENTE
           ASSIGN TO "clientes.dat"
           ORGANISATION IS SEQUENTIAL. *> aki é a forma de organização dos dados, pelo q parece*>

       DATA DIVISION.
       FILE SECTION.
       FD ARQUIVO-CLIENTE.

       01  CLIENTE-REGISTRO.
           05 CLIENTE-NOME PIC X(20).
           05 CLIENTE-ENDERECO PIC X(50).
           05 CLIENTE-TELEFONE PIC X(15).
           05 CLIENTE-EMAIL PIC X(30).

       WORKING-STORAGE SECTION.

       01  RESPOSTA PIC X.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           OPEN EXTEND ARQUIVO-CLIENTE. *> aki abre o registro*>

           MOVE "S" TO RESPOSTA.

           PERFORM ADCIONA-REGISTROS UNTIL RESPOSTA = "N".
      * Faz o ADICIONA-REGISTROS e PARE quando RESPOSTA = "N"

           CLOSE ARQUIVO-CLIENTE.*>aki fecha o programa, se a passar do PERFORM*>

       PROGRAM-DONE.
           STOP RUN.

       ADCIONA-REGISTROS.
           MOVE SPACE TO CLIENTE-REGISTRO. *> Iniciar o registro com espaço em branco*>
           DISPLAY "Informe o Nome:".
           ACCEPT CLIENTE-NOME.
           DISPLAY "Informe o Endereço:"
           ACCEPT CLIENTE-ENDERECO.
           DISPLAY "Informe o Telefone:"
           ACCEPT CLIENTE-TELEFONE.
           DISPLAY "Informe o Email".
           ACCEPT CLIENTE-EMAIL.

           WRITE CLIENTE-REGISTRO.*> aki ele escreve no arquivo*>

           DISPLAY "-------------"
           DISPLAY "Deseja Adcionar Outro Cliente? (S/N)".
           ACCEPT RESPOSTA.
