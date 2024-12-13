# Documentação da Aplicação e Dockerfile

## Índice
- [Documentação da Aplicação e Dockerfile](#documentação-da-aplicação-e-dockerfile)
  - [Índice](#índice)
  - [Visão Geral da Aplicação](#visão-geral-da-aplicação)
    - [Principais Tecnologias](#principais-tecnologias)
    - [Funcionalidades](#funcionalidades)
  - [Dockerfile](#dockerfile)
    - [Principais Configurações do Docker](#principais-configurações-do-docker)

---

## Visão Geral da Aplicação
Esta aplicação é desenvolvida em **Python** usando o framework **Flask**, **Pymysql**, **OS**, e **logging**. Seu objetivo é conectar a um banco de dados relacional hospedado na AWS e expor dados de duas tabelas: **livros** e **autores**.

### Principais Tecnologias
- **Flask**: Utilizado para gerenciar rotas e endpoints.
- **Pymysql**: Biblioteca utilizada para conectar ao banco de dados.
- **MySQL (RDS)**: Banco de dados que armazena as informações da aplicação.
- **Variáveis de Ambiente**: Garantem segurança nas credenciais e configurações sensíveis.

### Funcionalidades
1. **Endpoint de Livros**: Retorna os registros armazenados na tabela de livros.
2. **Endpoint de Autores**: Retorna os registros da tabela de autores.
3. **Conexão Segura ao Banco**: Configurada para evitar exposição de credenciais.

---

## Dockerfile
O **Dockerfile** define o ambiente da aplicação, incluindo dependências, diretórios e portas necessárias para execução. Ele permite que a aplicação seja facilmente empacotada e executada em qualquer ambiente que suporte contêineres. 

### Principais Configurações do Docker
- **Imagem Base**: Uma versão otimizada do Python para aplicativos Flask.
  ```
  FROM python:3.11-alpine
  ```
- **Instalação de Dependências**: Automatizada a partir de um arquivo `requirements.txt`.
- **Porta Exposta**: A aplicação é configurada para escutar na porta 80 internamente.
- **Variáveis de Ambiente**: Utilizadas para definir a porta e o host da aplicação.
  ```
  ENV FLASK_APP=app:app
  ENV FLASK_RUN_HOST=0.0.0.0
  ENV FLASK_RUN_PORT=80
  ```
- **Segurança do Contêiner**: Uso de imagem leve e análise de vulnerabilidades com ferramentas como **Snyk**.
