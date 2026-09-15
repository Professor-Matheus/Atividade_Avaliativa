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
   *Sua resposta: Story Point: 29 / Sprints: 2,41, contudo, se rrendondarmos é 3


2. **Mapeamento de Dependências:** Monte o cronograma das Sprints (Sprint 1, Sprint 2, etc.) alocando as tarefas em cada uma, respeitando rigorosamente a capacidade de 12 SP/Sprint e as dependências técnicas.
   *Sua resposta: 
   Sprint 1: Será realizada a Tarefa A – Modelagem do Banco de Dados, com esforço de 5 SP. Essa tarefa não possui dependências e, por isso, pode ser iniciada primeiro.

Sprint 2: Será realizada a Tarefa B – API REST de Autenticação, com esforço de 8 SP. Ela só pode ser iniciada após a conclusão da Tarefa A.

Sprint 3: Serão realizadas as Tarefas C – Interface de Login (3 SP) e D – Módulo de Pagamentos (8 SP), totalizando 11 SP. A Tarefa C depende de B, enquanto D depende de A. Portanto, ambas podem ser realizadas nesta Sprint sem ultrapassar o limite de 12 SP.

Sprint 4: Será realizada a Tarefa E – Painel de Relatórios (5 SP). Ela depende das Tarefas B e D, que já estarão concluídas ao final da Sprint 3.
   