# Atividade_Avaliativa
Este repositório contém a avaliação prática e conceitual da disciplina, conectando o **Planejamento Ágil** à **Execução e Automação DevOps** através do uso estrito da linha de comando (Git CLI).

---

## Objetivo

O objetivo principal é simular o ciclo de vida real de um projeto de software: desde a estimativa de *backlog*, mapeamento de dependências de *release* e cálculo de *velocity*, até o desenvolvimento local com commits atômicos e a construção de pipelines automatizadas de CI/CD utilizando o **GitHub Actions**.

---

## Avaliação

* **Simulação de Fluxo Real:** Resolução de questões teóricas e práticas organizadas em módulos progressivos.
* **Rastreabilidade por Git CLI:** Avaliação baseada no histórico de commits, uso de operações de terminal (`git mv`, `git log`) e alternância de identificação local de autoria (`git config user.name`).
* **Pipeline Integrada:** Construção prática de workflows em YAML (`.github/workflows/ci_cd_pipeline.yml`) executados em *runners* na nuvem.

---

## Modalidades de Trabalho e Pontuação

| Modalidade | Teto de Pontuação | Critério de Validação no Git |
| :--- | :--- | :--- |
| **Individual** | **1,87 pt** | Todos os commits obrigatoriamente registrados sob o `user.name` do aluno. |
| **Em Dupla** | **3,75 pts** | **1,87 pt por integrante**, auditado individualmente via histórico de commits no repositório. |

> ⚠️ **Atenção para Duplas:** A autoria de cada módulo é verificada estritamente pelo parâmetro `user.name` registrado no commit. Se apenas um integrante assinar os commits, a pontuação total do repositório será limitada ao teto da modalidade individuale somente para este aluno.

---

## 📂 Estrutura de Arquivos do Repositório

Ao realizar o `git clone`, a estrutura inicial do projeto será:

```text
Atividade_Avaliativa/
├── README.md                                 # Guia geral e instruções da avaliação
├── .github/
│   └── workflows/
│       └── ci_cd_pipeline.yml                # Pipeline de CI/CD a ser configurada (Módulo 3 e 4)
├── historico_terminal.txt                    # Log exportado dos comandos CLI executados
└── pasta_modelo/                             # MUST: Renomear via 'git mv' para seu(s) nome(s)
    ├── modulo1_planejamento/
    │   ├── perguntas_teoricas.md             # Questões de Story Points, Velocity e Release Planning
    │   └── exercicio_pratico.md              # Exercício de cálculo de Sprints e dependências
    ├── modulo2_git_codigo/
    │   ├── perguntas_teoricas.md             # Questões de Commits Atômicos e Merge Conflicts
    │   └── app.js                            # Código JavaScript para implementação prática
    └── modulo3_4_devops_cicd/
        └── perguntas_teoricas.md             # Questões de GitHub Actions, Runners e Ambientes
```
---
# 1. Renomeação Obrigatória da Pasta (git mv)
Antes de iniciar qualquer resolução, altere a pasta pasta_modelo usando o comando do Git para registrar a renomeação no histórico:  

git mv pasta_modelo/ aluno_nome_sobrenome/
 ex: `git mv pasta_modelo/ alunoA_e_alunoB/`
 
---
# 2. Identificação Local de Autoria (git config)
Para garantia da nota, altere a identidade local do Git antes de fazer seus commits:
`git config --local user.name "Seu Nome Completo"
git config --local user.email "seu.email@escola.com"`

---
# Passo a Passo para executação 
1. Clonar o Repositório:
`git clone <URL_DO_REPOSITORIO> 
cd Atividade_Avaliativa`
>cd comando usado para se movimentar entre as pastas
---
2. Configurar o Usuário Local:
`git config --local user.name "Seu Nome" 
git config --local user.email "seu.email@escola.com"`
>--local informa que o registro deste usuario ficara apenas no repositorio atual.\
>user.name = seu nome , ficara registrado em todos os commits.\
>user.email = seu email.
2.1 Criar uma Branch
`git checkout -b aluno_nome_sobrenome  ou nomealunoA_nomealunoB`
>checkout serve para navegar entre as branches , comando `-b` serve para criar uma nova branch.
---
3. Renomear a Pasta Modelo:\
`git mv pasta_modelo/ seu_nome_sobrenome/ ou git mv pasta_modelo/ nomealunoA_nomealunoB/`\
`git commit -m "refactor: Renomeando Pasta Modelo"`
---
4. Resolver os Módulos:\
Responda às perguntas teóricas nos arquivos .md dos Módulos 1, 2 e 3/4.\
Resolva o cálculo de Release Planning no Módulo 1\
Implemente o arquivo app.py no Módulo 2 realizando no mínimo 3 commits atômicos.\
Corrija as lacunas (FIXME / TODO) no arquivo `.github/workflows/ci_cd_pipeline.yml.`

---
5. Exportar o Histórico do Terminal:\
   Para terminal Bash\
`history | tail -n 30 > historico_terminal.txt`\
  Para Terminal PowerShell\
`Get-History | Select-Object -Last 30 | Format-Table -Auto | Out-File -FilePath historico_terminal.txt`

---
6. Entrega Final:\
`git add .`\
`git commit -m "docs: finaliza exercicios e adiciona log do terminal"`\
`git push origin aluno_nome_sobrenome`

---

### Distribuição de Notas

| Módulo / Requisito | Foco Avaliado | Pontuação (Solo) | Pontuação (Dupla) |
| :--- | :--- | :--- | :--- |
| **Módulo 1** | Teoria de Estimativas + Exercício de Release Planning | 0,45 pt | 0,90 pt |
| **Módulo 2** | Teoria de Engenharia + Implementação em `app.js` (Commits atômicos) | 0,45 pt | 0,90 pt |
| **Módulo 3 & 4** | Teoria de DevOps + Correção da Pipeline em `.github/workflows/` | 0,57 pt | 1,15 pt |
| **Operação CLI** | Uso do `git mv`, histórico de terminal e mensagens de commit | 0,40 pt | 0,80 pt |
| **TOTAL** | | **1,87 pt** | **3,75 pts** |

> ⚠️ **Nota:** Para trabalhos em dupla, a pontuação de cada arquivo será auditada individualmente pelo parâmetro `user.name` nos commits do Git. Caso apenas um estudante realize os commits da dupla, a pontuação total da entrega será reclassificada para o teto da modalidade individual (**1,87 pt**).
