from flask import Flask, request, render_template_string

app = Flask(__name__)

def calcule(x):
    if type(x) == int:
        for i in range(1, x):
            x = i * x
        return x

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            x = int(request.form["x"])
            y = calcule(x)
            if y is not None:
                result = f"<p>Le factoriel de {x} est: {y} </p>"
            else:
                result = f"<p>Veuillez entrer un entier positif.</p>"
        except ValueError:
            result = "<p>Entrée invalide. Veuillez enyrer un nombre entier.</p>"           

    return render_template_string("""
    <html>
    <head>
        <title>calcule de factorielle</title>
    </head>
    <body>
        <h2>Calcul factorielle</h2>
        <form method="POST">
            <label for="x">x :</label>
            <input type="text" name="x" required><br><br>
            <button type="submit"></calculer</button>
        </form>
        <br>
        {{ result | safe }} 
    </body>
    </html>""", result=result)

if __name__ == "__main__":
    app.run(debug=True)