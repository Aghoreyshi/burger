import os

from flask import Flask, render_template, send_from_directory, make_response

app = Flask(__name__)
app.config.from_pyfile('settings.py')

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
    resp = make_response(render_template('index.html'))
    resp.headers['Content-type'] = 'text/html; charset=utf-8'
    return resp

@app.route('/menu')
def menu():
    resp = make_response(render_template('menu.html'))
    resp.headers['Content-type'] = 'text/html; charset=utf-8'
    return resp

@app.route('/locations')
def locations():
    resp = make_response(render_template('locations.html'))
    resp.headers['Content-type'] = 'text/html; charset=utf-8'
    return resp

@app.route('/contact')
def contact():
    resp = make_response(render_template('contact.html'))
    resp.headers['Content-type'] = 'text/html; charset=utf-8'
    return resp

#app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
