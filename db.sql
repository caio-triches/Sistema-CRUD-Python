CREATE DATABASE academia_flask;
USE academia_flask;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60),
    idade INT,
    plano VARCHAR(20)
);


CREATE TABLE treinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60),
    nivel VARCHAR(20),
    duracao INT
);

INSERT INTO treinos (nome, nivel, duracao) VALUES
('Treino Iniciante', 'Fácil', 30),
('Treino Intermediário', 'Médio', 45),
('Treino Avançado', 'Difícil', 60),
('Treino Cardio', 'Médio', 40),
('Treino de Força', 'Difícil', 50),
('Treino de Resistência', 'Médio', 55),
('Treino de Abdômen', 'Fácil', 25),
('Treino Funcional', 'Médio', 35),
('Treino de Pernas', 'Difícil', 50),
('Treino de Braços', 'Médio', 40),
('Treino HIIT', 'Difícil', 30),
('Treino Alongamento', 'Fácil', 20),
('Treino de Mobilidade', 'Fácil', 25),
('Treino de Potência', 'Difícil', 45),
('Treino Full Body', 'Médio', 60);

INSERT INTO alunos (nome, idade, plano) VALUES
('Lucas Almeida', 25, 'Mensal'),
('Carla Souza', 32, 'Trimestral'),
('Rafaela Torres', 20, 'Semestral'),
('Pedro Henrique', 27, 'Mensal'),
('Mariana Lopes', 22, 'Anual'),
('João Pereira', 30, 'Semestral'),
('Fernanda Silva', 28, 'Mensal'),
('Ricardo Gomes', 35, 'Anual'),
('Beatriz Castro', 21, 'Trimestral'),
('André Moura', 26, 'Mensal');
