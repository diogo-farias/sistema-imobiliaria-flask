print("TESTE DO PYTHON FUNCIONANDO")

from flask import Flask, render_template, request, redirect
from config import conectar

app = Flask(__name__)

# ------------------------------
# PAGINA PRINCIPAL
# ------------------------------
@app.route("/")
def index():

    return render_template("index.html")


# ------------------------------
# TELA DE CADASTRO DE IMOVEL
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
    (endereco,cidade,valor,quartos,banheiros)
    VALUES (%s,%s,%s,%s,%s)
    """

    dados = (endereco, cidade, valor, quartos, banheiros)

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

    return render_template("listar_imoveis.html", imoveis=imoveis)


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

    return render_template("editar_imovel.html", imovel=imovel)


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
    SET endereco=%s, cidade=%s, valor=%s, quartos=%s, banheiros=%s
    WHERE id=%s
    """

    dados = (endereco, cidade, valor, quartos, banheiros, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/imoveis")


# ==============================
# CRUD DE PESSOAS
# ==============================

# ------------------------------
# CADASTRAR PESSOA
# ------------------------------
@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():

    return render_template("cadastrar_pessoa.html")


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
    (nome,telefone,email,cpf)
    VALUES (%s,%s,%s,%s)
    """

    dados = (nome, telefone, email, cpf)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


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

    return render_template("listar_pessoas.html", pessoas=pessoas)


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

    return render_template("editar_pessoa.html", pessoa=pessoa)


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
    SET nome=%s, telefone=%s, email=%s, cpf=%s
    WHERE id=%s
    """

    dados = (nome, telefone, email, cpf, id)

    cursor.execute(sql, dados)

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/pessoas")


# ------------------------------
# INICIAR SERVIDOR
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)