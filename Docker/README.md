# Docs app e Dockerfile

## Visão Geral da Aplicação
Esta aplicação é desenvolvida em **Python** usando o framework **Flask**, **Pymysql**, **OS**, **logging**. Seu objetivo é conectar a um banco de dados relacional hospedado na AWS e expor dados de duas tabelas: **livros** e **autores** dentro de dois endpoints, nos utilizamos uma bliblioteca para criar variaveis dentro da nossa aplicação para garantir um ambiente protegido e não expor seu banco de dados dentro da aplicação, com Flask nos criamos dois endpoints para buscar duas tabelas dentro do banco de dados e retornar ela.

### Principais Tecnologias
- **Flask**: Utilizado para gerenciar rotas e endpoints.
- **Pymysql**: Bliblioteca do python para conectar o banco de dados.
- **MySQL (RDS)**: Banco de dados que armazena as informações da aplicação.
- **Variáveis de Ambiente**: Garantem segurança nas credenciais e configurações sensíveis.

### Funcionalidades
1. **Endpoint de Livros**: Retorna os registros armazenados na tabela de livros.
2. **Endpoint de Autores**: Retorna os registros da tabela de autores.
3. **Conexão Segura ao Banco**: Configurada para evitar exposição de credenciais.

### Dockerfile
O **Dockerfile** define o ambiente da aplicação, incluindo dependências, diretórios e portas necessárias para execução. Ele permite que a aplicação seja facilmente empacotada e executada em qualquer ambiente que suporte contêineres, escolhemos a imagem python com alpine para ser mais maleavel e longe de vulnerabilidades, juntamente com **Snyk** nos garantimos a segurança do container.

## Principais Configurações do Docker
- **Imagem Base**: Uma versão otimizada do Python para aplicativos Flask.
- **Instalação de Dependências**: Automatizada a partir de um arquivo `requirements.txt`.
- **Porta Exposta**: A aplicação é configurada para escutar na porta 80 internamente.
- **Variaveis de ambiente**: Utilizamos o ENV para se utilizar as variaveis de ambiente.
    ```Dockerfile
    ENV FLASK_APP=app:app
    ENV FLASK_RUN_HOST=0.0.0.0
    ENV FLASK_RUN_PORT=80
    ```
