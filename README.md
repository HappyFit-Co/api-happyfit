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
@@ -14,22 +18,60 @@

> O software proposto visa controlar a ingestão de alimentos e água, bem como gerenciar treinos de academia do usuário. Com interface web, o aplicativo oferecerá notificações sobre consumo de água e metas diárias, estimulando hábitos saudáveis
## 💻 Pré-requisitos
## Tópicos 

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou a versão mais recente de `<linguagem / dependência / requeridos>`
* Você tem uma máquina `<Windows / Linux / Mac>`. Indique qual sistema operacional é compatível / não compatível.
* Você leu `<guia / link / documentação_relacionada_ao_projeto>`.
:small_blue_diamond: [🐍 Execução localmente](#-execução-localmente)

## 🐍 Usando o HappyFit
:small_blue_diamond: [🐳 Execução com Docker](#-execução-com-docker)

Para usar a API RESTful HappyFit com docker basta seguir a etapa abaixo: 
:small_blue_diamond: [📃 Executando os testes unitários](#-executando-os-testes-unitários)

:small_blue_diamond: [🛠 Construído com](#-construído-com)

:small_blue_diamond: [📫 Documentação](#-documentação)

:small_blue_diamond: [🤝 Equipe](#-equipe)

:small_blue_diamond: [📄 Licença](#-licença)

## 🐍 Execução localmente

Este tutorial foi desenvolvido para usuários do Windows com um terminal PowerShell:
* Para executar o projeto localmente na sua máquina, precisa criar o ambiente virtual:
```
python -m venv env
```

* Em seguida, ative o ambiente virtual através do terminal, você notará que aparece '(env)':
```
.\env\Scripts\activate
```

* A seguir, baixe todas as dependências do arquivo 'requirements.txt':
```
pip install -r requirements.txt
```

* Agora, basta executar o arquivo 'server.py':
```
python -u server.py
```

* Depois disso, caso queira desativar o ambiente virtual execute no terminal:
```
deactivate
```

## 🐳 Execução com Docker
Para executar o projeto com docker, basta dar o seguinte comando no terminal na pasta raiz do projeto:
```
docker run -d --rm -p 5000:5000 happyfit
```

## 📃 Executando os testes unitários

## 🛠 Construído com

## 📫 Documentação

Confira a [Documentação do HappyFit]().
## 🤝 Equipe
Agradecemos às seguintes pessoas que contribuíram para este projeto:
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
## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.
[⬆ Voltar ao topo](#happyfit-restful-api)
