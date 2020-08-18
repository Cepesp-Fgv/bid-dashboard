# Big Data para o Desenvolvimento Urbano Sustentável

Será criada uma plataforma a partir dos dados que já estão em CKAN (vide TR6) adicionando algumas usabilidades à base. Esse produto pretende agregar duas usabilidades definidas em um sentido amplo:

1. a capacidade de visualização e tabulação desses dados de maneira simples pelos cidadãos
2. a possibilidade de as cidades adicionarem dados sobre o desenvolvimento de projetos urbanos permitindo aos cidadãos acompanhar o andamento do projeto.

## Como Executar o Projeto

Instale os pré-requisitos (Utilizando Virtual Env):
```
pip3 install virtualenv
virtualenv .venv --python=python3
pip install -r requirements.txt
```

Copie o exemplo (.env.example) e altere as variáveis de ambiente (arquivo .env):
```shell
cp .env.example .env
```

Para executar o servidor (em modo desenvolvedor)
```shell
python application.py
```

## Como visualizar dashboards

No Quicksight, adicione um usuário como Leitor.
No arquivo ".env" atribua a variável `AWS_QUICKSIGHT_USER_EMAIL` o e-mail do usuário criado.
É possível visualizar dashboards acessando https://[DOMINIO]/dashboards?id=[ID_DO_PAINEL_NO_QUICKSIGHT]

Exemplos:
- https://fgv.urbbox.com.br/dashboards?id=e325202f-a9ea-4b0e-b7e9-fb1253968ef6
- https://fgv.urbbox.com.br/dashboards?id=f594eb2d-babd-4de6-b438-8b29381917b0
- https://fgv.urbbox.com.br/dashboards?id=5ed4741f-66af-4dba-b7f3-461eb608cfcb
