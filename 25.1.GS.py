tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

qtd_desastres = int(input("Digite a quantidade de desastres: "))

for i in range(qtd_desastres):
    print(f"\n Tipos de Desastres {i+1}")

    tipos_desastres.append(input("Digite qual o tipo do desastre ocorrido: "))
    paises.append(input("Digite o nome do pais em que ocorreu: "))
    cidades.append(input("Digite o nome da cidade em que ocorreu: "))
    bairros.append(input("Digite o nome do bairro em que ocorreu: "))
    ruas.append(input("Digite o nome da rua em que ocorreu: "))
    while True:
        total = int(input("Total de pessoas afetadas: "))
        criancas = int(input("Total de crianças: "))
        adultos = int(input("Total de adultos: "))
        idosos = int(input("Total de idosas: "))
        mobilidade_reduzida = int(input("Total de pessoas com mobilidade reduzida: "))
        feridos = int(input("Total de pessoas feridas: "))
        soma = criancas + adultos + idosos + mobilidade_reduzida + feridos
        if soma == total:
            total_afetados.append(total)
            criancas.append(criancas)
            adultos.append(adultos)
            idosos.append(idosos)
            mobilidade_reduzida.append(mobilidade_reduzida)
            feridos(feridos)

            break
        else:
            print(f"Erro!!! A soma {soma} não bate com o total de pessoas infomado {total} \nDigite os dados novamente!")


print("\n" + "="*40)
print("Relatório Final")
print("="*40)

print(f"Total de desastres {qtd_desastres}")






