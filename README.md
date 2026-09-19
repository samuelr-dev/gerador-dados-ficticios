# Gerador de Dados Fictícios

Aplicação desktop em Python, com interface gráfica em Tkinter, que gera dados pessoais fictícios brasileiros (nome, telefone e CPF) e uma notícia fictícia sobre a pessoa gerada, criada por um modelo de linguagem por meio da API da Groq.

O projeto foi desenvolvido em grupo, como trabalho acadêmico.

## Aviso de uso

Os dados são gerados aleatoriamente e destinam-se a testes, demonstrações e estudo. Os CPFs são criados com dígitos verificadores válidos e, por acaso, podem coincidir com números reais. Por isso, não devem ser usados para fins reais, nem para se passar por outra pessoa ou em qualquer atividade ilícita.

## Funcionalidades

- Geração de nome, telefone (com DDD brasileiro) e CPF fictícios, com a biblioteca Faker (localização `pt_BR`)
- Exibição dos dados em formato de tabela na interface
- Geração de uma notícia fictícia curta com o nome gerado, dividida em título, cidade e data, e corpo do texto, usando o modelo `llama-3.1-8b-instant` pela API da Groq

## Tecnologias

- Python
- Tkinter (interface gráfica)
- Faker (geração de dados fictícios)
- pandas e tabulate (organização e formatação dos dados)
- Groq (API do modelo de linguagem)
- python-dotenv (leitura da chave de API a partir do arquivo `.env`)

## Estrutura

```
gerador-dados-ficticios/
├── .env.example
├── .gitignore
├── idlogo.png
├── main.py
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.10 ou superior
- Tkinter, que já vem na instalação padrão do Python no Windows e no macOS. No Linux, instale o pacote `python3-tk`.
- Chave de API da Groq, necessária apenas para a geração de notícias. Ela pode ser criada em [console.groq.com/keys](https://console.groq.com/keys).

## Como executar

1. Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/samuelr-dev/gerador-dados-ficticios.git
cd gerador-dados-ficticios
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux e no macOS, o segundo comando é `source venv/bin/activate`.

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo `.env` a partir do exemplo e coloque a sua chave de API:

```bash
copy .env.example .env
```

No Linux e no macOS, use `cp .env.example .env`. Em seguida, abra o arquivo `.env` e substitua `cole_sua_chave_aqui` pela sua chave:

```
GROQ_API_KEY=sua_chave_aqui
```

5. Execute a aplicação:

```bash
python main.py
```

## Configuração da chave de API

A chave da Groq é lida da variável `GROQ_API_KEY`, definida no arquivo `.env`. Esse arquivo está no `.gitignore` e não deve ser enviado ao repositório. Nunca escreva a chave diretamente no código.

Se a chave não estiver configurada, a geração de dados funciona normalmente. Ao clicar em "Gerar Notícia", a interface exibe um aviso pedindo a configuração da chave.

## Como usar

1. Clique em "Gerar Dados" para criar um nome, um telefone e um CPF fictícios.
2. Com os dados gerados, clique em "Gerar Notícia" para criar uma notícia fictícia com o nome exibido.

A notícia só pode ser gerada depois de os dados serem criados.

## Apresentação

Vídeo de apresentação do projeto: [youtube.com/watch?v=0_chL_33_1c](https://www.youtube.com/watch?v=0_chL_33_1c)

Observação: a gravação de tela foi refeita e sobreposta ao áudio, portanto os dois não estão totalmente sincronizados.

## Integrantes

<!-- Adicione aqui os demais integrantes do grupo -->
- Samuel Rodrigues
