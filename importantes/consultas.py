def consulta_matricula(alunos, matricula_ref):
    for aluno in alunos:
        matricula = aluno.split(";")[0]
        if matricula == matricula_ref:
            return aluno.strip("\n").split(";")


def consulta_alunos(alunos, nome_ref):
    consulta = []
    for aluno in alunos:
        nome = aluno.split(";")[1]
        if nome_ref in nome:
            consulta.append(aluno.strip("\n").split(";"))
    return consulta


def consulta_cursos(alunos, curso_ref):
    consulta = []
    for aluno in alunos:
        curso = aluno.strip("\n").split(";")[-1]
        if curso == curso_ref:
            consulta.append(aluno.strip("\n").split(";"))
    return consulta