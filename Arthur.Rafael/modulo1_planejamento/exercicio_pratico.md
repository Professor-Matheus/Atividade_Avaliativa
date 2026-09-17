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
   29 SP (5 + 8 + 3 + 8 + 5)
   29 SP / 12 SP por sprint=2,41
   Release total = 4 sprints entregues

2. **Mapeamento de Dependências:** Monte o cronograma das Sprints (Sprint 1, Sprint 2, etc.) alocando as tarefas em cada uma, respeitando rigorosamente a capacidade de 12 SP/Sprint e as dependências técnicas.
   SprintID Funcionalidade Esforço (SP)Total da Sprint Capacidade Sobrando
   Sprint 1 A Modelagem do Banco de Dados 5 SP 5 SP 7SP
   Sprint 2 B API REST de Autenticação 8SP 8SP 4SP
   Sprint 3 CD Interface de Login (UI)Módulo de Pagamentos (API) 3SP 8SP 11SP 1SP
   Sprint 4 E Painel de Relatórios (UI) 5SP 5SP 7SP
