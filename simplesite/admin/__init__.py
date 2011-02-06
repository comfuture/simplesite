from flask import Module, render_template

module = Module(__name__, url_prefix='/admin')

@module.route('/')
def index():
    return render_template('admin/index.html')

