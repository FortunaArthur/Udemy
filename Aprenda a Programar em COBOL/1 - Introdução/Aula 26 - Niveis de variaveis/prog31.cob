       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROG31.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
      *    Demonstração Niveis de Variaveis

       WORKING-STORAGE SECTION.

       77  NOME PIC X(10).

       01  PESSOA. *> RECORD*>
           05 ESCOLARIDADE PIC X.
               88 ENSINO-FUNDAMENTAL VALUE "F".
               88 ENSINO-MEDIO VALUE "M".
               88 ENSINO-SUPERIOR VALUE "S".

       01  FUNCIONARIO.
           05 CODIGO PIC 99.
           05 FILLER PIC X(1) VALUE "*".
           05 IDADE PIC 99.
           05 FILLER PIC X(1) VALUE "*".
           05 ENDERECO PIC X(20).

       66  DETALHES RENAMES CODIGO THRU IDADE.
      *    VAI IMCORPROTAR AS VARIAVEIS CODIGO ATÉ IDADE.

       PROCEDURE DIVISION.
       PROGRAM-BEGIN.

           DISPLAY "==== VARIEVEIS NIVEL 77 E 88 ===="
           DISPLAY "Qual seu Nome?"
           ACCEPT NOME.
           DISPLAY "Qual sua Escolaridade?".
           DISPLAY "F -- ENSINO-FUNDAMENTAL".
           DISPLAY "M -- ENSINO-MEDIO".
           DISPLAY "S -- ENSINO-SUPERIOR".
           ACCEPT ESCOLARIDADE.

           IF ESCOLARIDADE = "F" *>AKI VC ATRIBIU O REGISTRO, NÃO AS VARIAVEIS DENTRO DELE*>
               DISPLAY "VC ESTA NO INICIO DOS ESTUDOS".

           IF ESCOLARIDADE = "M"
               DISPLAY "VC ESTA NO FIM DA TORTURA".

           IF ESCOLARIDADE = "S"
               DISPLAY "VC ESTA NA FACUL, BOA SORTE".
      *    Parece 1 IF Comum, + como tem 3 Variaveis ele Otimiza o Processo pra ficar + Rapido que 1 IF Normal
      *    Devido sua Base de comparação, que são as 3 variaveis

           DISPLAY "==== VARIAVEIS NIVEL 66 ====".
           DISPLAY "Informe o Codigo do Funcionario"
           ACCEPT CODIGO.
           DISPLAY "Informe a Idade do FUNCIONARIO".
           ACCEPT IDADE.
           DISPLAY "Informe o Endereco do Funcionario".
           ACCEPT ENDERECO.

           DISPLAY "==== EXIBINDO DETALHES ===="
           DISPLAY DETALHES.

       PROGRAM-DONE.
           STOP RUN.
