from conexao import Conexao as db

def consultar_produto(cod_produto):
    conexao = db()
    conn = conexao.conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto WHERE cod_produto = ?", (cod_produto,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def consultar_endereco(cod_endereco):
    conexao = db()
    conn = conexao.conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM endereco WHERE cod_endereco = ?", (cod_endereco,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def consultar_estoque(id_endereco=None, id_produto=None):
    conexao = db()
    conn = conexao.conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT produto.nome_produto, endereco.cod_endereco,quantidade
        FROM estoque
        JOIN produto ON estoque.id_produto = produto.id_produto,
        endereco on estoque.id_endereco = endereco.id_endereco

        WHERE produto.nome_produto = ? or endereco.cod_endereco=?
        """,
        (id_produto,id_endereco)
    )

    resultado = cursor.fetchall()
    conn.close()
    return resultado

