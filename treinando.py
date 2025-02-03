from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = 'Henr!quecastro01',
    database = 'avaliacoe_dos_filmes'
)
cursor = db.cursor()


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/salvar", methods=["POST"])
def salvar(): 
    nome = request.form["nome"]
    cursor.execute("INSERT INTO testes (nome) VALUES (%s)", (nome,))
    db.commit()
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)