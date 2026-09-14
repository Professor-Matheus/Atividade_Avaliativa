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
