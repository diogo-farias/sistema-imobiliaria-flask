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
# TELA DE CADASTRO
# ------------------------------
@app.route("/cadastrar")
def cadastrar():

    return render_template("cadastrar_imovel.html")


# ------------------------------
# SALVAR IMÓVEL
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
# VISUALIZAR IMÓVEIS
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
# DELETAR IMÓVEL
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
# TELA DE EDITAR
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
# ATUALIZAR IMÓVEL
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


if __name__ == "__main__":
    app.run(debug=True)