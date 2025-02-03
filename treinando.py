from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
    host= "mysql-5e358e5-henricaua18-0424.k.aivencloud.com",
    user = "avnadmin",
    password = 'AVNS_6zJohm7nIe9u_7o21HU',
    database = 'defaultdb'
)
cursor = db.cursor()


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/salvar", methods=["POST"])
def salvar(): 
    nome = request.form["nome"]
    cursor.execute("INSERT INTO teste (nome) VALUES (%s)", (nome,))
    db.commit()
    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)
