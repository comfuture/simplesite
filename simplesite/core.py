from flask import Flask
from model import metadata, setup_all
import page, board, admin

# create application
app = Flask(__name__)

# load config
app.config.from_pyfile('config.py')

# register modules
app.register_module(admin.module)
app.register_module(page.module)
app.register_module(board.module)

# init database
metadata.bind = app.config.get('DATABASE')
setup_all(True)

@app.route('/')
def index():
    return 'index page'

