# 💻 Módulo 2: Exercício Prático de Código (Python)
# REGRA: Você deve implementar as funções abaixo e realizar NO MÍNIMO 3 COMMITS separados no Git, 
# cada um cobrindo uma funcionalidade ou correção específica.

def calcular_velocidade(sprints):

    """
    1. Função para calcular média de Story Points finalizados.
    sprints: lista de inteiros contendo os pontos de cada Sprint (ex: [12, 10, 14])
    """

    # TODO: Implementar lógica de soma e média

    if not sprints:
        return 0

    return sum(sprints) / len(sprints)


def validar_dependencia(tarefa_pai_concluida):
    """
    2. Função para validar se a dependência técnica foi concluída.
    tarefa_pai_concluida: booleano (True ou False)
    """
    # TODO: Retornar True se concluída, False caso contrário
        return tarefa_pai_concluida


def status_release(sprints_estimadas):
    """
    3. Função para formatar o status da release.
    sprints_estimadas: número inteiro indicando a quantidade de Sprints
    """
    # TODO: Retornar string no formato "Release prevista para X Sprints"
    return f"Release prevista para {sprints_estimadas} Sprints"
    
