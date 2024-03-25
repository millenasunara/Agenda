print("=-=-=-=-=-Agenda de Contatos=-=-=-=-=-")
agenda = {
    "Millena" : "1234-5678",
    "Dafne" : "2345-9787",
    "João" : "5443-8745",
    "Rose" : "6745-3432",
    "Carol": "8753-2394",
    "Mayza" : "3644-4873",
    "Bruno" : "3423-9854",
    "Joyce" : "7489-1233",
    "Beatriz" : "9877-6587",
    "Kamilly": "7879-7675"}
letraprocurada = input("Insira a letra (Maiúscula) para verificar se há na agenda de contatos: ")
comeca = {nome:telefone for nome, telefone in agenda.items()
if nome.startswith(letraprocurada)}

if comeca:
    print("\n---Contatos encontrados: ---")
    for nome, telefone in comeca.items():
        print(f"{nome}:{telefone}")

else:
    print("\n---Nenhum contato encontrado!---")

num = input("\n---Insira o primeiro número : ---")
encontrado = []

for nome, telefone in agenda.items():
         if telefone.startswith(num):
             encontrado.append((nome, telefone))

if encontrado:
         print("\n---Contatos encontrados com o número inicial inserido:---")
         for nome, telefone in encontrado:
             print(f"{nome}: {telefone}")
else:
    print("\n---Nenhum contato foi encontrado com o número inicial inserido.---")

num2 = input("\n---Insira o segundo número: ---")
encontrado = []

for nome, telefone in agenda.items():
    if telefone.endswith(num2):
         encontrado.append((nome, telefone))

if encontrado:
    print("\n---Contatos encontrados com o número final inserido:---")
    for nome, telefone in encontrado:
            print(f"{nome}: {telefone}")
else:
    print("\n---Nenhum contato foi encontrado com o número final inserido.---")