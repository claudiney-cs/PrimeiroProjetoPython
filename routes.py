from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    nome = "Claudiney - CSWeb"
    dados = {"profissao": "Programador", "canal": "CSWeb"}
    titulo = "Meu primeiro projeto"
    return render_template ('home.html', nome=nome, dados=dados, titulo=titulo)

@app.route("/about")
def about():
    return render_template ("about.html")

@app.route("/contato")
def contato():
    return render_template ("contato.html")

if __name__ == "__main__":
    app.run(debug=True)