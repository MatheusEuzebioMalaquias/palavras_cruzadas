def escolher(titulo, itens):
    while True:
        print(f"\n{titulo}")
        for numero, item in enumerate(itens, start=1):
            print(f"{numero}. {item}")

        escolha = input("Escolha (0 para sair): ")

        if escolha == "0":
            return None

        if escolha.isdigit() and 1 <= int(escolha) <= len(itens):
            return int(escolha) - 1

        print("Opção inválida.")