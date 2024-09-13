# main.py

from ecommchatbot.data_genration import data_genration
from ecommchatbot.data_ingestion import data_ingest
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

vstore = data_ingest("done")
chain = data_genration(vstore=vstore)
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result=chain.invoke(input)
    print("Response : ", result)
    return str(result)

if __name__ == '__main__':
    app.run(debug= True)