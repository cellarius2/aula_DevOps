from src.main import *

#Testa com dois valores corretos e um incorreto conforme resultado esperado
def test_filtrar_ciencia_dados():
    participantes = [
        {"nome": "Ana",     "area": "BI"},
        {"nome": "Bruna",   "area": "Ciência de Dados"},
        {"nome": "Fernanda","area": "Ciência de Dados"},
    ]
    assert filtrar_ciencia_dados(participantes) == ["Bruna", "Fernanda"]

#Testa com o campo vazio
def test_filtrar_lista_vazia():
    assert filtrar_ciencia_dados([]) == []

#Testa com todos valores incorretos conforme resultado esperado
def test_filtrar_sem_correspondencia():
    participantes = [
        {"nome": "Elena", "area": "Engenharia de Dados"},
        {"nome": "Isabela", "area": "BI"},
        {"nome": "Larissa", "area": "Engenharia de Dados"},
    ]
    assert filtrar_ciencia_dados(participantes) == []