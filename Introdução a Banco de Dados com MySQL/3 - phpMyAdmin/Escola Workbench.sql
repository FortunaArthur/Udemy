create database escola;
use escola;

CREATE TABLE `alunos` (
  `NOME` varchar(255) DEFAULT NULL,
  `EMAIL` varchar(255) DEFAULT NULL,
  `DATA_NASCIMENTO` date DEFAULT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `alunos` (`NOME`, `EMAIL`, `DATA_NASCIMENTO`, `ID`) VALUES
('Pedro Martins', 'aluno1@gmail.com', '1987-07-17', 2),
('Diego Mariano', 'aluno2@gmail.com', '1990-01-01', 3),
('Felipe Ana Maria Braga', 'aluno3@gmail.com', '2017-01-01', 4),
('Pedro Martins', 'aluno4@gmail.com', '1997-02-13', 5),
('REGINA CAZÉ', 'aluno5@gmail.com', '1920-01-01', 6);

CREATE TABLE `cursos` (
  `NOME` varchar(255) DEFAULT NULL,
  `DURACAO` varchar(20) DEFAULT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `cursos` (`NOME`, `DURACAO`, `ID`) VALUES
('Cascinagem', '4H', 1);

CREATE TABLE `alunos_cursos` (
  `ID` int(11) NOT NULL,
  `ID_ALUNO` int(11) NOT NULL,
  `ID_CURSO` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `alunos_cursos` (`ID`, `ID_ALUNO`, `ID_CURSO`) VALUES
(1, 4, 1);


