from flask import Flask, session, render_template, request

from Modules.GameSearch import search_results

app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        search_name = request.form["search_name"]
        sites = request.form.getlist("sites")
        session['sites'] = sites
        html = search_results(search_name, sites)
        return render_template('index.html', text=html)
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
