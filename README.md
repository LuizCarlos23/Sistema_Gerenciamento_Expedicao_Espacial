# Sistema de Gerenciamento de Expedição Espacial

Este documento descreve o projeto da disciplina de Sistema de Gerenciamento de Expedição Espacial, que consiste na implementação de um sistema para administrar o cadastro de missões de expedições espaciais.

## Descrição Geral

O propósito do projeto é construir um Sistema de Gerenciamento de Expedição Espacial para facilitar o planejamento, monitoramento e execução de missões espaciais, desde o lançamento até o retorno. As principais funcionalidades incluem:

- **Create (Criar):** Adicionar novas missões ao sistema, incluindo campos como nome da missão, data de lançamento, destino, tripulação, carga útil.
- **Read (Ler):** Visualizar todas as missões registradas no sistema, exibindo detalhes básicos de cada missão. Recuperar os detalhes de uma missão específica com base no ID da missão. Pesquisar missões por intervalo de datas.
- **Update (Atualizar):** Modificar os detalhes de uma missão existente, permitindo atualizações em campos como destino, tripulação, carga útil, etc.
- **Delete (Deletar):** Excluir uma missão do sistema, removendo todos os dados associados, utilizando o ID da Missão.

## Tabela Missão

Atributos da Tabela de Missões:

1. **ID da Missão:** Um identificador único para cada missão espacial. Tipo de Dados: Inteiro (Chave Primária).
2. **Nome da Missão:** O nome atribuído à missão espacial. Tipo de Dados: Texto (String).
3. **Data de Lançamento:** A data em que a missão foi lançada. Tipo de Dados: Data.
4. **Destino:** O destino final da missão, como um planeta, lua ou órbita específica. Tipo de Dados: Texto (String).
5. **Estado da Missão:** O estado atual da missão, como "Ativa", "Concluída", "Abortada", etc. Tipo de Dados: Texto (String).
6. **Tripulação:** Uma lista dos membros da tripulação envolvidos na missão, o nome do membro: Texto (String).
7. **Carga Útil:** Uma descrição da carga útil transportada pela missão, incluindo equipamentos científicos, instrumentos de medição, etc. Tipo de Dados: Texto (String).
8. **Duração da Missão:** A duração planejada da missão, desde o lançamento até o retorno. Tipo de Dados: Intervalo de Tempo (Duração).
9. **Custo da Missão:** O custo total estimado da missão, incluindo custos de desenvolvimento, lançamento, operação e retorno. Tipo de Dados: Moeda (Decimal).
10. **Status da Missão:** Informações detalhadas sobre o status atual da missão. Tipo de Dados: Texto Longo (String ou Texto).

## Entrega do Projeto

O projeto será entregue em um único arquivo zip, com o nome "missoes_nome_da_equipe.zip". O arquivo deve conter os códigos e o relatório em formato .pdf, identificando o(s) nome(s) do(s) aluno(s) que realizou(aram) o projeto.

## Avaliação do Projeto

O projeto será avaliado de acordo com os seguintes critérios:

- **Total:** 5 pontos.
- **Qualidade do Design:** 0.5 ponto.
- **Qualidade do Código:** 4 pontos.
- **Relatório RAD:** 0.5 ponto.

## Equipes

- **Tkinter:** Até 3 pessoas.
- **Flask:** Até 3 pessoas. Implementação em Flask apenas API. É possível utilizar front-end para ganhar 0.5 ponto extra.

Observação: A validação da API em Flask será realizada através do Thunder Client.

**Equipe de Desenvolvimento:**
- Luiz Carlos Estevão
- Gabriel Ramos
- Nicolas Rock