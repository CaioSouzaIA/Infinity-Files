from db import conectar

class Produto:
    def __init__(self, nome, descricao, qtd_estoque, preco, id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.qtd_estoque = qtd_estoque
        self.preco = preco

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()
        if self.id is None:
            sql = "INSERT INTO PRODUTO (Nome, Descricao, Qtd_estoque, Preco) VALUES (%s, %s, %s, %s)"
            valores = (self.nome, self.descricao, self.qtd_estoque, self.preco)
            cursor.execute(sql, valores)
            self.id = cursor.lastrowid
        else:
            sql = "UPDATE PRODUTO SET Nome=%s, Descricao=%s, Qtd_estoque=%s, Preco=%s WHERE ID=%s"
            valores = (self.nome, self.descricao, self.qtd_estoque, self.preco, self.id)
            cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    def deletar(self):
        if self.id is None:
            return
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM VENDAS WHERE ID_do_produto_vendido = %s", (self.id,))
        conn.commit()
        cursor.execute("DELETE FROM PRODUTO WHERE ID=%s", (self.id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def listar_todos():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Nome, Descricao, Qtd_estoque, Preco FROM PRODUTO")
        produtos = []
        for (id, nome, descricao, qtd_estoque, preco) in cursor.fetchall():
            produtos.append(Produto(nome, descricao, qtd_estoque, preco, id))
        cursor.close()
        conn.close()
        return produtos

    def __str__(self):
        return f"Produto({self.id}, {self.nome}, Estoque: {self.qtd_estoque}, Preço: {self.preco})"

       
                
        

        
        


    
    
    
    
    
    
    
    
        

        
            
            
            