from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Mishail"}
    return
