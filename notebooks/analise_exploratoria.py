"""
PROJETO: Resumo de Bolso: Assistente de Estudo para Alunos
INTEGRANTES: André Cizotti (10409439), Gabriel Rodrigues (10409071), Giulia Araki (10408954)
SÍNTESE: Código de análise exploratória de texto para processamento de aulas.
HISTÓRICO: 
31/03/2026 - Versão inicial - Análise de frequência de termos técnicos e contagem de palavras.
"""

import collections

# Simulação das aulas carregadas do dataset
textos_aulas = [
    "A inteligência artificial utiliza modelos de linguagem para processar dados.",
    "O aprendizado de máquina é uma subárea importante da computação e IA."
]

def analisar_frequencia(textos):
    palavras = " ".join(textos).lower().split()
    contagem = collections.Counter(palavras)
    return contagem.most_common(5)

print("--- Análise Exploratória N1 ---")
print(f"Total de aulas processadas: {len(textos_aulas)}")
print(f"Termos mais frequentes identificados: {analisar_frequencia(textos_aulas)}")
