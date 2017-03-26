from flask import Flask

from api.baimen.baimen import login_module
from models.basicmodel import db

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db.app = app
db.init_app(app)

app.register_blueprint(login_module, url_prefix='/api/login')


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
