import sqlite3

def tempo():
   import time
   time.sleep(3)
def limpar():
   import os
   os.system("cls")


class Aluno:
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, rgm=""):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.rgm = rgm

    def imc(self):
        resultado = self.peso / (self.altura * self.altura)
        if resultado >= 40.0 :
            return "Obesidade classe III"
        elif resultado >= 35.0:
            return "Obesidade classe II"
        elif resultado >= 30.0 :
            return "Obesidade classe I"
        elif resultado >= 25.0:
            return "Excesso de Peso"
        elif resultado >= 18.5:
            return "Peso Normal"
        if resultado < 18.5:
            return "Abaixo do peso normal"

class Professor:
    def __init__(self, nome="", idade=0, altura=0.0, peso=0.0, matricula=""):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.matricula = matricula

class Disciplina:
  def __init__(self, codigo="", nome="", cargaHoraria=160, turma="", notaMinima=7):
      self.codigo = codigo
      self.nome = nome
      self.cargaHoraria = cargaHoraria
      self.turma = turma
      self.notaMinima = notaMinima

class ModuloAcademico:
    def __init__(self):
        self.opcao = 0
        self.listaAlunos = []
        self.listaProfessores = []
        self.listaDisciplinas = []

        self.RecuperarAlunos()
        self.recuperarProfessores()
        self.recuperarDisciplinas()

    def cadastrarAluno(self):
        while True:
          try:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            altura = float(input("Digite a altura do aluno: "))
            peso = float(input("Digite o peso do aluno: "))
            RGM = input("Digite o RGM do aluno: ")
            aluno = Aluno(nome, idade, altura, peso, RGM)
            self.listaAlunos.append(aluno)
            self.salvarAlunos()
            break

          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue

    def cadastrarProfessor(self):
        while True:
          try:
            nome = input("Digite o nome do professor: ")
            idade = int(input("Digite a idade do professor: "))
            altura = float(input("Digite a altura do professor: "))
            peso = float(input("Digite o peso do professor: "))
            matricula = input("Digite a matricula do aluno: ")
            professor = Professor(nome, idade, altura, peso, matricula)
            self.listaProfessores.append(professor)
            self.salvarProfessores()
            break

          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue

    def cadastrarDisciplina(self):
        while True:
          try:
            codigo = input("Digite o codigo da disciplina: ")
            nome = input("Digite o nome da disciplina: ")
            cargaHoraria = int(input("Digite a carga horaria da disciplina: "))
            turma = input("Digite a turma da disciplina: ")
            notaMinima = float(input("Digite a nota minima da disciplina: "))
            disciplina = Disciplina(codigo, nome, cargaHoraria, turma, notaMinima)
            self.listaDisciplinas.append(disciplina)
            self.salvarDisciplinas()
            break

          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue


    def imprimirAluno(self):
      print("|Alunos:")
      print("|Nome|Idade|Altura|Peso|RGM")
      print("-------------------------------")
      for a in self.listaAlunos :
        print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso, "|", a.rgm)
      print("-------------------------------")

    def imprimirProfessor(self):
      print("|Professores:")
      print("|Nome|Idade|Altura|Peso|Matricula")
      print("-------------------------------")
      for a in self.listaProfessores :
        print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso, "|", a.matricula)
      print("-------------------------------")

    def imprimirDisciplina(self):
      print("|Disciplinas:")
      print("|Codigo|Nome|CargaHoraria|Turma|NotaMinima")
      print("-------------------------------")
      for a in self.listaDisciplinas :
        print(a.codigo, "|", a.nome, "|", a.cargaHoraria, "|", a.turma, "|", a.notaMinima)
      print("-------------------------------")


    def removerAluno(self):
        while True:
            try:
                RGM = input("Digite o RGM do aluno a ser removido: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()

                cursor.execute('SELECT * FROM ALUNO WHERE RGM = ?;', (RGM,))
                aluno_existente = cursor.fetchone()

                if aluno_existente:
                    cursor.execute('DELETE FROM ALUNO WHERE RGM = ?;', (RGM,))
                    conexao.commit()
                    conexao.close()

                    for aluno in self.listaAlunos:
                        if aluno.rgm == RGM:
                            self.listaAlunos.remove(aluno)
                            break
                          
                    print(f"Aluno com RGM {RGM} removido do banco de dados e da lista.")
                    self.salvarAlunos()
                    break
                else:
                    print("Aluno não encontrado no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao remover aluno:", error)
                break

    def removerProfessor(self):
        while True:
            try:
                matricula = input("Digite a matrícula do professor a ser removido: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()

                cursor.execute('SELECT * FROM PROFESSOR WHERE MATRICULA = ?;', (matricula,))
                professor_existente = cursor.fetchone()

                if professor_existente:
                    cursor.execute('DELETE FROM PROFESSOR WHERE MATRICULA = ?;', (matricula,))
                    conexao.commit()
                    conexao.close()

                    for professor in self.listaProfessores:
                        if professor.matricula == matricula:
                            self.listaProfessores.remove(professor)
                            break
                          
                    print(f"Professor com matrícula {matricula} removido do banco de dados e da lista.")
                    self.salvarProfessores() 
                    break
                else:
                    print("Professor não encontrado no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao remover professor:", error)
                break

    def removerDisciplina(self):
        while True:
            try:
                codigo = input("Digite o código da disciplina a ser removida: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()

                cursor.execute('SELECT * FROM DISCIPLINA WHERE CODIGO = ?;', (codigo,))
                disciplina_existente = cursor.fetchone()

                if disciplina_existente:
                    cursor.execute('DELETE FROM DISCIPLINA WHERE CODIGO = ?;', (codigo,))
                    conexao.commit()
                    conexao.close()

                    for disciplina in self.listaDisciplinas:
                        if disciplina.codigo == codigo:
                            self.listaDisciplinas.remove(disciplina)
                            break
                          
                    print(f"Disciplina com código {codigo} removida do banco de dados e da lista.")
                    self.salvarDisciplinas()  
                    break
                else:
                    print("Disciplina não encontrada no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao remover disciplina:", error)
                break


    def RecuperarAlunos(self):
       try:
           conexao = sqlite3.connect('FACULDADE.db')
           cursor = conexao.cursor()
           retorno = cursor.execute('SELECT * FROM ALUNO;')

           for linha in retorno:
               nome, idade, altura, peso, rgm = linha
               aluno = Aluno(nome, idade, altura, peso, rgm)
               self.listaAlunos.append(aluno)

           conexao.commit()
           conexao.close()

       except sqlite3.Error as error:
           print("Erro ao recuperar alunos:", error)

    def recuperarProfessores(self):
      try:
          conexao = sqlite3.connect('FACULDADE.db')
          cursor = conexao.cursor()
          retorno = cursor.execute('SELECT * FROM PROFESSOR;')
          for linha in retorno:
              nome, idade, altura, peso, matricula = linha
              professor = Professor(nome, idade, altura, peso, matricula)
              self.listaProfessores.append(professor)
          conexao.commit()
          conexao.close()
      except sqlite3.Error as error:
          print("Erro ao recuperar Professores:", error)

    def recuperarDisciplinas(self):
      try:
          conexao = sqlite3.connect('FACULDADE.db')
          cursor = conexao.cursor()
          retorno = cursor.execute('SELECT * FROM DISCIPLINA;')

          for linha in retorno:
              codigo, nome, cargaHoraria, turma, notaMinima = linha
              disciplina = Disciplina(codigo, nome, cargaHoraria, turma, notaMinima)
              self.listaDisciplinas.append(disciplina)

          conexao.commit()
          conexao.close()
      except sqlite3.Error as error:
           print("Erro ao recuperar Professores:", error)


    def atualizarAluno(self):
        while True:
            try:
                busca = input("Digite o RGM do aluno a ser atualizado: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()

                cursor.execute('SELECT * FROM ALUNO WHERE RGM = ?;', (busca,))
                aluno_existente = cursor.fetchone()

                if aluno_existente:
                    novo_nome = input("Digite o novo nome do aluno: ")
                    nova_idade = int(input("Digite a nova idade do aluno: "))
                    nova_altura = float(input("Digite a nova altura do aluno: "))
                    novo_peso = float(input("Digite o novo peso do aluno: "))

                    cursor.execute('UPDATE ALUNO SET NOME = ?, IDADE = ?, ALTURA = ?, PESO = ? WHERE RGM = ?;',
                                   (novo_nome, nova_idade, nova_altura, novo_peso, busca))
                    conexao.commit()
                    conexao.close()

                    for aluno in self.listaAlunos:
                        if aluno.rgm == busca:
                            aluno.nome = novo_nome
                            aluno.idade = nova_idade
                            aluno.altura = nova_altura
                            aluno.peso = novo_peso
                            break

                    print(f"Aluno com RGM {busca} atualizado no banco de dados e na lista.")
                    self.salvarAlunos()
                    break
                else:
                    print("Aluno não encontrado no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao atualizar aluno:", error)
                break

    def atualizarProfessor(self):
        while True:
            try:
                busca = input("Digite a Matricula do Professor a ser atualizado: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()
    
                cursor.execute('SELECT * FROM PROFESSOR WHERE MATRICULA = ?;', (busca,))
                aluno_existente = cursor.fetchone()
    
                if aluno_existente:
                    novo_nome = input("Digite o novo nome do professor: ")
                    nova_idade = int(input("Digite a nova idade do professor: "))
                    nova_altura = float(input("Digite a nova altura do professor: "))
                    novo_peso = float(input("Digite o novo peso do professor: "))
    
                    cursor.execute('UPDATE PROFESSOR SET NOME = ?, IDADE = ?, ALTURA = ?, PESO = ? WHERE MATRICULA = ?;',
                                   (novo_nome, nova_idade, nova_altura, novo_peso, busca))
                    conexao.commit()
                    conexao.close()

                    for professor in self.listaProfessores:
                        if professor.matricula == busca:
                            professor.nome = novo_nome
                            professor.idade = nova_idade
                            professor.altura = nova_altura
                            professor.peso = novo_peso
                            break
                        
                    print(f"Professor com Matricula {busca} atualizado no banco de dados e na lista.")
                    self.salvarProfessores() 
                    break
                else:
                    print("Professor não encontrado no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao atualizar professor:", error)
                break

    def atualizarDisciplina(self):
        while True:
            try:
                busca = input("Digite o codigo da disciplina a ser atualizada: ")
                conexao = sqlite3.connect('FACULDADE.db')
                cursor = conexao.cursor()
    
                cursor.execute('SELECT * FROM DISCIPLINA WHERE CODIGO = ?;', (busca,))
                disciplina_existente = cursor.fetchone()
    
                if disciplina_existente:
                    novo_nome = input("Digite o novo nome da disciplina: ")
                    nova_cargaHoraria = int(input("Digite a nova carga Horaria da disciplina: "))
                    nova_turma = input("Digite a nova turma da disciplina: ")
                    novo_notaMinima = float(input("Digite a nova nota minima da disciplina: "))
    
                    cursor.execute('UPDATE DISCIPLINA SET NOME = ?, CARGAHORARIA = ?, TURMA = ?, NOTAMINIMA = ? WHERE CODIGO = ?;',
                                   (novo_nome, nova_cargaHoraria, nova_turma, novo_notaMinima, busca))
                    conexao.commit()
                    conexao.close()
    
                    for disciplina in self.listaDisciplinas:
                        if disciplina.codigo == busca:
                            disciplina.nome = novo_nome
                            disciplina.cargaHoraria = nova_cargaHoraria
                            disciplina.turma = nova_turma
                            disciplina.notaMinima = novo_notaMinima
                            break
                        
                    print(f"Disciplina com codigo {busca} atualizado no banco de dados e na lista.")
                    self.salvarDisciplinas()  
                    break
                else:
                    print("Professor não encontrado no banco de dados.")
                    break
            except sqlite3.Error as error:
                print("Erro ao atualizar Disciplina:", error)
                break

    def salvarAlunos(self):
      while True:
          try:
            import sqlite3
            conexao = sqlite3.connect('FACULDADE.db')
            cursor = conexao.cursor()
            for aluno in self.listaAlunos:
              cursor.execute(f"INSERT INTO ALUNO (NOME, IDADE, ALTURA, PESO, RGM) VALUES (?, ?, ?, ?, ?);",
                             (aluno.nome, aluno.idade, aluno.altura, aluno.peso, aluno.rgm))
            conexao.commit()
            conexao.close()
            break
          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue

    def salvarProfessores(self):
      while True:
          try:
            import sqlite3
            conexao = sqlite3.connect('FACULDADE.db')
            cursor = conexao.cursor()
            for professor in self.listaProfessores:
              cursor.execute(f"INSERT INTO PROFESSOR (NOME, IDADE, ALTURA, PESO, MATRICULA) VALUES (?, ?, ?, ?, ?);",
                             (professor.nome, professor.idade, professor.altura, professor.peso, professor.matricula))
            conexao.commit()
            conexao.close()
            break
          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue

    def salvarDisciplinas(self):
      while True:
          try:
            import sqlite3
            conexao = sqlite3.connect('FACULDADE.db')
            cursor = conexao.cursor()
            for disciplina in self.listaDisciplinas:
              cursor.execute(f"INSERT INTO DISCIPLINA (CODIGO, NOME, CARGAHORARIA, TURMA, NOTAMINIMA) VALUES (?, ?, ?, ?, ?);",
                             (disciplina.codigo, disciplina.nome, disciplina.cargaHoraria, disciplina.turma, disciplina.notaMinima))
            conexao.commit()
            conexao.close()
            break
          except ValueError:
            print("Algum dado foi inserido de forma incorreta, tente novamente")
            tempo()
            limpar()
            continue


    def consultarAlunos65plus(self):
        contador = 0
        for a in self.listaAlunos :
            if a.peso > 65:
                contador += 1
        print("Quantidade de alunos > 65 kg eh: ", contador)
        for a in self.listaAlunos :
            if a.peso > 65:
                print("O aluno ", a.nome, " tem imc: ", a.imc())

    def executar(self):
        while True:
            print("|############################################################|")
            print("|    ----------     OOP PYTHON        ------- | ")
            print("|############################################################|")
            print("   -- ALUNOS --  ")
            print(" 1) Cadastrar Alunos")
            print(" 2) Imprimir Alunos")
            print(" 3) Remover Alunos")
            print(" 4) Atualizar Alunos")
            print(" 5) Consulta Alunos > 65 Kg:")
            print(" ")
            print("   -- PROFESSOR --  ")
            print(" 11) Cadastrar Professor")
            print(" 12) Imprimir Professor")
            print(" 13) Remover Professor")
            print(" 14) Atualizar Professor")
            print("")
            print("   -- DISCIPLINA --  ")
            print(" 21) Cadastrar Disciplina")
            print(" 22) Imprimir Disciplina")
            print(" 23) Remover Disciplina")
            print(" 24) Atualizar Disciplina")
            print("")
            print("0 - Sair")

            self.opcao = input("Escolha uma opcao: ")
            if self.opcao == "1":
                limpar()
                self.cadastrarAluno()
                tempo()
                limpar()

            elif self.opcao == "2":
                limpar()
                self.imprimirAluno()
                tempo()
                limpar()

            elif self.opcao == "3":
                limpar()
                self.removerAluno()
                tempo()
                limpar()

            elif self.opcao == "4":
                limpar()
                self.atualizarAluno()
                tempo()
                limpar()
            
            elif self.opcao == "5":
                limpar()
                self.consultarAlunos65plus()
                tempo()
                limpar()

            elif self.opcao == "11":
                limpar()
                self.cadastrarProfessor()
                tempo()
                limpar()
            
            elif self.opcao == "12":
               limpar()
               self.imprimirProfessor()
               tempo()
               limpar()
            
            elif self.opcao == "13":
               limpar()
               self.removerProfessor()
               tempo()
               limpar()
            
            elif self.opcao == "14":
                limpar()
                self.atualizarProfessor()
                tempo()
                limpar()

            elif self.opcao == "21":
                limpar()
                self.cadastrarDisciplina()
                tempo()
                limpar()
            
            elif self.opcao == "22":
                limpar()
                self.imprimirDisciplina()
                tempo()
                limpar()
            
            elif self.opcao == "23":
                limpar()
                self.removerDisciplina()
                tempo()
                limpar()
            
            elif self.opcao == "24":
                limpar()
                self.atualizarDisciplina()
                tempo()
                limpar()
            
            elif self.opcao == "0":
                break
            
            else:
                print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    modulo_academico = ModuloAcademico()
    modulo_academico.executar()