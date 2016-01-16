from flask import Flask
from models.basicmodel import db

app = Flask(__name__)

app.config.from_pyfile('config_file.cfg')
db.app = app
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
