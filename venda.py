from db import conectar
from produto import Produto
from datetime import date

class Venda:
    def __init__(self, id_do_produto, qtd_vendida, data_da_venda=None, id=None):
        self.id = id
        self.id_do_produto = id_do_produto
        self.qtd_vendida = qtd_vendida
        self.data_da_venda = data_da_venda or date.today()

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        # Verifica se tem estoque suficiente
        cursor.execute("SELECT Qtd_estoque FROM PRODUTO WHERE ID = %s", (self.id_do_produto,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise ValueError("Produto não encontrado.")
        estoque_atual = resultado[0]
        if estoque_atual < self.qtd_vendida:
            raise ValueError("Estoque insuficiente.")

        # Realiza a venda
        sql = "INSERT INTO VENDAS (ID_do_produto_vendido, Qtd_vendida, Data_da_venda) VALUES (%s, %s, %s)"
        valores = (self.id_do_produto, self.qtd_vendida, self.data_da_venda)
        cursor.execute(sql, valores)

        # Atualiza o estoque do produto
        novo_estoque = estoque_atual - self.qtd_vendida
        cursor.execute("UPDATE PRODUTO SET Qtd_estoque = %s WHERE ID = %s", (novo_estoque, self.id_do_produto))

        conn.commit()
        cursor.close()
        conn.close()

    def __str__(self):
        return f"Venda(Produto: {self.id_do_produto}, Qtd: {self.qtd_vendida}, Data: {self.data_da_venda})"
