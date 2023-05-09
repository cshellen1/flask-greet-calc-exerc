# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def sub_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def mult_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def div_nums():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(int(div(a, b)))

operators = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult,
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = operators[operation](a,b)
    return str(int(res))
    
    