# Nome: Enos de Barros Cruz
# Rm: 561926
# Nome: Fabio Henrique
# Rm: 563048
# Nome: Lucas Miyoshi Matsuda
# Rm: 555295


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
        crianca = int(input("Total de crianças: "))
        adulto = int(input("Total de adultos: "))
        idoso = int(input("Total de idosas: "))
        mob_reduzida = int(input("Total de pessoas com mobilidade reduzida: "))
        ferido = int(input("Total de pessoas feridas: "))
        soma = crianca + adulto + idoso + mob_reduzida + ferido
        if soma == total:
            total_afetados.append(total)
            criancas.append(crianca)
            adultos.append(adulto)
            idosos.append(idoso)
            mobilidade_reduzida.append(mob_reduzida)
            feridos.append(ferido)
            break
        else:
            print(f"Erro!!! A soma {soma} não bate com o total de pessoas infomado {total} \nDigite os dados novamente!")


print("\n" + "="*40)
print("Relatório Final")
print("="*40)


print(f"\n Total de desastres registrados: {qtd_desastres}")

soma_criancas = sum(criancas)
soma_adultos = sum(adultos)
soma_idosos = sum(idosos)
soma_mobilidade = sum(mobilidade_reduzida)
soma_feridos = sum(feridos)

print("\n Pessoas afetadas por categoria:")
print(f"Crianças: {soma_criancas}")
print(f"Adultos: {soma_adultos}")
print(f"Idosos: {soma_idosos}")
print(f"Mobilidade reduzida: {soma_mobilidade}")
print(f"Feridos: {soma_feridos}")

categorias = [soma_criancas, soma_adultos, soma_idosos, soma_mobilidade, soma_feridos]
rotulos = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
mais_afetada = rotulos[categorias.index(max(categorias))]
print(f"\n Categoria mais afetada: {mais_afetada}")

indice_max = total_afetados.index(max(total_afetados))

print("\n Desastre com maior número de afetados:")
print(f"Total de pessoas afetadas: {total_afetados[indice_max]}")
print(f"Tipo: {tipos_desastres[indice_max]}")
print(f"Local:{ruas[indice_max]}, {bairros[indice_max]}, {cidades[indice_max]}, {paises[indice_max]}")

print(f"\n Total geral de pessoas afetadas: {sum(total_afetados)}")