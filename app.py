from flask import Flask, render_template

app = Flask(__name__)

# Rota '/' 
@app.route("/")
def exibir_home():
    return render_template("home.html")

# Rota '/contato'
@app.route("/contato")
def exibir_contato():
    return render_template("contato.html")

# Condição para rodar o servidor
if __name__ == "__main__":
    app.run(debug=True)