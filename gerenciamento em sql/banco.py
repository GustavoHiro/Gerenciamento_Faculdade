import sqlite3
conexao = sqlite3.connect('FACULDADE.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE ALUNO(NOME TEXT, IDADE INT, ALTURA FLOAT,PESO FLOAT, RGM INT PRIMARY KEY );')
cursor.execute('CREATE TABLE PROFESSOR(NOME TEXT, IDADE INT, ALTURA FLOAT,PESO FLOAT, MATRICULA INT PRIMARY KEY );')
cursor.execute('CREATE TABLE DISCIPLINA( CODIGO INT PRIMARY KEY, NOME TEXT, CARGAHORARIA TEXT, TURMA TEXT,NOTAMINIMA FLOAT );')
conexao.commit()
conexao.close()


