from importantes.consultas import consulta_matricula, consulta_cursos, consulta_alunos
from importantes.interface import gerar_titulo, gerar_opcoes
from importantes.constants import CONSULTAS

with open("alunos.txt", "r", encoding="utf8") as alunos:
    gerar_opcoes(CONSULTAS)

    escolha = int(input("\n> "))
    if escolha-1 in range(3):
        if escolha == 1:
            matricula = input("Digite a matrícula: ")
            resultado = consulta_matricula(alunos, matricula)

            gerar_titulo("Resultado da Matrícula")
            print(resultado)
        elif escolha == 2:
            nome = input("Digite o nome do aluno: ").title()
            resultado = consulta_alunos(alunos, nome)

            gerar_titulo("Resultado do Nome do Aluno")
            for dado in resultado:
                print(dado)
        elif escolha == 3:
            curso = input("Digite o curso: ")
            resultado = consulta_cursos(alunos, curso)

            gerar_titulo("Resultado do Número do Curso")
            for dado in resultado:
                print(dado)
    else:
        input("Digite um valor válido !")
