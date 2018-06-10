# mc536
Repositório para um trabalho da disciplina MC536
## Objetivo
O objetivo é a criação de uma interface que permita o manejamento de um banco de dados relacionados à Copa do Mundo.
Neste ambiente serão permitidas consultas e inserções no Banco de Dados.

O arquivo `main.py` contém a base para a execução da interface gráfica.
## Descrições
### Executar
Para executar faça `python main.py` num ambiente python 3.6 com os pacotes listados em `requirements.txt`.

Faça `pip install < requirements.txt` se não tiver os pacotes instalados na sua máquina.

### Desenvolvimento
O app está sendo desenvolvido utilizando o Tkinter, um módulo de python para encapsular e facilitar a criação de
ambientes gráficos usando Tk/Tcl.
## IMPORTANTE:
Desenvolver o projeto utilizando a [Git Workflow](https://guides.github.com/introduction/flow/) 

### Uso
Queries simples estao no pacote `queries`. Usar fazendo `import` statements.

Podemos acessar as queries simples no pacote `queries.simple`. Usar fazendo `from queries import simple` statement.

Para cada db temos acesso as suas funcoes por `queries.simple.jogador`. Usar fazendo 
`from queries.simple.jogador import get_time` statement para a funcao `get_time` da tabela jogador.

### Resumo:
* **NUNCA** faça commits diretamente na `master` ela é sagrada
* Novas features são implementadas em `feature-branches` 
* Após concluir uma feature, abra um **Pull Request** da sua branch com a `master`
  * **Code Reviews** antes de aceitar qualquer Pull Request são obrigatórias.
  * Teste exaustivamente o funcionamento da sua branch.
    * Garanta que sua `feature-branch` consiga ser mergeada na `master`
    * Garanta que sua `feature-branch` não quebre funcionalidades da `master`
* Confirme o pull request para fazer o merge da sua branch com a `master`
