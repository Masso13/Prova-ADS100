def criar_matricula():
    with open("alunos.txt", "r", encoding="utf8") as alunos:
        matricula = int(alunos.readlines()[-1].split(";")[0]) + 1
        faltando = 4 - len(str(matricula))
        matricula = "{}{}".format("0"*faltando, matricula)
    return matricula