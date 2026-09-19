# Importação das Libs
import os
from dotenv import load_dotenv
from faker import Faker
fake = Faker('pt_BR')
import pandas as pd
from tkinter import *
from tabulate import tabulate
from groq import Groq

# Carrega as variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Configuração da Janela/GUI
window = Tk()
window.title("Gerador de Dados Fictícios")
window.geometry('1920x1080')
icon = PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'idlogo.png'))
window.iconphoto(True, icon)
window.config(background="#478eff")


# Configuração da IA / API
# A chave da API da Groq é lida da variável GROQ_API_KEY, definida no arquivo .env.
# Veja o README. Nunca escreva a chave diretamente no código.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

idData = None

# Gerador de dados Aleatórios
def gerarDados():

    persons_ID = []
    dddBrasil = [11,12,13,14,15,16,17,18,19,
        21,22,24,27,28,
        31,32,33,34,35,37,38,
        41,42,43,44,45,46,47,48,49,
        51,53,54,55,
        61,62,63,64,65,66,67,68,69,
        71,73,74,75,77,79,
        81,82,83,84,85,86,87,88,89,
        91,92,93,94,95,96,97,98,99]
    
    for i in range (1):
        name = f"{fake.first_name()} {fake.last_name()}"
        numero = fake.bothify(text='9####-####')
        dddGerado = fake.random_element(dddBrasil)
        cpf = fake.cpf()
        telephone = f"({dddGerado}) {numero}"
        persons_ID.append([name, telephone, cpf])

    dados = pd.DataFrame(persons_ID, columns=['Nome', 'Telefone', 'CPF'])
    return dados

# Função para exibir os dados na tela
def exibirDados():
    global idData
    idData = gerarDados()

    dadosContainer.delete("1.0", END)
    texto = tabulate(idData, headers='keys', tablefmt='plain', showindex=False)
    dadosContainer.insert(END, texto)

    dadosContainer.tag_configure('header', 
                                 foreground="#53ffff",
                                 font=('Consolas', 15, 'bold'))
    dadosContainer.tag_add('header', "1.0", "1.end")

# Função para gerar a noticia
def gerarNoticia():

    if client is None:
        noticiaContainer.delete("1.0", END)
        noticiaContainer.insert(END, "⚠️ Chave da API não configurada. Defina GROQ_API_KEY no arquivo .env (veja o README).")
        return

    if idData is None:
        noticiaContainer.delete("1.0", END)
        noticiaContainer.insert(END, "⚠️ Gere os dados primeiro antes de criar uma notícia!")
        return

    # Extrai os dados da pessoa gerada para usar no prompt
    pessoa = idData.iloc[0]        

    noticiaContainer.delete("1.0", END)
    noticiaContainer.insert(END, "⏳ Gerando notícia...")
    window.update()

    # Prompt
    noticiaGerada = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": (
                    f"Gere uma notícia fictícia curta com o nome: {pessoa['Nome']}. "
                    f"A primeira linha deve ser apenas o título. "
                    f"A segunda linha deve ser apenas a cidade e data. "
                    f"O restante é o corpo da notícia. Sem asteriscos ou markdown."
                )
            }
        ]
    )

    texto = noticiaGerada.choices[0].message.content
    linhas = texto.splitlines()

    # Configuração da notícia, divindo as partes
    noticiaContainer.tag_configure('titulo', foreground="#53ffff", font=('Consolas', 20, 'bold'))
    noticiaContainer.tag_configure('local',  foreground="#aaaaaa", font=('Consolas', 12, 'italic'))
    noticiaContainer.tag_configure('corpo',  foreground="white",   font=('Consolas', 13))

    noticiaContainer.delete("1.0", END)
    for i, linha in enumerate(linhas):
        if i == 0:
            noticiaContainer.insert(END, linha + "\n\n", 'titulo')
        elif i == 1:
            noticiaContainer.insert(END, linha + "\n\n", 'local')
        else:
            noticiaContainer.insert(END, linha + "\n", 'corpo')

# Título Principal
label = Label(window, 
              text="GERADOR DE DADOS FICTÍCIOS", 
              font=('Arial', 40, 'bold'), 
              fg="white", 
              bg="#645ae4",
              relief=RIDGE,
              bd=10,
              padx=10,
              pady=10)
label.pack(pady=20)

# Botão para gerar os dados e exibir na tela
btnGerarDados = Button(window, text="Gerar Dados", command=exibirDados)
btnGerarDados.config(font=('Arial', 15, 'bold'),
                     fg="white",
                     bg="#0048b4",
                     relief=RIDGE,
                     bd=10,
                     padx=10,
                     pady=10)
btnGerarDados.config(activebackground="#53ffff",
                     activeforeground="black")
btnGerarDados.pack(pady=20)

# Container dos dados exibidos
dadosContainer = Text(window, width=65, height=3)
dadosContainer.config(font=('Consolas', 14),
                      fg="white",
                      bg="#2b2b2b",
                      bd=5,
                      padx=20,
                      pady=20)
dadosContainer.pack(pady=10)

# Botão para gerar notícia falsa e exibir na tela
btnGerarNotícia = Button(window, text="Gerar Notícia", command=gerarNoticia)
btnGerarNotícia.config(font=('Arial', 15, 'bold'),
                     fg="white",
                     bg="#0048b4",
                     relief=RIDGE,
                     bd=10,
                     padx=10,
                     pady=10)
btnGerarNotícia.config(activebackground="#53ffff",
                     activeforeground="black")
btnGerarNotícia.pack(pady=20)

# Container da notícia gerada
noticiaContainer = Text(window, width=120, height=20)
noticiaContainer.config(font=('Consolas', 14),
                      fg="white",
                      bg="#2b2b2b",
                      bd=5,
                      padx=20,
                      pady=20)
noticiaContainer.pack(pady=10)


window.mainloop()   