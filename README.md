# Documentação da Aplicação, Dockerfile e Automação

<p align="center">
  <img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=green" width="130">
  <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" width="80">
  <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white" width="60">
  <img src="https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white" width="80">
  <img src="https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" width="80">
  <img src="https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" width="80">
</p>

## Índice
* [01 - Visão Geral da Aplicação](#01---visão-geral-da-aplicação)
* [02 - Principais Tecnologias](#02---principais-tecnologias)
* [03 - Funcionalidades](#03---funcionalidades)
* [04 - Dockerfile](#04---dockerfile)
* [05 - Como utilizar a aplicação](#05---como-utilizar-a-aplicação)

## Sobre os Integrantes 
| Nome | GitHub | Social |
| ---| ---| ---|
|Julio Vicente | https://github.com/Julio-vincente | https://www.linkedin.com/in/julio-vicente-b08239276/
|Flavio Martins | https://github.com/Flaviomartinx | https://www.linkedin.com/in/flavio-martins-mendes
|Guilherme do Carmo | https://github.com/GuiROC1 | https://www.linkedin.com/in/guilherme-r-carmo/
|Maria Oliveira |  | https://www.linkedin.com/in/maria-oliveiraa67

# 01 - Visão Geral da Aplicação
Esta aplicação é desenvolvida em **Python** usando o framework **Flask**, **Pymysql**, **OS**, **logging**. Seu objetivo é conectar a um banco de dados relacional hospedado na AWS e expor dados de duas tabelas: **livros** e **autores** dentro de dois endpoints, nos utilizamos uma biblioteca para criar variaveis dentro da nossa aplicação para garantir um ambiente protegido e não expor seu **banco de dados** dentro da aplicação, com Flask nos criamos dois **endpoints** para buscar duas tabelas dentro do banco de dados e retornar elas.

# 02 - Principais Tecnologias
- **Flask**: Utilizado para gerenciar rotas e endpoints.
- **Pymysql**: Biblioteca utilizada para conectar ao banco de dados.
- **MySQL (RDS)**: Banco de dados que armazena as informações da aplicação dentro da AWS.
- **Variáveis de Ambiente**: Garantem segurança nas credenciais e configurações sensíveis.
- **Gunicorn**: Servidor WSGI utilizado para rodar a aplicação Flask de forma eficiente em produção.

# 03 - Funcionalidades
1. **Endpoint de Livros**: Retorna os registros armazenados na tabela de livros.
2. **Endpoint de Autores**: Retorna os registros da tabela de autores.
3. **Conexão Segura ao Banco**: Configurada para evitar exposição de credenciais.

# 04 - Dockerfile
O **Dockerfile** define o ambiente da aplicação, incluindo dependências, diretórios e portas necessárias para execução. Ele permite que a aplicação seja facilmente empacotada e executada em qualquer ambiente que suporte contêineres. 

### Principais Configurações do Docker
- **Imagem Base**: Uma versão otimizada do Python para aplicativos Flask.
  ```Dockerfile
  FROM python:3.11-alpine
  ```
- **Instalação de Dependências**: Automatizada a partir de um arquivo `requirements.txt` com bibliotecas como **Flask**, **pymysql**, **gnunicorn**.
- **Porta Exposta**: A aplicação é configurada para escutar na porta 80 internamente.
  ```Dockerfile
  EXPOSE 80
  ```
- **Variáveis de Ambiente**: Utilizadas para definir a porta e o host da aplicação.
  ```Dockerfile
  ENV FLASK_APP=app:app
  ENV FLASK_RUN_HOST=0.0.0.0
  ENV FLASK_RUN_PORT=80
  ```
- **Segurança do Contêiner**: Uso de imagem leve e análise de vulnerabilidades com ferramentas como **Snyk**.

# 05 - Como utilizar a aplicação
Para replicar o Dockerfile, será necessário copiar a pasta **Docker** inteira. Não será preciso baixar nenhuma biblioteca em sua máquina, apenas ter acesso a um repositório de **imagens Docker** e configurar as variaveis de **ambiente dentro do RDS**. 

Se for testar localmente, utilize os seguintes comandos:

```shell
docker build -t teste .
docker run -p 80:80 teste
```

# 06 - Visão Geral da Automação
A automação foi desenvolvida para eliminar a necessidade de registrar manualmente as imagens do Dockerfile. Ela realiza automaticamente o registro das imagens no repositório **ECR** da **AWS**. Além disso, cada nova imagem gerada recebe automaticamente uma tag contendo os cinco primeiros caracteres do último commit no GitHub. A automação também atualiza o serviço no **ECS**, garantindo que o ambiente seja atualizado de forma dinâmica e eficiente.

# 07 - Jobs da Automação
A automação conta com quatro jobs principais que garantem o funcionamento e a confiabilidade do processo:

- **Register-Images**: Registra as imagens do **Dockerfile** no **ECR** da AWS como repositório centralizado.
- **Scan-Container**: Realiza uma análise de segurança no container utilizando a ferramenta **Snyk**, para identificar e prevenir vulnerabilidades.
- **Update-ECS**: Atualiza o serviço no **ECS** utilizando a imagem registrada pelo primeiro job, garantindo que o ambiente reflita a nova versão.
- **Verify-Deployment**: Valida se o container está funcionando corretamente no ECS, verificando sua integridade e disponibilidade.

# 08 - Configurações Básicas
Para utilizar a automação, é necessário configurar previamente um ambiente na AWS, incluindo o ECS, ECR e permissões adequadas para execução. A automação requer:

1. **ECS**: Um cluster configurado para hospedar os serviços.
2. **ECR**: Um repositório para armazenar as imagens Docker.
3. **IAM Roles**: Permissões adequadas para execução dos jobs.
4. **Snyk**: Sera necessario uma conta dentro da plataforma `Snyk` para se configurar uma das variaveis de ambiente.

Aqui em baixo vai estar as variaveis necessarias para conseguir utilizar a automação
  ```text    
  AWS_ACCESS_KEY_ID = Chave access dentro da sua conta da AWS
  AWS_REGION = Região que sua conta se encontra
  AWS_SECRET_ACCESS_KEY = Chave secret dentro da sua conta da AWS
  ECR_URI = URI do seu repositorio ECR
  SNYK_TOKEN
  DB_NAME
  DB_HOST
  DB_USER
  DB_PASSWORD
  ECS_CLUSTER
  ECS_SERVICE
  ECS_EXECUTION_ROLE_ARN
  ```

## Secrets 
Dentro do seu repositorio vamos ter que configurar alguma Secrets para tornar essa workflow acessivel
AFHJDOFHASKDF