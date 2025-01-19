# Estou tendo varios erros de indentação no codigo ajuda do chat para idenficar isso 
from Banco import Banco
import mysql.connector # pode ser que seja aqui o erro 
class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", telefone = "",
    email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha


    def insertUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, telefone, email, senha) values (%s, %s, %s, %s)", (nome, telefone, email, senha)) # forma mais simple para evitar erro com as "" que deveria ter!  tirando essa nessecidade!

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = ?, telefone = ?, email = ? where id = ?", (nome, telefone, email, usuario))
            #c.execute("update usuarios set nome = '" + self.nome + "',
            #telefone = '" + self.telefone + "', email = '" + self.email +
            #"', usuario = '" + self.usuario + "', senha = '" + self.senha +
            #"' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor() # feito de uma forma simplificada para não ficar dando erro !

            c.execute("select * from usuarios where idusuario = " + idusuario + "  ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
        

# Classe para interação com o banco de dados
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",         # Substitua pelo usuário do seu banco
            password="",         # Substitua pela senha do seu banco
            database="trabalho_svendas" # Substitua pelo nome do seu banco
        )
        self.cursor = self.connection.cursor()

    def login(self, email, senha):
        query = "SELECT id FROM usuarios WHERE email=%s AND senha=%s"
        self.cursor.execute(query, (email, senha))
        return self.cursor.fetchone()

    def buscar_produtos(self):
        query = "SELECT id, nome, valor, quantidade_estoque FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def cadastrar_venda(self, nome_cliente, cpf, usuario_id, forma_pagamento, quantidade_parcelas, valor_total, produtos):
        try:
            # Inserir na tabela vendas
            query_venda = """
                INSERT INTO vendas (nome_cliente, cpf, usuario_id, forma_pagamento, quantidade_parcelas, valor_total)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query_venda, (nome_cliente, cpf, usuario_id, forma_pagamento, quantidade_parcelas, valor_total))
            venda_id = self.cursor.lastrowid

            # Inserir na tabela venda_produtos
            for produto_id, quantidade, preco_unitario in produtos:
                query_venda_produto = """
                    INSERT INTO venda_produtos (venda_id, produto_id, quantidade, preco_unitario)
                    VALUES (%s, %s, %s, %s)
                """
                self.cursor.execute(query_venda_produto, (venda_id, produto_id, quantidade, preco_unitario))

            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print("Erro ao cadastrar venda:", e)
            return False

    def buscar_vendas(self):
        query = """
            SELECT 
                v.id AS venda_id,
                v.nome_cliente AS Cliente,
                v.valor_total AS Valor_Total_Venda,
                v.data_venda AS Data_Venda,
                GROUP_CONCAT(p.nome SEPARATOR ', ') AS Produtos
            FROM vendas v
            JOIN venda_produtos vp ON v.id = vp.venda_id
            JOIN produtos p ON vp.produto_id = p.id
            GROUP BY v.id
            ORDER BY v.data_venda DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
