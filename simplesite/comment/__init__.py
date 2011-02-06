from flask import Module
from model import *

module = Module(__name__)

def get_comments(content_id):
    comments = Comment.query.filter_by(content=Content.query.filter(id=content_id)).all()
    return comments

@module.route('/<path:path>/@<int:content_id>/*')
def list(path):
    comments = get_comments(content_id)
    context = {'comments': comments}
    return render_template('comment/list.html', **context)

@module.route('/<path:path>/@<int:content_id>/+')
def form(path):
    return render_template('comment/form.html')

@module.route('/<path:path>/@<int:content_id>/', methods=['POST'])
def post(path):
    c = Comment(content=Content.query.filter_by(id=content_id).first(),
        author=request.values.get('author'))
    session.commit()
    return redirect(path)

@module.route('/<path:path>/@<int:content_id>/<int:id>', methods=['POST','PUT'])
def modify(path, content_id, id):
    c = Comment.query.filter_by(id=id).first()
    if c:
        # do edit values
        session.commit()
    return redirect(path)

@module.route('/<path:path>/@<int:content_id>/<int:id>', methods=['DELETE'])
def delete(path, id):
    return ''
