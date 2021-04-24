#　サーバ

# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def info():
    global addr, count
    addr = str(request.form['addr'])
    count = str(request.form['count'])
    return render_template('index.html', addr=addr, count=count)

@app.route("/", methods=["GET"])
def view():
    return render_template('index.html', addr=addr, count=count)

if __name__ == "__main__":
    app.run()