
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Banco import Database  # Importa a classe Database do arquivo de backend
import tkinter as tk;
db = Database()

def configurar_placeholder(entry, placeholder):
    def on_click(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focusout(event):
        if entry.get() == "":
            entry.insert(0,placeholder)
            entry.config(fg='gray')

    entry.insert(0, placeholder)
    entry.config(fg='gray')
    entry.bind("<FocusIn>", on_click)
    entry.bind("<FocusOut>", on_focusout)


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"



# Função para realizar login
def fazer_login():
    email = email_entry.get()  # Pega o email inserido pelo usuário
    senha = senha_entry.get()  # Pega a senha inserida pelo usuário

    usuario = db.login(email, senha)  # Realiza a validação no banco de dados
    if usuario:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")  # Mostra mensagem de sucesso
        usuario_id.set(usuario[0])  # Salva o ID do usuário no campo usuario_id
        abrir_home()  # Abre a tela inicial após o login
    else:
        messagebox.showerror("Erro", "Credenciais inválidas!")  # Caso as credenciais sejam inválidas

# Tela de login
def abrir_login():
    for widget in root.winfo_children():  # Limpa todos os widgets da tela atual
        widget.destroy()

    bg_image = Image.open("img.jpg")

    bg_image = bg_image.resize((root.winfo_screenwidth(), root. winfo_screenheight())) 

    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)

    bg_label.image = bg_photo

    bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    login_frame = tk.Frame(root, bg="black", bd=2, relief=tk.RIDGE)

    login_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

    tk.Label(login_frame, text="Login", font=("Arial", 20, "bold"),bg="black", fg="white").pack(pady=10)

    tk.Label(login_frame, text="Email:", font=("Arial", 12), bg="black", fg="white", anchor="w").pack(fill='x', padx=34, pady=5)
    global email_entry
    email_entry = tk.Entry(login_frame, width=35, font=("Arial",12))
    email_entry.pack(pady=5)
    configurar_placeholder(email_entry,"Digite seu email")
    
    tk.Label(root, text="Senha:").pack(pady=5)  # Label para o campo de senha
    global senha_entry  # Cria a variável global para o campo de senha
    senha_entry = tk.Entry(root, show="*")  # Cria o campo de entrada de senha (oculta os caracteres)
    senha_entry.pack()

    tk.Button(root, text="Entrar", command=fazer_login).pack(pady=10)  # Botão para realizar login

# Tela principal (Home)
def abrir_home():
    for widget in root.winfo_children():  # Limpa todos os widgets da tela atual
        widget.destroy()

    tk.Label(root, text="Bem-vindo!").pack(pady=10)  # Exibe a mensagem de boas-vindas
    tk.Button(root, text="Cadastrar Venda", command=abrir_cadastro_venda).pack(pady=10)  # Botão para ir para tela de cadastro de venda
    tk.Button(root, text="Vendas Realizadas", command=abrir_vendas_realizadas).pack(pady=10)  # Botão para ir para tela de vendas realizadas
    tk.Button(root, text="Sair", command=root.quit).pack(pady=10)  # Botão para sair do aplicativo

# Tela de cadastro de vendas
def abrir_cadastro_venda():
    for widget in root.winfo_children():  # Limpa todos os widgets da tela atual
        widget.destroy()

    tk.Label(root, text="Nome do Cliente:").pack(pady=5)  # Label para o campo de nome do cliente
    nome_cliente_entry = tk.Entry(root)  # Campo de entrada de nome do cliente
    nome_cliente_entry.pack()

    tk.Label(root, text="CPF:").pack(pady=5)  # Label para o campo de CPF
    cpf_entry = tk.Entry(root)  # Campo de entrada de CPF
    cpf_entry.pack()

    tk.Label(root, text="Forma de Pagamento:").pack(pady=5)  # Label para a forma de pagamento
    forma_pagamento_combo = ttk.Combobox(root, values=["à vista", "parcelado"])  # Combobox para escolher a forma de pagamento
    forma_pagamento_combo.pack()

    tk.Label(root, text="Quantidade de Parcelas:").pack(pady=5)  # Label para a quantidade de parcelas
    parcelas_entry = tk.Entry(root)  # Campo de entrada de quantidade de parcelas
    parcelas_entry.pack()

    tk.Label(root, text="Produtos:").pack(pady=5)  # Label para a lista de produtos
    produto_combo = ttk.Combobox(root)  # Combobox para selecionar o produto
    produto_combo.pack()

    tk.Label(root, text="Quantidade:").pack(pady=5)  # Label para a quantidade do produto
    quantidade_entry = tk.Entry(root)  # Campo de entrada da quantidade do produto
    quantidade_entry.pack()

    produtos = db.buscar_produtos()  # Consulta os produtos no banco de dados
    produto_map = {}  # Dicionário para mapear o nome do produto ao seu id e valor
    for produto in produtos:
        produto_id, nome, valor, estoque = produto  # Extrai as informações do produto
        produto_map[nome] = (produto_id, valor, estoque)  # Adiciona ao dicionário
    produto_combo["values"] = list(produto_map.keys())  # Define as opções no combobox

    venda_produtos = []  # Lista para armazenar os produtos da venda

    def adicionar_produto():
        produto_selecionado = produto_combo.get()  # Pega o nome do produto selecionado
        quantidade = quantidade_entry.get()  # Pega a quantidade do produto inserida

        if produto_selecionado and quantidade.isdigit():  # Verifica se a quantidade é válida
            quantidade = int(quantidade)  # Converte para inteiro
            produto_id, valor, estoque = produto_map[produto_selecionado]  # Obtém o produto selecionado
            if quantidade > estoque:  # Verifica se a quantidade solicitada não é maior que o estoque
                messagebox.showerror("Erro", "Quantidade em estoque insuficiente!")
                return

            venda_produtos.append((produto_id, quantidade, valor))  # Adiciona o produto à lista de venda
            messagebox.showinfo("Sucesso", f"{quantidade} unidade(s) de {produto_selecionado} adicionadas à venda!")  # Confirmação

    tk.Button(root, text="Adicionar Produto", command=adicionar_produto).pack(pady=10)  # Botão para adicionar o produto à venda
    
    


    def salvar_venda():
        nome_cliente = nome_cliente_entry.get()  # Obtém o nome do cliente
        cpf = cpf_entry.get()  # Obtém o CPF do cliente
        forma_pagamento = forma_pagamento_combo.get()  # Obtém a forma de pagamento
        quantidade_parcelas = parcelas_entry.get()  # Obtém a quantidade de parcelas

        # Calcula o valor total da venda
        valor_total = sum(quantidade * valor for _, quantidade, valor in venda_produtos)

        if db.cadastrar_venda(nome_cliente, cpf, usuario_id.get(), forma_pagamento, quantidade_parcelas or None, valor_total, venda_produtos):
            messagebox.showinfo("Sucesso", "Venda cadastrada com sucesso!")  # Confirmação de cadastro
            abrir_vendas_realizadas()  # Abre a tela de vendas realizadas
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar venda!")  # Erro no cadastro

    tk.Button(root, text="Salvar Venda", command=salvar_venda).pack(pady=10)  # Botão para salvar a venda

    tk.Button(root, text="Sair", command=abrir_home).pack(pady=10)  # Botão para voltar a pagina inicial

# Tela de Vendas Realizadas
def abrir_vendas_realizadas():
    for widget in root.winfo_children():  # Limpa todos os widgets da tela atual
        widget.destroy()

    tk.Label(root, text="Vendas Realizadas").pack(pady=10)  # Exibe o título da tela

    vendas = db.buscar_vendas()  # Busca todas as vendas realizadas no banco de dados

    # Cria a tabela para exibir as vendas realizadas
    tree = ttk.Treeview(root, columns=("ID Venda", "Cliente", "Valor Total", "Data da Venda", "Produtos"), show="headings")
    tree.heading("ID Venda", text="ID Venda")
    tree.heading("Cliente", text="Cliente")
    tree.heading("Valor Total", text="Valor Total")
    tree.heading("Data da Venda", text="Data da Venda")
    tree.heading("Produtos", text="Produtos")
    tree.pack(fill=tk.BOTH, expand=True)  # Exibe a tabela na tela

    # Insere os dados de vendas na tabela
    for venda in vendas:
        venda_id, cliente, valor_total, data_venda, produtos = venda  # Desempacota a venda
        tree.insert("", tk.END, values=(venda_id, cliente, f"R${valor_total:.2f}", data_venda, produtos))  # Insere cada venda

    # Botão para voltar à tela inicial
    tk.Button(root, text="Voltar ao Início", command=abrir_home).pack(pady=10)
    

# Inicialização do aplicativo
root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("500x500")  # Define o tamanho da janela

usuario_id = tk.IntVar()  # Armazena o ID do usuário logado

abrir_login()  # Abre a tela de login

root.mainloop()  # Executa o loop principal da interface gráfica
