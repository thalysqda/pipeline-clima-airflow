# 🌤️ Weather Data Pipeline (ETL)

## 📌 Sobre o Projeto
Este é um projeto ponta a ponta de Engenharia de Dados focado na construção de um pipeline ETL (Extract, Transform, Load) automatizado. O objetivo do sistema é extrair dados meteorológicos em tempo real da API do OpenWeatherMap, realizar a limpeza e modelagem dos dados, e armazená-los em um banco de dados relacional para futuras análises. Toda a orquestração do fluxo é feita de forma automatizada e conteinerizada.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python (Pandas, Requests, SQLAlchemy)
* **Banco de Dados:** PostgreSQL
* **Orquestração:** Apache Airflow
* **Infraestrutura:** Docker & Docker Compose
* **Fonte de Dados:** OpenWeatherMap API

## ⚙️ Arquitetura do Pipeline
1.  **Extract:** Conexão com a API do OpenWeatherMap para coletar dados brutos (JSON) do clima de São Paulo.
2.  **Transform:** Utilização da biblioteca Pandas para "achatar" estruturas aninhadas, remover colunas desnecessárias, tipar os dados corretamente e converter os *timestamps* para o fuso horário local.
3.  **Load:** Carregamento do DataFrame tratado diretamente para uma tabela no PostgreSQL.
4.  **Orchestration:** O Apache Airflow gerencia o agendamento e a execução sequencial das tarefas de forma isolada via Docker.
