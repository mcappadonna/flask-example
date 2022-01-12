from flask import Flask

app = Flask(__name__)

@app.route("/<int:a>/<int:b>")
def somma(a, b):
    return "Available endpoints:\n\n- /sum/<int>/<int>: return the sum of two integers"

@app.route("/sum/<int:a>/<int:b>")
def mysum(a, b):
    return "Sum: %d\n" % (a + b)
