import csv
import os

# Passo 1: Crie uma lista vazia para armazenar os candidatos
candidatos = []

# Passo 2: Defina uma função para cadastrar candidatos
def cadastrar_candidato():
    candidato = {}  # Crie um dicionário para armazenar informações do candidato
    candidato["nome"] = input("Nome do candidato: ")
    
    # Solicite as notas para cada etapa
    candidato["entrevista"] = int(input("Nota da entrevista: "))
    candidato["teste_teórico"] = int(input("Nota do teste teórico: "))
    candidato["teste_prático"] = int(input("Nota do teste prático: "))
    candidato["soft_skills"] = int(input("Nota da avaliação de soft skills: "))
    
    # Adicione o candidato à lista de candidatos
    candidatos.append(candidato)

# Passo 3: Crie um menu de opções
while True:
    print("=" * 15)
    print("\033[0;35mMenu de Opções\033[m")
    print("=" * 15)
    print("\033[0;32m[1] Cadastrar Candidato")
    print("[2] Buscar Candidatos por Notas Mínimas")
    print("[3] Sair\033[m")
    
    opcao = input("Escolha uma opção: ")
    
    # Passo 4: Implemente as opções do menu
    if opcao == "1":
        cadastrar_candidato()
        print("Candidato cadastrado com sucesso!")
    elif opcao == "2":
        criterios = {}  # Crie um dicionário para armazenar critérios de notas mínimas
        criterios["entrevista"] = int(input("Nota mínima da entrevista: "))
        criterios["teste_teórico"] = int(input("Nota mínima do teste teórico: "))
        criterios["teste_prático"] = int(input("Nota mínima do teste prático: "))
        criterios["soft_skills"] = int(input("Nota mínima da avaliação de soft skills: "))
        
        candidatos_selecionados = []
        for candidato in candidatos:
            atende_criterios = all(candidato[etapa] >= nota_minima for etapa, nota_minima in criterios.items())
            if atende_criterios:
                candidatos_selecionados.append(candidato)
        
        if candidatos_selecionados:
            print("\033[0;33mCandidatos que atendem aos critérios:\033[m")
            for candidato in candidatos_selecionados:
                print("Nome:", candidato["nome"])
                print('e', criterios["entrevista"],'_t',criterios["teste_teórico"], '_p',criterios["teste_prático"], '_s',criterios["soft_skills"])
                
        else:
            print("\nNenhum candidato atende aos critérios informados.")
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")

# Passo 5: Encerre o programa quando o usuário escolher sair
print("Programa encerrado.")

# Passo 6: Salve os candidatos em um arquivo CSV (modo de anexação 'a')
def salvarcsv(cadastro):
    if not os.path.exists("cadastro.csv"):
        # Se o arquivo não existe, crie-o e escreva o cabeçalho
        with open("cadastro.csv", mode="w", newline="") as file:
            file.write("sep=,\n")
            fieldnames = ["Nome", "Entrevista", "Teste Teórico", "Teste Prático", "Soft Skills"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    # Abra o arquivo no modo de anexação
    with open("cadastro.csv", mode="a", newline="") as file:
        fieldnames = ["Nome", "Entrevista", "Teste Teórico", "Teste Prático", "Soft Skills"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
    # Se o arquivo não existir, escreva a linha de separação "sep=," e o cabeçalho
        if file.tell() == 0:
            file.write("sep=,\n")
            writer.writeheader()
        
        writer.writerows(cadastro)






