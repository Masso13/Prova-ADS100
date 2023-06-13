from importantes.constants import CURSOS, SEXOS
from importantes.interface import gerar_titulo, gerar_opcoes
from importantes import criar_matricula

matricula = criar_matricula()

with open("alunos.txt", "a", encoding="utf8") as alunos:
    gerar_titulo("Cadastro de Alunos")

    nome = input("Digite o seu nome completo: ").title()

    # Sexo
    gerar_titulo("Selecione o seu Sexo")
    while True:
        gerar_opcoes(SEXOS)

        escolha = int(input("\n> "))

        if escolha-1 in range(len(SEXOS)):
            sexo = SEXOS[escolha-1]
            break
        else:
            input("Digite um valor válido !")

    # Endereço
    gerar_titulo("Informe o seu Endereço")
    logradouro = input("Logradouro: ").title()
    numero = int(input("Número Residencial: "))
    complemento = input("Complemento: ").capitalize()
    bairro = input("Bairro: ").title()
    cep = input("CEP: ")
    cidade = input("Cidade: ").title()

    # Contato
    gerar_titulo("Informe os seus Contatos")
    telefone = input("Telefone: ")
    email = input("E-mail: ").lower()

    gerar_titulo("Selecione o Pacote de Cursos")
    while True:
        gerar_opcoes(CURSOS)

        escolha = int(input("\n> "))

        if escolha-1 in range(len(CURSOS)):
            curso = list(CURSOS)[escolha-1]
            break
        else:
            input("Digite um valor válido !")
    
    alunos.write(f"{matricula};{nome};{sexo};{logradouro},{numero},{complemento},{bairro},{cep},{cidade};{telefone};{email};{curso}\n")