def filtrar_ciencia_dados(lista):
    resultado = []

    for pessoa in lista:
        if pessoa["area"] == "Ciência de Dados":
            resultado.append(pessoa["nome"])

    return resultado


participantes = [
    {"nome": "Ana", "area": "BI"},
    {"nome": "Bruna", "area": "Ciência de Dados"},
    {"nome": "Carla", "area": "BI"},
    {"nome": "Daniela", "area": "Engenharia de Dados"},
    {"nome": "Eduarda", "area": "BI"},
    {"nome": "Fernanda", "area": "Ciência de Dados"},
    {"nome": "Gabriela", "area": "BI"},
    {"nome": "Helena", "area": "Engenharia de Dados"},
    {"nome": "Isabela", "area": "BI"},
    {"nome": "Juliana", "area": "Ciência de Dados"},
    {"nome": "Karina", "area": "BI"},
    {"nome": "Larissa", "area": "Engenharia de Dados"}
]

resultado = filtrar_ciencia_dados(participantes)

print("Participantes interessadas em Ciência de Dados:")
for nome in resultado:
    print("-", nome)

print(f"\nTotal: {len(resultado)} participantes")