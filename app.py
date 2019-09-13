from flask import Flask, render_template, request

from Modules.GameSeach import search_results

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_name = request.form["search_name"]
        html = search_results(search_name)
        return render_template('index.html', text=html)
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
