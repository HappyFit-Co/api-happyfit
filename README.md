# HappyFit RESTful API

<div align="center">
  <img src="https://img.shields.io/static/v1?label=python&message=language&color=blue&style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/static/v1?label=flask%20restx&message=framework&color=orange&style=for-the-badge&logo=flask"/>
  <img src="http://img.shields.io/static/v1?label=License&message=MIT&color=green&style=for-the-badge"/>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/HappyFit-Co/api-happyfit?style=for-the-badge">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/HappyFit-Co/api-happyfit?style=for-the-badge">
  <img alt="GitHub forks" src="https://img.shields.io/github/forks/HappyFit-Co/api-happyfit?style=for-the-badge">
  <img alt="Bitbucket open issues" src="https://img.shields.io/bitbucket/issues/HappyFit-Co/api-happyfit?style=for-the-badge">
  <img alt="Bitbucket open pull request" src="https://img.shields.io/bitbucket/pr-raw/HappyFit-Co/api-happyfit?style=for-the-badge">
  <img src="http://img.shields.io/static/v1?label=STATUS&message=Development&color=GREEN&style=for-the-badge"/>
</div>

<div align="center">
  <img src="https://cdn.discordapp.com/attachments/445732137623224331/1088506154872750090/logo_happyfit.png" alt="logo HappyFit">
</div>

> O software proposto tem como objetivo controlar a ingestão de alimentos e água, além de gerenciar os treinos do usuário na academia. Com uma interface web intuitiva, o aplicativo oferecerá notificações sobre o consumo de água e metas diárias, incentivando a adoção de hábitos saudáveis.

## Tópicos 

:small_blue_diamond: [🐍 Execução localmente](#-execução-localmente)

:small_blue_diamond: [🐳 Execução com Docker](#-execução-com-docker)

:small_blue_diamond: [📃 Executando os Testes Unitários](#-executando-os-testes-unitários)

:small_blue_diamond: [⚙ Executando os Testes Automatizados](#-executando-os-testes-automatizados)

:small_blue_diamond: [📭 Postman e Testes Funcionais](#-postman-e-testes-funcionais)

:small_blue_diamond: [🛠 Construído com](#-construído-com)

:small_blue_diamond: [📫 Documentação](#-documentação)

:small_blue_diamond: [🤝 Equipe](#-equipe)

:small_blue_diamond: [📄 Licença](#-licença)

## 🐍 Execução localmente

Certifique-se de ter o Python instalado em sua máquina antes de prosseguir com essas etapas.

Este tutorial foi desenvolvido para usuários do Windows com um terminal PowerShell. Siga as etapas abaixo para executar o projeto localmente em sua máquina:

* Crie um arquivo chamado **_.env_** e configure corretamente as variáveis de ambiente necessárias. Você pode usar o arquivo **_.env.sample_** como referência.

* Crie um ambiente virtual executando o seguinte comando no terminal:
```
python -m venv env
```

* Em seguida, ative o ambiente virtual. Você verá que o prompt do terminal mostrará '(env)':
```
.\env\Scripts\activate
```

* Agora, instale todas as dependências listadas no arquivo 'requirements.txt', executando o seguinte comando:
```
pip install -r requirements.txt
```

* Com as dependências instaladas, execute o arquivo 'server.py' para iniciar o servidor:
```
python -u server.py
```

* Após a execução, você poderá acessar a API por meio da URL local fornecida no terminal.

* Se desejar parar a execução da aplicação, pressione `Ctrl + C` no terminal. Em seguida, você pode desativar o ambiente virtual executando o seguinte comando:
```
deactivate
```

Após desativar o ambiente virtual, a execução do projeto será encerrada.

Lembre-se de que, sempre que desejar executar novamente o projeto localmente, você precisará ativar o ambiente virtual antes de iniciar a aplicação.

## 🐳 Execução com Docker

Antes de executar o projeto com Docker, certifique-se de ter o [Docker](https://www.docker.com/get-started) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados em sua máquina. 

Para executar o projeto usando Docker, siga as etapas abaixo:

* Crie um arquivo chamado **_.env_** e configure corretamente as variáveis de ambiente necessárias. Você pode usar o arquivo **_.env.sample_** como referência.

* No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando:
```
docker-compose up
```
Isso iniciará os contêineres Docker necessários para executar o projeto.

Para parar a execução dos contêineres, pressione `Ctrl + C` no terminal. Isso interromperá a execução dos contêineres e liberará os recursos utilizados.

Caso deseje executar novamente o projeto usando o Docker, basta seguir novamente as etapas anteriores, garantindo que você tenha o arquivo **_.env_** configurado corretamente e execute o comando `docker-compose up` no terminal.

## 📃 Executando os Testes Unitários

## ⚙ Executando os Testes Automatizados

## 📭 Postman e Testes Funcionais

Neste projeto, incluímos um [arquivo Postman]() contendo uma coleção de requisições e testes funcionais para a API. Você pode importar facilmente esse arquivo no Postman para testar e interagir com a API.

Para importar a coleção do Postman e executar os testes, siga as etapas abaixo:

* Faça o download e instale o [Postman](https://www.postman.com/downloads/) em sua máquina.

* Após a instalação, abra o Postman.

* No topo da interface do Postman, clique em "File" e, em seguida, selecione "Import".

* Na janela de importação, clique na guia "File" e escolha o arquivo Postman fornecido neste projeto.

* Clique em "Import" para importar a coleção no Postman.

* Agora você pode executar os testes funcionais na API usando a coleção importada. Certifique-se de que o servidor esteja em execução antes de executar os testes.

Os testes funcionais fornecidos na coleção do Postman são projetados para validar o comportamento da API.

## 🛠 Construído com

* [Python](https://www.python.org/): Linguagem de programação poderosa e de alto nível.
* [Flask](https://flask.palletsprojects.com/): Framework web leve e flexível para Python.
* [Flask-RESTX](https://flask-restx.readthedocs.io/): Extensão do Flask para criação de APIs RESTful de maneira fácil e rápida.
* [MongoDB](https://www.mongodb.com/): Banco de dados NoSQL altamente escalável e flexível.
* [Swagger UI](https://swagger.io/tools/swagger-ui/): Interface de usuário interativa para explorar e testar APIs RESTful.
* [Docker](https://www.docker.com/): Plataforma de contêineres que facilita a criação e implantação de aplicativos em ambientes isolados.

Essas são as principais tecnologias utilizadas para construir esta API RESTful. O Flask e o Flask-RESTX são responsáveis por criar as rotas e manipular as respostas HTTP da API. O MongoDB é utilizado como banco de dados para armazenar e recuperar os dados da aplicação de forma eficiente. O Swagger UI fornece uma interface amigável para explorar e testar a API. O Docker é utilizado para empacotar a aplicação e suas dependências em contêineres, facilitando a implantação e a portabilidade.

## 📫 Documentação

A documentação do projeto e da API está disponível nos seguintes links:

- [Documentação do Projeto](https://cdn.discordapp.com/attachments/1089358473483006105/1111483062363111464/ProjectPlan_HappyFit.pdf): Este documento fornece uma visão geral do projeto HappyFit, incluindo sua finalidade, escopo e funcionalidades.
- [Documentação do Swagger](https://cdn.discordapp.com/attachments/1089358473483006105/1111479233684975616/Swagger_HappyFit.pdf): A documentação do Swagger descreve os endpoints e os modelos da API de forma detalhada.

Após executar a aplicação, você pode acessar o Swagger UI pela rota "/", onde encontrará uma interface interativa para explorar e testar a API.

Certifique-se de revisar esses documentos para obter mais informações sobre o projeto HappyFit e para entender como interagir com a API usando o Swagger UI. Eles fornecerão detalhes importantes sobre o escopo, os recursos e os endpoints disponíveis na aplicação.

## 🤝 Equipe

Gostaríamos de expressar nosso sincero agradecimento às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/mrjonas151">
        <img src="https://avatars.githubusercontent.com/u/89425034?v=4" width="100px;" alt="Foto do Jonas"/><br>
        <sub>
          <b>Jonas Tomaz de Aquinos</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Tchuc01">
        <img src="https://avatars.githubusercontent.com/u/106837080?v=4" width="100px;" alt="Foto do Luiz"/><br>
        <sub>
          <b>Luiz Henrique da Silva Araújo</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/phTononFerreira">
        <img src="https://avatars.githubusercontent.com/u/97487176?v=4" width="100px;" alt="Foto do Pedro"/><br>
        <sub>
          <b>Pedro Henrique Tonon Ferreira</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/takeshitos">
        <img src="https://avatars.githubusercontent.com/u/89425063?v=4" width="100px;" alt="Foto do Ricardo"/><br>
        <sub>
          <b>Ricardo Takeshi Outi Miyamoto</b>
        </sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/RobertoLuiz99">
        <img src="https://avatars.githubusercontent.com/u/117315179?v=4" width="100px;" alt="Foto do Roberto"/><br>
        <sub>
          <b>Roberto Luiz Pereira Raposo</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SidneyFerracinJr">
        <img src="https://avatars.githubusercontent.com/u/64179428?v=4" width="100px;" alt="Foto do Sidney"/><br>
        <sub>
          <b>Sidney Alexandre Ferracin Jr.</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/ViniciusGR797">
        <img src="https://avatars.githubusercontent.com/u/106624536?v=4" width="100px;" alt="Foto do Vinícius"/><br>
        <sub>
          <b>Vinícius Gomes Ribeiro</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

Agradecemos a todos os membros da equipe por seu trabalho árduo, dedicação e contribuições valiosas para o projeto. Seu empenho e habilidades foram fundamentais para o sucesso deste trabalho.

## 📝 Licença

Este projeto está licenciado sob os termos da [Licença](LICENSE). Por favor, consulte o arquivo LICENSE para obter mais detalhes.

A licença escolhida para o projeto é um elemento importante para estabelecer os direitos de uso, distribuição e modificações do código-fonte. É essencial que todos os usuários, colaboradores e interessados revisem e compreendam os termos e condições da licença antes de utilizar ou contribuir para o projeto.

Recomenda-se que você leia atentamente o arquivo LICENSE para garantir o cumprimento das regras estabelecidas e o uso adequado do código fornecido neste repositório.

[⬆ Voltar ao topo](#happyfit-restful-api)
