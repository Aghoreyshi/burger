import os

from flask import Flask, render_template, send_from_directory
#from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)

#----------------------------------------
# controllers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
