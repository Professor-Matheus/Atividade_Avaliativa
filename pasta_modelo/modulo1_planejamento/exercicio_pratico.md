# 📊 Módulo 1: Exercício Prático (Release Planning)

### Cenário
Sua equipe possui uma **Velocidade Média de 12 Story Points por Sprint**. O Product Backlog priorizado contém as seguintes tarefas:

| ID | Funcionalidade | Esforço (SP) | Dependência Técnica |
| :--- | :--- | :--- | :--- |
| A | Modelagem do Banco de Dados | 5 | Nenhuma |
| B | API REST de Autenticação | 8 | Tarefa A |
| C | Interface de Login (UI) | 3 | Tarefa B |
| D | Módulo de Pagamentos (API) | 8 | Tarefa A |
| E | Painel de Relatórios (UI) | 5 | Tarefas B e D |

---

### Responda:

1. **Cálculo da Release:** Qual o total de Story Points do projeto e em quantas Sprints a Release completa será entregue? (Apresente o cálculo simples).
   (a)5+(b)8+(c)3+(d)8+(e)5=29 SP
   29 / 12 = 3 Sprints

2. **Mapeamento de Dependências:** Monte o cronograma das Sprints (Sprint 1, Sprint 2, etc.) alocando as tarefas em cada uma, respeitando rigorosamente a capacidade de 12 SP/Sprint e as dependências técnicas.
   Sprint 1: A (5)
   Sprint 2: B (8)
   Sprint 3: D (8) 
   Sprint 4: C (3)
   Sprint 5: E (5)
