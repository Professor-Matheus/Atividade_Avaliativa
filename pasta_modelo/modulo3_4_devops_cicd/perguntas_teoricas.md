# 📝 Módulo 3 & 4: Automação DevOps e CI/CD

Responda às questões abaixo diretamente neste arquivo.

1. **O que é Integração Contínua (CI) e como ela se conecta com gatilhos (triggers) do Git como push e pull_request?**

   *Sua resposta aqui: é uma prática de desenvolvimento em que as alterações feitas no código são integradas frequentemente ao projeto e passam por verificações automáticas, como testes e validações. No GitHub Actions, os gatilhos push e pull_request podem iniciar automaticamente essas tarefas. O push executa o processo quando há um novo envio de código para o repositório, enquanto o pull_request pode executar os testes quando uma alteração é proposta para ser integrada à branch principal.


2. **Qual a função de um "Runner" na execução do GitHub Actions e qual a diferença entre o ambiente de testes/QA e o ambiente de produção na Entrega Contínua (CD)?**

   *Sua resposta aqui: é o ambiente responsável por executar as tarefas definidas em um workflow do GitHub Actions, como instalar dependências, executar testes e verificar o código. No processo de Entrega Contínua (CD), o ambiente de testes/QA é utilizado para validar a aplicação e encontrar possíveis erros antes da publicação. Já o ambiente de produção é onde a aplicação é disponibilizada para os usuários finais, por isso as alterações devem ser previamente testadas e aprovadas. 
