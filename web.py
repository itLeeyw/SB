from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    pass
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}

app.run('127.0.0.1',8080)