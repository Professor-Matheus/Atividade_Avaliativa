# 📝 Módulo 2: Perguntas Teóricas (Git & Engenharia de Software)

Responda às questões abaixo diretamente neste arquivo.

1. **O que caracteriza um "Commit Atômico" e por que commits gigantescos dificultam a integração e a rastreabilidade do código?**

   *Sua resposta aqui:commit atômico é aquele que contém uma alteração pequena, específica e relacionada a uma única tarefa ou objetivo. Commits gigantescos dificultam a integração porque aumentam a chance de conflitos entre as alterações de diferentes desenvolvedores. Além disso, tornam mais difícil identificar quando e por que determinada alteração foi feita, prejudicando a rastreabilidade, revisão e correção de problemas.

2. **Como ocorrem os conflitos de merge no Git e qual a melhor estratégia para resolvê-los de forma segura antes da integração?**

   *Sua resposta aqui: ocorrem quando duas branches fazem alterações diferentes na mesma parte de um arquivo, e o Git não consegue decidir automaticamente qual alteração deve ser mantida. A estratégia mais segura é atualizar a branch com as mudanças mais recentes da branch principal, identificar e analisar os conflitos, resolvê-los manualmente, testar o código e só então realizar o merge. Isso reduz o risco de integrar alterações incorretas ou quebrar funcionalidades existentes.
   
