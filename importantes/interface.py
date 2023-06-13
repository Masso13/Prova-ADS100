def gerar_opcoes(opcoes):
    for i, opcao in enumerate(opcoes):
        print(f"({i + 1}) {opcao}")

def gerar_titulo(titulo):
    print("-=" * 10, titulo, "=-" * 10)