# Documentação da Aplicação, Dockerfile e Automação

| GithubActions | GitHub | AWS | Docker | Flask | Python |
|---------------|--------|-----|--------|-------|--------|
| <img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=green" title="GithubActions" alt="githubactions" width="145" height="40"> | <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" title="GitHub" alt="github" width="105" height="35"> | <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white" title="AWS" alt="aws" width="60" height="35"> | <img src="https://img.shields.io/badge/docker-%232496ED.svg?style=for-the-badge&logo=docker&logoColor=white" title="Docker" alt="docker" width="95" height="35"> | <img src="https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" title="Flask" alt="flask" width="95" height="35"> | <img src="https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white" title="Python" alt="python" width="110" height="35"> |

## Índice
* [01 - Visão Geral da Aplicação](#01---visão-geral-da-aplicação)
* [02 - Principais Tecnologias](#02---principais-tecnologias)
* [03 - Funcionalidades](#03---funcionalidades)
* [04 - Dockerfile](#04---dockerfile)
* [05 - Como Utilizar a Aplicação](#05---como-utilizar-a-aplicação)
* [06 - Visão Geral da Automação](#06---visão-geral-da-automação)
* [07 - Jobs da Automação](#07---jobs-da-automação)
* [08 - Configurações Básicas](#08---configurações-básicas)
* [09 - Secrets](#09---secrets)

## Sobre os Integrantes 
| Nome | GitHub | Social |
| ---| ---| ---|
| Julio Vicente | [GitHub](https://github.com/Julio-vincente) | [LinkedIn](https://www.linkedin.com/in/julio-vicente-b08239276/) |
| Flavio Martins | [GitHub](https://github.com/Flaviomartinx) | [LinkedIn](https://www.linkedin.com/in/flavio-martins-mendes) |
| Guilherme do Carmo | [GitHub](https://github.com/GuiROC1) | [LinkedIn](https://www.linkedin.com/in/guilherme-r-carmo/) |
| Maria Oliveira | - | [LinkedIn](https://www.linkedin.com/in/maria-oliveiraa67) |

## 01 - Visão Geral da Aplicação
Esta aplicação foi desenvolvida em **Python** utilizando o framework **Flask** e a biblioteca **Pymysql** para se conectar a um banco de dados relacional hospedado na AWS. A aplicação expõe dados de duas tabelas: **livros** e **autores**, acessíveis por dois endpoints. Para garantir segurança, usamos variáveis de ambiente que evitam a exposição de credenciais diretamente no código.

## 02 - Principais Tecnologias
- **Flask**: Framework utilizado para gerenciar as rotas e endpoints.
- **Pymysql**: Biblioteca que permite a conexão com o banco de dados MySQL.
- **MySQL (RDS)**: Banco de dados utilizado para armazenar as informações da aplicação na AWS.
- **Variáveis de Ambiente**: Usadas para garantir a segurança das credenciais e configurações sensíveis.
- **Gunicorn**: Servidor WSGI para execução da aplicação Flask em produção.

## 03 - Funcionalidades
1. **Endpoint de Livros**: Retorna os registros da tabela de livros.
2. **Endpoint de Autores**: Retorna os registros da tabela de autores.
3. **Conexão Segura ao Banco**: Utiliza variáveis de ambiente para manter as credenciais protegidas.

## 04 - Dockerfile
O **Dockerfile** configura o ambiente necessário para rodar a aplicação, incluindo as dependências, diretórios e portas necessárias.

### Principais Configurações do Docker
- **Imagem Base**: Utiliza uma versão otimizada do Python para aplicativos Flask.
  ```dockerfile
  FROM python:3.11-alpine
  ```
- **Instalação de Dependências**: Automatizada a partir de um arquivo `requirements.txt`.
- **Porta Exposta**: Configura a aplicação para escutar na porta 80 internamente.
  ```dockerfile
  EXPOSE 80
  ```
- **Variáveis de Ambiente**: Definem a porta e o host da aplicação.
  ```dockerfile
  ENV FLASK_APP=app:app
  ENV FLASK_RUN_HOST=0.0.0.0
  ENV FLASK_RUN_PORT=80
  ```
- **Segurança do Contêiner**: A imagem base é leve, e ferramentas como **Snyk** podem ser usadas para análise de vulnerabilidades.

## 05 - Como Utilizar a Aplicação
Para replicar a configuração, basta copiar a pasta **Docker** e configurar as variáveis de ambiente dentro do RDS. Caso deseje testar localmente, execute os seguintes comandos:

```bash
docker build -t teste .
docker run -p 80:80 teste
```

## 06 - Visão Geral da Automação
A automação elimina a necessidade de registrar manualmente as imagens do Dockerfile. Ela realiza o registro automático das imagens no **ECR** da AWS, atribuindo uma tag com os cinco primeiros caracteres do último commit no GitHub. Além disso, a automação atualiza automaticamente o serviço no **ECS**.

## 07 - Jobs da Automação
A automação é composta por quatro jobs principais:
1. **Register-Images**: Registra as imagens do **Dockerfile** no **ECR**.
2. **Scan-Container**: Realiza uma análise de segurança no container usando o **Snyk**.
3. **Update-ECS**: Atualiza o serviço no **ECS** com a nova imagem.
4. **Verify-Deployment**: Valida se o container está funcionando corretamente no ECS.

## 08 - Configurações Básicas
Antes de utilizar a automação, configure um ambiente na AWS com ECS, ECR e permissões adequadas. A automação requer as seguintes configurações:

1. **ECS**: Um cluster configurado para hospedar os serviços.
2. **ECR**: Repositório para armazenar as imagens Docker.
3. **IAM Roles**: Permissões adequadas para os jobs.
4. **Snyk**: Conta na plataforma **Snyk** para configurar a variável de ambiente.

### Variáveis de Ambiente Necessárias
```text
AWS_ACCESS_KEY_ID = <Sua chave de acesso AWS>
AWS_REGION = <Região da sua conta AWS>
AWS_SECRET_ACCESS_KEY = <Sua chave secreta AWS>
ECR_URI = <URI do repositório ECR>
SNYK_TOKEN = <Token do Snyk>
DB_NAME = <Nome do banco de dados>
DB_HOST = <Host do banco de dados>
DB_USER = <Usuário do banco de dados>
DB_PASSWORD = <Senha do banco de dados>
ECS_CLUSTER = <Nome do cluster ECS>
ECS_SERVICE = <Nome do serviço ECS>
ECS_EXECUTION_ROLE_ARN = <ARN da role de execução ECS>
SECURITY_GROUPS = <ID do seu grupo de segurança usado no ECS>
SUBNETS = <IDs das subnets publicas utilizadas no ECS>
```

## 09 - Secrets
Para tornar a automação acessível no GitHub Actions, configure as seguintes **Secrets** no seu repositório:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `ECR_URI`
- `SNYK_TOKEN`
- `DB_NAME`
- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `ECS_CLUSTER`
- `ECS_SERVICE`
- `ECS_EXECUTION_ROLE_ARN`
- `SECURITY_GROUPS`
- `SUBNETS`