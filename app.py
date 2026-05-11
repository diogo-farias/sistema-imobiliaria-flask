print("TESTE DO PYTHON FUNCIONANDO")

from flask import Flask, render_template, request, redirect
from config import conectar

app = Flask(__name__)

# ==========================================================
# PAGINA PRINCIPAL
# ==========================================================
@app.route("/")
def index():

    return render_template("index.html")


# ==========================================================
# CRUD DE IMOVEIS
# ==========================================================

# ------------------------------
# TELA CADASTRAR IMOVEL
# ------------------------------
@app.route("/cadastrar")
def cadastrar():

    return render_template("cadastrar_imovel.html")


# ------------------------------
# SALVAR IMOVEL
# ------------------------------
@app.route("/salvar", methods=["POST"])
def salvar():

    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    valor = request.form["valor"]
    quartos = request.form["quartos"]
    banheiros = request.form["banheiros"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO imoveis
    (endereco, cidade, valor, quartos, banheiros)
    VALUES (%s, %s, %s, %s, %s)
    """

    dados = (
        endereco,
        cidade,
        valor,
        quartos,
        banheiros
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


# ------------------------------
# LISTAR IMOVEIS
# ------------------------------
@app.route("/imoveis")
def visualizar_imoveis():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM imoveis"

    cursor.execute(sql)

    imoveis = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template(
        "listar_imoveis.html",
        imoveis=imoveis
    )


# ------------------------------
# DELETAR IMOVEL
# ------------------------------
@app.route("/deletar/<int:id>")
def deletar(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM imoveis WHERE id = %s"

    cursor.execute(sql, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/imoveis")


# ------------------------------
# EDITAR IMOVEL
# ------------------------------
@app.route("/editar/<int:id>")
def editar(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM imoveis WHERE id = %s"

    cursor.execute(sql, (id,))

    imovel = cursor.fetchone()

    cursor.close()
    conexao.close()

    return render_template(
        "editar_imovel.html",
        imovel=imovel
    )


# ------------------------------
# ATUALIZAR IMOVEL
# ------------------------------
@app.route("/atualizar", methods=["POST"])
def atualizar():

    id = request.form["id"]

    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    valor = request.form["valor"]
    quartos = request.form["quartos"]
    banheiros = request.form["banheiros"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE imoveis
    SET endereco=%s,
    cidade=%s,
    valor=%s,
    quartos=%s,
    banheiros=%s
    WHERE id=%s
    """

    dados = (
        endereco,
        cidade,
        valor,
        quartos,
        banheiros,
        id
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/imoveis")


# ==========================================================
# CRUD DE PESSOAS
# ==========================================================

# ------------------------------
# CADASTRAR PESSOA
# ------------------------------
@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():

    return render_template(
        "cadastrar_pessoa.html"
    )


# ------------------------------
# SALVAR PESSOA
# ------------------------------
@app.route("/salvar_pessoa", methods=["POST"])
def salvar_pessoa():

    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    cpf = request.form["cpf"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO pessoas
    (nome, telefone, email, cpf)
    VALUES (%s, %s, %s, %s)
    """

    dados = (
        nome,
        telefone,
        email,
        cpf
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pessoas")


# ------------------------------
# LISTAR PESSOAS
# ------------------------------
@app.route("/pessoas")
def listar_pessoas():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM pessoas"

    cursor.execute(sql)

    pessoas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template(
        "listar_pessoas.html",
        pessoas=pessoas
    )


# ------------------------------
# DELETAR PESSOA
# ------------------------------
@app.route("/deletar_pessoa/<int:id>")
def deletar_pessoa(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM pessoas WHERE id = %s"

    cursor.execute(sql, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pessoas")


# ------------------------------
# EDITAR PESSOA
# ------------------------------
@app.route("/editar_pessoa/<int:id>")
def editar_pessoa(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM pessoas WHERE id = %s"

    cursor.execute(sql, (id,))

    pessoa = cursor.fetchone()

    cursor.close()
    conexao.close()

    return render_template(
        "editar_pessoa.html",
        pessoa=pessoa
    )


# ------------------------------
# ATUALIZAR PESSOA
# ------------------------------
@app.route("/atualizar_pessoa", methods=["POST"])
def atualizar_pessoa():

    id = request.form["id"]

    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    cpf = request.form["cpf"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE pessoas
    SET nome=%s,
    telefone=%s,
    email=%s,
    cpf=%s
    WHERE id=%s
    """

    dados = (
        nome,
        telefone,
        email,
        cpf,
        id
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pessoas")


# ==========================================================
# CRUD DE PAGAMENTOS
# ==========================================================

# ------------------------------
# CADASTRAR PAGAMENTO
# ------------------------------
@app.route("/cadastrar_pagamento")
def cadastrar_pagamento():

    return render_template(
        "cadastrar_pagamento.html"
    )


# ------------------------------
# SALVAR PAGAMENTO
# ------------------------------
@app.route("/salvar_pagamento", methods=["POST"])
def salvar_pagamento():

    nome_pagador = request.form["nome_pagador"]
    valor = request.form["valor"]
    data_pagamento = request.form["data_pagamento"]
    forma_pagamento = request.form["forma_pagamento"]
    status_pagamento = request.form["status_pagamento"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO pagamentos
    (
        nome_pagador,
        valor,
        data_pagamento,
        forma_pagamento,
        status_pagamento
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    dados = (
        nome_pagador,
        valor,
        data_pagamento,
        forma_pagamento,
        status_pagamento
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pagamentos")


# ------------------------------
# LISTAR PAGAMENTOS
# ------------------------------
@app.route("/pagamentos")
def listar_pagamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM pagamentos"

    cursor.execute(sql)

    pagamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template(
        "listar_pagamentos.html",
        pagamentos=pagamentos
    )


# ------------------------------
# DELETAR PAGAMENTO
# ------------------------------
@app.route("/deletar_pagamento/<int:id>")
def deletar_pagamento(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "DELETE FROM pagamentos WHERE id = %s"

    cursor.execute(sql, (id,))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pagamentos")


# ------------------------------
# EDITAR PAGAMENTO
# ------------------------------
@app.route("/editar_pagamento/<int:id>")
def editar_pagamento(id):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM pagamentos WHERE id = %s"

    cursor.execute(sql, (id,))

    pagamento = cursor.fetchone()

    cursor.close()
    conexao.close()

    return render_template(
        "editar_pagamento.html",
        pagamento=pagamento
    )


# ------------------------------
# ATUALIZAR PAGAMENTO
# ------------------------------
@app.route("/atualizar_pagamento", methods=["POST"])
def atualizar_pagamento():

    id = request.form["id"]

    nome_pagador = request.form["nome_pagador"]
    valor = request.form["valor"]
    data_pagamento = request.form["data_pagamento"]
    forma_pagamento = request.form["forma_pagamento"]
    status_pagamento = request.form["status_pagamento"]

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE pagamentos
    SET nome_pagador=%s,
    valor=%s,
    data_pagamento=%s,
    forma_pagamento=%s,
    status_pagamento=%s
    WHERE id=%s
    """

    dados = (
        nome_pagador,
        valor,
        data_pagamento,
        forma_pagamento,
        status_pagamento,
        id
    )

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pagamentos")


# ==========================================================
# INICIAR SERVIDOR
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)