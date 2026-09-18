# 💻 Módulo 2: Exercício Prático de Código (Python)
# REGRA: Você deve implementar as funções abaixo e realizar NO MÍNIMO 3 COMMITS separados no Git, 
# cada um cobrindo uma funcionalidade ou correção específica.

def calcular_velocidade(sprints):
    """
    1. Função para calcular média de Story Points finalizados.
    sprints: lista de inteiros contendo os pontos de cada Sprint (ex: [12, 10, 14])
    """
    # TODO: def calcular_velocidade(sprints):
    # Se a lista estiver vazia, a velocidade é zero para evitar divisão por zero
    if not sprints:
        return 0.0
        
    # Lógica de soma e média
    total_pontos = sum(sprints)
    media = total_pontos / len(sprints)
    
    return media

# Exemplo de uso:
# dados_sprints = [12, 10, 14]
# print(calcular_velocidade(dados_sprints))  # Saída: 12.0

    pass


def validar_dependencia(tarefa_pai_concluida):
    """
    # TODO: def validar_dependencia(tarefa_pai_concluida: bool) -> bool:
    """
    Valida se a dependência técnica foi concluída.
    
    Retorna True se concluída, False caso contrário.
    """
    if tarefa_pai_concluida:
        return True
    return False

    pass



def status_release(sprints_estimadas):
    
    3. Função para formatar o status da release.
    sprints_estimadas: número inteiro indicando a quantidade de Sprints
    """
    # TODO: def status_release(sprints_estimadas: int) -> str:
    """Formata o status da release com base na quantidade de sprints."""
    plural = "Sprints" if sprints_estimadas != 1 else "Sprint"
    return f"Release prevista para {sprints_estimadas} {plural}"

    pass
