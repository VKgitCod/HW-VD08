from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    quote = None
    if request.method == 'GET':
        quote = get_quote()
    return render_template("index.html", quote=quote)

def get_quote():
    #api_key = "99ceb9ce40c34279852b74d789b0cbce"
    url = 'https://api.quotable.io/random'
    response = requests.get(url, verify=False)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)